# Sistema de Spoofing de APK

## Visão Geral

Este projeto é uma implementação completa de um sistema de spoofing de APK (Android Package) que permite modificar metadados e identidade de aplicativos Android. O sistema foi desenvolvido com foco em usabilidade, segurança e eficiência.

## Funcionalidades

- **Análise de APK**: Leitura e extração de informações de arquivos APK
- **Modificação de Metadados**: Alteração de package names, nomes de aplicativos, versões
- **Manipulação de Recursos**: Substituição de ícones e outros recursos
- **Assinatura Digital**: Re-assinatura de APKs modificados com chaves válidas
- **Empacotamento Final**: Geração de APK final funcional

## Estrutura do Projeto

```
apk_spoof/
├── src/
│   ├── main.py                 # Ponto de entrada principal
│   ├── modules/                # Módulos principais
│   │   ├── analyzer.py         # Análise de APKs
│   │   ├── modifier.py           # Modificação de APKs
│   │   ├── signer.py             # Assinatura de APKs
│   │   └── packager.py         # Empacotamento de APKs
│   └── utils/                  # Utilitários
│       └── config.py           # Configurações do sistema
├── test_system_simple.py     # Script de teste
└── README.md                   # Este arquivo
```

## Requisitos

- Python 3.7+
- Apktool (para manipulação de APKs)
- JDK 8+ (para assinatura)

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd apk_spoof
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Certifique-se de que Apktool e JDK estão instalados e disponíveis no PATH.

## Uso

### Interface de Linha de Comando

```bash
# Analisar um APK
python src/main.py analyze <arquivo.apk>

# Modificar um APK
python src/main.py modify <arquivo.apk> --package com.example.newapp

# Assinar um APK
python src/main.py sign <arquivo.apk>

# Empacotar um APK
python src/main.py package <arquivo.apk>
```

### Interface Gráfica (em desenvolvimento)

O sistema também oferece uma interface gráfica para usuários avançados.

## Arquitetura

O sistema foi projetado com uma arquitetura modular:

1. **Módulo de Análise**: Parser de APKs e extração de metadados
2. **Módulo de Modificação**: Edição de manifestos e recursos
3. **Módulo de Assinatura**: Re-assinatura digital de APKs
4. **Módulo de Empacotamento**: Reconstrução final do APK

## Segurança

- Todos os processos são executados em ambiente isolado
- Validação rigorosa de entradas para evitar vulnerabilidades
- Proteção contra manipulação de arquivos maliciosos

## Desenvolvimento

Para contribuir com o projeto, siga estas etapas:

1. Fork o repositório
2. Crie uma branch para sua feature: `git checkout -b feature/nova-funcionalidade`
3. Faça commit das suas alterações: `git commit -am 'Adiciona nova funcionalidade'`
4. Faça push para a branch: `git push origin feature/nova-funcionalidade`
5. Crie um Pull Request

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato com o desenvolvedor.