# Configuración del Entorno de Desarrollo para ESCOM-Editor Java

## Requisitos Previos
- JDK 17 o superior instalado y configurado en el PATH.
- Visual Studio Code instalado.
- Extensión "Java Extension Pack" instalada en VSCode.
- JavaFX SDK 17 o superior descargado desde https://openjfx.io/ y descomprimido.

## Configuración en VSCode

1. Abrir VSCode y abrir la carpeta del proyecto Java.

2. Configurar el archivo `launch.json` para incluir los módulos de JavaFX:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "java",
            "name": "Launch ESCOM-Editor",
            "request": "launch",
            "mainClass": "com.escomeditor.gui.MainWindow",
            "vmArgs": "--module-path /ruta/a/javafx-sdk-17/lib --add-modules javafx.controls,javafx.fxml,javafx.swing"
        }
    ]
}
```

Reemplazar `/ruta/a/javafx-sdk-17/lib` con la ruta real donde se descomprimió JavaFX SDK.

3. Configurar el classpath y module-path en `settings.json` si es necesario para la compilación.

## Compilación y Ejecución

- Para compilar manualmente:

```bash
javac --module-path /ruta/a/javafx-sdk-17/lib --add-modules javafx.controls,javafx.fxml,javafx.swing -d out src/com/escomeditor/core/*.java src/com/escomeditor/filters/*.java src/com/escomeditor/gui/*.java
```

- Para ejecutar:

```bash
java --module-path /ruta/a/javafx-sdk-17/lib --add-modules javafx.controls,javafx.fxml,javafx.swing -cp out com.escomeditor.gui.MainWindow
```

## Notas

- Se recomienda usar Maven o Gradle para gestionar dependencias y compilación en proyectos más grandes.
- Asegúrese de que la versión de Java y JavaFX sean compatibles.
- Para más información sobre JavaFX en VSCode, consulte la documentación oficial de OpenJFX y la extensión de Java para VSCode.
