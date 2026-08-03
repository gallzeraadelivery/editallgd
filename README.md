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
- Ambiente de desenvolvimento Android (Android Studio)
- JDK 8 ou superior

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
├── gradlew.bat           # Script do Gradle para Windows
└── INSTALLATION_SCRIPT.sh   # Script de instalação
```

## Instalação e Compilação

### Para ambiente MacBook com Android Studio:

1. **Clonar o repositório:**
```bash
git clone https://github.com/gallzeraadelivery/editallgd.git
cd editallgd/android_fingerprint_spoof
```

2. **Compilar o projeto:**
   - Abra no Android Studio
   - Vá para Build → Make Project
   - O APK será gerado em: `app/build/outputs/apk/debug/app-debug.apk`

3. **Para compilação via linha de comando:**
```bash
./gradlew build
```

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