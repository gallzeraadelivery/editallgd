#!/usr/bin/env python3
"""
Arquivo de Configuração do Sistema
Contém as configurações padrão e constantes do sistema.
"""

import os
from pathlib import Path

class Config:
    """Classe para gerenciamento de configurações"""
    
    # Versão do sistema
    VERSION = "1.0.0"
    
    # Diretórios padrão
    DEFAULT_TEMP_DIR = os.path.join(os.path.expanduser("~"), ".apk_spoof", "temp")
    DEFAULT_OUTPUT_DIR = os.path.join(os.path.expanduser("~"), ".apk_spoof", "output")
    
    # Configurações de segurança
    ALLOWED_FILE_TYPES = ['.apk']
    MAX_FILE_SIZE = 1024 * 1024 * 100  # 100MB
    
    # Configurações de logging
    LOG_LEVEL = "INFO"
    LOG_FILE = os.path.join(DEFAULT_TEMP_DIR, "apk_spoof.log")
    
    # Configurações de ferramentas externas
    APKTOOL_PATH = "apktool"  # Pode ser substituído por caminho completo
    JARSIGNER_PATH = "jarsigner"  # Pode ser substituído por caminho completo
    
    @classmethod
    def get_config(cls):
        """Retorna um dicionário com todas as configurações"""
        return {
            'version': cls.VERSION,
            'temp_dir': cls.DEFAULT_TEMP_DIR,
            'output_dir': cls.DEFAULT_OUTPUT_DIR,
            'allowed_file_types': cls.ALLOWED_FILE_TYPES,
            'max_file_size': cls.MAX_FILE_SIZE,
            'log_level': cls.LOG_LEVEL,
            'log_file': cls.LOG_FILE,
            'apktool_path': cls.APKTOOL_PATH,
            'jarsigner_path': cls.JARSIGNER_PATH
        }
    
    @classmethod
    def create_directories(cls):
        """Cria diretórios necessários para o sistema"""
        dirs_to_create = [
            cls.DEFAULT_TEMP_DIR,
            cls.DEFAULT_OUTPUT_DIR
        ]
        
        for directory in dirs_to_create:
            try:
                os.makedirs(directory, exist_ok=True)
            except Exception as e:
                print(f"Erro ao criar diretório {directory}: {e}")

# Inicializar diretórios
Config.create_directories()

# Exemplo de uso
if __name__ == "__main__":
    config = Config.get_config()
    print("Configurações do Sistema:")
    for key, value in config.items():
        print(f"  {key}: {value}")