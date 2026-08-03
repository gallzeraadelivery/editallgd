# Instruções de Compilação

## Requisitos

- Android Studio (ou ferramentas de linha de comando)
- JDK 8 ou superior
- SDK do Android
- Dispositivo Android com root (para testes)

## Passos para Compilação

### Método 1: Usando Android Studio

1. **Abrir o projeto**
   - Abra o Android Studio
   - Selecione "Open an existing Android Studio project"
   - Navegue até o diretório `android_fingerprint_spoof`

2. **Sincronizar o projeto**
   - O Android Studio irá sincronizar automaticamente
   - Aguarde o download das dependências

3. **Compilar o projeto**
   - Vá para Build → Make Project (ou pressione Ctrl+F9)
   - O APK será gerado em: `app/build/outputs/apk/debug/app-debug.apk`

4. **Gerar versão release**
   - Vá para Build → Generate Signed Bundle / APK
   - Siga as instruções para criar um APK assinado

### Método 2: Usando linha de comando

```bash
cd android_fingerprint_spoof
./gradlew build
```

O APK será gerado em:
- Debug: `app/build/outputs/apk/debug/app-debug.apk`
- Release: `app/build/outputs/apk/release/app-release.apk`

## Instalação no dispositivo

1. Conecte seu dispositivo Android com root
2. Ative o modo desenvolvedor e USB debugging
3. Execute:
```bash
adb install app-debug.apk
```

## Aviso Importante

⚠️ Este aplicativo requer acesso root para funcionar corretamente.
- Pode causar instabilidade no sistema
- Pode ser detectado por apps de segurança
- Use apenas em ambientes de testes