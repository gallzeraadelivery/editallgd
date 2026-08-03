#!/usr/bin/env python3
"""
Módulo de Assinatura de APK
Responsável por re-assinar arquivos APK com chaves válidas.
"""

import os
import subprocess
import tempfile
import logging
from pathlib import Path

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APKSigner:
    """Classe para assinatura de APKs"""
    
    def __init__(self):
        """Inicializa o assinador de APK"""
        self.key_store_path = None
        self.key_alias = None
        self.key_password = None
        self.store_password = None
        
    def sign(self, apk_path, key_store_path=None, key_alias=None, 
              key_password=None, store_password=None):
        """
        Assina um arquivo APK com uma chave válida
        
        Args:
            apk_path (str): Caminho para o arquivo APK
            key_store_path (str): Caminho para o keystore
            key_alias (str): Alias da chave
            key_password (str): Senha da chave
            store_password (str): Senha do keystore
            
        Returns:
            str: Caminho para o APK assinado
        """
        
        # Verificar se o arquivo existe
        if not os.path.exists(apk_path):
            raise FileNotFoundError(f"Arquivo APK não encontrado: {apk_path}")
        
        try:
            # Se nenhuma chave for fornecida, vamos gerar uma chave temporária
            if not all([key_store_path, key_alias, key_password, store_password]):
                logger.info("Gerando chave temporária para assinatura")
                return self._generate_and_sign_keyless(apk_path)
            
            # Usar a chave fornecida
            self.key_store_path = key_store_path
            self.key_alias = key_alias
            self.key_password = key_password
            self.store_password = store_password
            
            signed_apk_path = self._sign_with_existing_key(apk_path)
            return signed_apk_path
            
        except Exception as e:
            logger.error(f"Erro durante a assinatura do APK: {e}")
            raise
    
    def _generate_and_sign_keyless(self, apk_path):
        """
        Gera uma chave temporária e assina o APK
        
        Args:
            apk_path (str): Caminho para o arquivo APK
            
        Returns:
            str: Caminho para o APK assinado
        """
        try:
            # Criar diretório temporário
            temp_dir = tempfile.mkdtemp(prefix="apk_sign_")
            
            # Gerar chave temporária
            key_path = os.path.join(temp_dir, "debug.keystore")
            key_alias = "androiddebugkey"
            key_password = "android"
            store_password = "android"
            
            # Comando para gerar keystore (usando keytool)
            cmd = [
                "keytool", "-genkey", "-v",
                "-keystore", key_path,
                "-alias", key_alias,
                "-storepass", store_password,
                "-keypass", key_password,
                "-keyalg", "RSA",
                "-keysize", "2048",
                "-validity", "10000",
                "-dname", "CN=Android Debug,O=Android,C=US"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"Erro ao gerar keystore: {result.stderr}")
            
            logger.info("Keystore temporário gerado com sucesso")
            
            # Assinar o APK com a chave gerada
            signed_apk_path = f"{apk_path}_signed.apk"
            
            sign_cmd = [
                "jarsigner",
                "-keystore", key_path,
                "-storepass", store_password,
                "-keypass", key_password,
                "-signedjar", signed_apk_path,
                apk_path,
                key_alias
            ]
            
            result = subprocess.run(sign_cmd, capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"Erro ao assinar APK: {result.stderr}")
            
            logger.info("APK assinado com sucesso")
            return signed_apk_path
            
        except Exception as e:
            logger.error(f"Erro ao gerar e assinar com chave temporária: {e}")
            raise
    
    def _sign_with_existing_key(self, apk_path):
        """
        Assina o APK usando uma chave existente
        
        Args:
            apk_path (str): Caminho para o arquivo APK
            
        Returns:
            str: Caminho para o APK assinado
        """
        try:
            signed_apk_path = f"{apk_path}_signed.apk"
            
            sign_cmd = [
                "jarsigner",
                "-keystore", self.key_store_path,
                "-storepass", self.store_password,
                "-keypass", self.key_password,
                "-signedjar", signed_apk_path,
                apk_path,
                self.key_alias
            ]
            
            result = subprocess.run(sign_cmd, capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"Erro ao assinar APK: {result.stderr}")
            
            logger.info("APK assinado com sucesso usando chave existente")
            return signed_apk_path
            
        except Exception as e:
            logger.error(f"Erro ao assinar com chave existente: {e}")
            raise

# Exemplo de uso
if __name__ == "__main__":
    signer = APKSigner()
    
    # Exemplo de assinatura (substitua pelos caminhos reais)
    # signed_path = signer.sign(
    #     "exemplo.apk",
    #     key_store_path="caminho/para/keystore.jks",
    #     key_alias="meualias",
    #     key_password="senha123",
    #     store_password="senha456"
    # )
    # print(f"APK assinado salvo em: {signed_path}")
    
    print("Módulo de assinatura de APK carregado com sucesso!")