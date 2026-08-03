# Fingerprint Spoofing App for Android

## Visão Geral

Este é um aplicativo Android que permite modificar os "fingerprints" do dispositivo para fins de spoofing ou bypass de segurança. O aplicativo requer acesso root para funcionar corretamente.

## Funcionalidades

- Spoof de propriedades do sistema (build info)
- Modificação de informações de hardware
- Bypass de verificação de identidade do dispositivo
- Interface gráfica intuitiva

## Requisitos

- Dispositivo Android com root
- Android 5.0 (API level 21) ou superior
- Permissões especiais para acesso ao sistema

## Estrutura do Projeto

```
android_fingerprint_spoof/
├── app/
│   ├── build.gradle          # Configuração do build
│   └── src/
│       └── main/
│           ├── java/com/example/fingerprintspoof/
│           │   └── MainActivity.java    # Classe principal
│           ├── res/
│           │   ├── layout/
│           │   │   └── activity_main.xml  # Layout da interface
│           │   ├── values/
│           │   │   ├── strings.xml        # Strings da aplicação
│           │   │   └── styles.xml       # Estilos
│           │   └── mipmap/
│           └── AndroidManifest.xml  # Manifesto do aplicativo
├── build.gradle              # Configuração do projeto
├── gradle.properties         # Propriedades do Gradle
└── gradlew.bat           # Script do Gradle para Windows
```

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
```

2. Abra o projeto no Android Studio

3. Compile e instale no dispositivo rootado

## Uso

1. Execute o aplicativo no dispositivo rootado
2. Clique em "Spoof Fingerprint"
3. O aplicativo modificará as propriedades do sistema

## Aviso Importante

⚠️ **Este aplicativo pode causar instabilidade no sistema**
- Pode fazer com que apps detectem o spoofing
- Pode causar falhas em sistemas de segurança
- Use com cuidado e em ambientes de testes

## Permissões Necessárias

- `ACCESS_SUPERUSER` - Para acesso root
- `WRITE_SECURE_SETTINGS` - Para modificação de propriedades do sistema
- `READ_PHONE_STATE` - Para leitura de informações do dispositivo

## Desenvolvimento

O aplicativo foi desenvolvido usando:
- Java 8
- Android SDK 33
- Android Studio

## Compilação

Para compilar o projeto, siga as instruções em: [COMPILATION_INSTRUCTIONS.md](COMPILATION_INSTRUCTIONS.md)

## Licença

Este projeto é apenas para fins educacionais e de teste.