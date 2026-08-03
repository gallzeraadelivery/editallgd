#!/usr/bin/env python3
"""
Módulo de Empacotamento de APK
Responsável por reconstruir arquivos APK com todas as modificações aplicadas.
"""

import os
import tempfile
import zipfile
import logging
from pathlib import Path

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APKPackager:
    """Classe para empacotamento de APKs"""
    
    def __init__(self):
        """Inicializa o empacotador de APK"""
        self.temp_dir = None
        
    def package(self, modified_apk_path, output_path=None):
        """
        Empacota um APK modificado em um arquivo final
        
        Args:
            modified_apk_path (str): Caminho para o APK modificado
            output_path (str): Caminho para o arquivo de saída (opcional)
            
        Returns:
            str: Caminho para o APK empacotado final
        """
        
        # Verificar se o arquivo existe
        if not os.path.exists(modified_apk_path):
            raise FileNotFoundError(f"Arquivo APK não encontrado: {modified_apk_path}")
        
        try:
            # Se nenhum caminho de saída for especificado, usar o padrão
            if not output_path:
                base_name = os.path.splitext(modified_apk_path)[0]
                output_path = f"{base_name}_final.apk"
            
            # Copiar o APK modificado para o destino final
            import shutil
            shutil.copy2(modified_apk_path, output_path)
            
            logger.info(f"APK empacotado com sucesso em: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Erro durante o empacotamento do APK: {e}")
            raise
    
    def validate_package(self, apk_path):
        """
        Valida se o APK é um pacote válido
        
        Args:
            apk_path (str): Caminho para o arquivo APK
            
        Returns:
            bool: True se o APK for válido
        """
        try:
            # Verificar se o arquivo existe
            if not os.path.exists(apk_path):
                return False
            
            # Tentar abrir como ZIP para validar o formato
            with zipfile.ZipFile(apk_path, 'r') as apk:
                # Verificar se contém o manifesto necessário
                manifest_exists = any(name == 'AndroidManifest.xml' for name in apk.namelist())
                
                if not manifest_exists:
                    logger.warning("APK não contém AndroidManifest.xml")
                    return False
                
                # Verificar tamanho do arquivo
                file_size = os.path.getsize(apk_path)
                if file_size <= 0:
                    logger.warning("APK tem tamanho inválido")
                    return False
                
            logger.info("Validação do APK concluída com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"Erro durante a validação do APK: {e}")
            return False

# Exemplo de uso
if __name__ == "__main__":
    packager = APKPackager()
    
    # Exemplo de empacotamento (substitua pelos caminhos reais)
    # output_path = packager.package("exemplo_modificado.apk", "saida_final.apk")
    # print(f"APK empacotado em: {output_path}")
    
    # Exemplo de validação
    # is_valid = packager.validate_package("exemplo.apk")
    # print(f"APK válido: {is_valid}")
    
    print("Módulo de empacotamento de APK carregado com sucesso!")