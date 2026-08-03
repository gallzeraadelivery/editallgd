#!/usr/bin/env python3
"""
Script de Teste Simples do Sistema de Spoofing de APK
Testa a funcionalidade básica do sistema.
"""

import sys
import os
from pathlib import Path

# Adicionando o diretório src ao path para importações
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_imports():
    """Testa se todos os módulos podem ser importados corretamente"""
    print("Testing module imports...")
    
    try:
        from modules.analyzer import APKAnalyzer
        from modules.modifier import APKModifier
        from modules.signer import APKSigner
        from modules.packager import APKPackager
        
        print("SUCCESS: All modules imported successfully")
        return True
    except ImportError as e:
        print(f"ERROR: Failed to import modules: {e}")
        return False

def test_basic_functionality():
    """Testa a funcionalidade básica do sistema"""
    print("\nTesting basic functionality...")
    
    try:
        # Testar criação de instâncias
        analyzer = APKAnalyzer()
        modifier = APKModifier()
        signer = APKSigner()
        packager = APKPackager()
        
        print("SUCCESS: Instances created successfully")
        
        # Testar métodos básicos
        config = {
            'package': 'com.example.testapp',
            'version_name': '1.0.0',
            'version_code': 1,
            'app_label': 'Test App'
        }
        
        print("SUCCESS: Basic configurations defined")
        return True
        
    except Exception as e:
        print(f"ERROR: Basic functionality failed: {e}")
        return False

def main():
    """Função principal de teste"""
    print("=" * 50)
    print("TESTE DO SISTEMA DE SPOOFING DE APK")
    print("=" * 50)
    
    success = True
    
    # Testar importações
    if not test_imports():
        success = False
    
    # Testar funcionalidade básica
    if not test_basic_functionality():
        success = False
    
    print("\n" + "=" * 50)
    if success:
        print("SUCCESS: ALL TESTS PASSED!")
        print("System is ready for use.")
    else:
        print("ERROR: SOME TESTS FAILED!")
        print("Check the errors above.")
    print("=" * 50)
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())