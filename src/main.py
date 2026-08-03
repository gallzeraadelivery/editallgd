#!/usr/bin/env python3
"""
Sistema de Spoofing de APK - Arquivo Principal
Este é o ponto de entrada principal da aplicação.
"""

import sys
import os
from pathlib import Path

# Adicionando o diretório src ao path para importações
sys.path.insert(0, str(Path(__file__).parent))

def main():
    """Função principal do sistema"""
    print("Sistema de Spoofing de APK")
    print("=" * 30)
    
    # Verificando se o ambiente está configurado corretamente
    try:
        from modules.analyzer import APKAnalyzer
        from modules.modifier import APKModifier
        from modules.signer import APKSigner
        from modules.packager import APKPackager
        
        print("Módulos carregados com sucesso!")
        print("Ambiente configurado corretamente.")
        
        # Exemplo de uso básico
        print("\nExemplo de uso:")
        print("- Analisar APK: python main.py analyze <arquivo.apk>")
        print("- Modificar APK: python main.py modify <arquivo.apk> --package com.example.newapp")
        print("- Assinar APK: python main.py sign <arquivo.apk>")
        print("- Empacotar APK: python main.py package <arquivo.apk>")
        
    except ImportError as e:
        print(f"Erro ao carregar módulos: {e}")
        print("Verifique se todos os componentes estão instalados corretamente.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())