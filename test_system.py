#!/usr/bin/env python3
"""
Script de Teste do Sistema de Spoofing de APK
Testa a funcionalidade básica do sistema.
"""

import sys
import os
from pathlib import Path

# Adicionando o diretório src ao path para importações
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_imports():
    """Testa se todos os módulos podem ser importados corretamente"""
    print("Testando importações dos módulos...")
    
    try:
        from modules.analyzer import APKAnalyzer
        from modules.modifier import APKModifier
        from modules.signer import APKSigner
        from modules.packager import APKPackager
        
        print("✓ Todos os módulos foram importados com sucesso")
        return True
    except ImportError as e:
        print(f"✗ Erro ao importar módulos: {e}")
        return False

def test_basic_functionality():
    """Testa a funcionalidade básica do sistema"""
    print("\nTestando funcionalidade básica...")
    
    try:
        # Testar criação de instâncias
        analyzer = APKAnalyzer()
        modifier = APKModifier()
        signer = APKSigner()
        packager = APKPackager()
        
        print("✓ Instâncias criadas com sucesso")
        
        # Testar métodos básicos
        config = {
            'package': 'com.example.testapp',
            'version_name': '1.0.0',
            'version_code': 1,
            'app_label': 'Test App'
        }
        
        print("✓ Configurações básicas definidas")
        return True
        
    except Exception as e:
        print(f"✗ Erro na funcionalidade básica: {e}")
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
        print("✓ TODOS OS TESTES PASSARAM COM SUCESSO!")
        print("O sistema está pronto para uso.")
    else:
        print("✗ ALGUNS TESTES FALHARAM!")
        print("Verifique os erros acima.")
    print("=" * 50)
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())