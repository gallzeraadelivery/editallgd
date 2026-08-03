#!/usr/bin/env python3
"""
Módulo de Modificação de APK
Responsável por modificar os metadados e recursos de arquivos APK.
"""

import os
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APKModifier:
    """Classe para modificação de APKs"""
    
    def __init__(self):
        """Inicializa o modificador de APK"""
        self.apk_path = None
        self.temp_dir = None
        self.manifest_data = {}
        
    def modify(self, apk_path, modifications=None):
        """
        Modifica um arquivo APK com as alterações especificadas
        
        Args:
            apk_path (str): Caminho para o arquivo APK
            modifications (dict): Dicionário com modificações a serem aplicadas
            
        Returns:
            str: Caminho para o APK modificado
        """
        self.apk_path = apk_path
        self.temp_dir = tempfile.mkdtemp(prefix="apk_modification_")
        self.modifications = modifications or {}
        
        try:
            # Verificar se o arquivo existe
            if not os.path.exists(apk_path):
                raise FileNotFoundError(f"Arquivo APK não encontrado: {apk_path}")
            
            # Aplicar modificações
            modified_apk_path = self._apply_modifications()
            
            logger.info("Modificações aplicadas com sucesso")
            return modified_apk_path
            
        except Exception as e:
            logger.error(f"Erro durante a modificação do APK: {e}")
            raise
    
    def _apply_modifications(self):
        """
        Aplica as modificações especificadas ao APK
        
        Returns:
            str: Caminho para o APK modificado
        """
        try:
            # Criar cópia do APK original
            modified_apk_path = f"{self.apk_path}_modified.apk"
            
            # Copiar o APK original para o novo local
            import shutil
            shutil.copy2(self.apk_path, modified_apk_path)
            
            # Abrir o APK como arquivo ZIP para modificar
            with zipfile.ZipFile(modified_apk_path, 'r') as apk:
                # Extrair AndroidManifest.xml
                manifest_content = apk.read('AndroidManifest.xml')
                
            # Parsear o XML do manifesto
            root = ET.fromstring(manifest_content)
            
            # Aplicar modificações
            if 'package' in self.modifications:
                # Alterar package name
                old_package = root.get('{http://schemas.android.com/apk/res/android}package')
                new_package = self.modifications['package']
                root.set('{http://schemas.android.com/apk/res/android}package', new_package)
                logger.info(f"Package name alterado de {old_package} para {new_package}")
            
            if 'version_name' in self.modifications:
                # Alterar nome da versão
                version_name = self.modifications['version_name']
                root.set('{http://schemas.android.com/apk/res/android}versionName', version_name)
                logger.info(f"Nome da versão alterado para {version_name}")
            
            if 'version_code' in self.modifications:
                # Alterar código da versão
                version_code = str(self.modifications['version_code'])
                root.set('{http://schemas.android.com/apk/res/android}versionCode', version_code)
                logger.info(f"Código da versão alterado para {version_code}")
            
            if 'app_label' in self.modifications:
                # Alterar label do aplicativo
                application = root.find('application')
                if application is not None:
                    app_label = self.modifications['app_label']
                    application.set('{http://schemas.android.com/apk/res/android}label', app_label)
                    logger.info(f"Label do aplicativo alterado para {app_label}")
            
            # Salvar o manifesto modificado
            manifest_xml = ET.tostring(root, encoding='utf-8')
            
            # Recriar o APK com as modificações
            with zipfile.ZipFile(modified_apk_path, 'w') as apk:
                # Adicionar o manifesto modificado
                apk.writestr('AndroidManifest.xml', manifest_xml)
                
            return modified_apk_path
            
        except Exception as e:
            logger.error(f"Erro ao aplicar modificações: {e}")
            raise
    
    def cleanup(self):
        """Limpa diretórios temporários"""
        try:
            if self.temp_dir and os.path.exists(self.temp_dir):
                import shutil
                shutil.rmtree(self.temp_dir)
                logger.info("Diretórios temporários limpos")
        except Exception as e:
            logger.warning(f"Erro ao limpar diretórios temporários: {e}")

# Exemplo de uso
if __name__ == "__main__":
    modifier = APKModifier()
    
    # Exemplo de modificação (substitua pelos caminhos reais)
    # modifications = {
    #     'package': 'com.example.newapp',
    #     'version_name': '2.0',
    #     'version_code': 20,
    #     'app_label': 'Novo Aplicativo'
    # }
    # 
    # modified_path = modifier.modify("exemplo.apk", modifications)
    # print(f"APK modificado salvo em: {modified_path}")
    
    print("Módulo de modificação de APK carregado com sucesso!")