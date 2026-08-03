#!/usr/bin/env python3
"""
Módulo de Análise de APK
Responsável por analisar e extrair informações de arquivos APK.
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

class APKAnalyzer:
    """Classe para análise de APKs"""
    
    def __init__(self):
        """Inicializa o analisador de APK"""
        self.apk_path = None
        self.temp_dir = None
        self.manifest_data = {}
        
    def analyze(self, apk_path):
        """
        Analisa um arquivo APK e extrai suas informações
        
        Args:
            apk_path (str): Caminho para o arquivo APK
            
        Returns:
            dict: Dicionário com informações extraídas do APK
        """
        self.apk_path = apk_path
        self.temp_dir = tempfile.mkdtemp(prefix="apk_analysis_")
        
        try:
            # Verificar se o arquivo existe
            if not os.path.exists(apk_path):
                raise FileNotFoundError(f"Arquivo APK não encontrado: {apk_path}")
            
            # Extrair informações do APK
            info = self._extract_apk_info()
            
            logger.info("Análise do APK concluída com sucesso")
            return info
            
        except Exception as e:
            logger.error(f"Erro durante a análise do APK: {e}")
            raise
    
    def _extract_apk_info(self):
        """
        Extrai informações específicas do APK
        
        Returns:
            dict: Informações extraídas
        """
        try:
            # Abrir o APK como arquivo ZIP
            with zipfile.ZipFile(self.apk_path, 'r') as apk:
                # Extrair AndroidManifest.xml
                manifest_content = apk.read('AndroidManifest.xml')
                
                # Parsear o XML do manifesto
                root = ET.fromstring(manifest_content)
                
                # Extrair informações principais
                package_name = root.get('{http://schemas.android.com/apk/res/android}package')
                version_code = root.get('{http://schemas.android.com/apk/res/android}versionCode')
                version_name = root.get('{http://schemas.android.com/apk/res/android}versionName')
                
                # Encontrar o nome da aplicação (label)
                application = root.find('application')
                app_label = None
                if application is not None:
                    app_label = application.get('{http://schemas.android.com/apk/res/android}label')
                
                # Extrair permissões
                permissions = []
                for elem in root.iter():
                    if elem.tag.endswith('uses-permission'):
                        perm = elem.get('{http://schemas.android.com/apk/res/android}name')
                        if perm:
                            permissions.append(perm)
                
                # Criar dicionário com informações extraídas
                info = {
                    'package': package_name,
                    'version_code': version_code,
                    'version_name': version_name,
                    'app_label': app_label,
                    'permissions': permissions,
                    'file_size': os.path.getsize(self.apk_path),
                    'file_path': self.apk_path
                }
                
                return info
                
        except Exception as e:
            logger.error(f"Erro ao extrair informações do APK: {e}")
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
    analyzer = APKAnalyzer()
    
    # Exemplo de análise (substitua pelo caminho real do APK)
    # info = analyzer.analyze("exemplo.apk")
    # print(info)
    
    print("Módulo de análise de APK carregado com sucesso!")