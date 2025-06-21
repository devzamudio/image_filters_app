# ESCOM-Editor Java Version

## Descripción
ESCOM-Editor es una aplicación de edición básica de imágenes que permite abrir, redimensionar, recortar, rotar y aplicar filtros simples como escala de grises, brillo y contraste. Esta es la versión portada a Java usando JavaFX para la interfaz gráfica y BufferedImage para el manejo de imágenes.

## Requisitos
- Java 17 o superior
- JavaFX 17 o superior
- Maven (opcional, para gestión de dependencias y compilación)

## Librerías utilizadas
- JavaFX: Para la interfaz gráfica moderna y responsiva.
- BufferedImage (Java estándar): Para la representación y manipulación de imágenes.
- TwelveMonkeys ImageIO (opcional): Para soporte extendido de formatos de imagen y filtros avanzados.
- ImageJ (opcional): Para filtros avanzados si se requiere.

## Instalación y configuración

### Configurar JavaFX en VSCode
1. Instalar el JDK 17 o superior.
2. Instalar la extensión "Java Extension Pack" en VSCode.
3. Descargar JavaFX SDK desde [https://openjfx.io/](https://openjfx.io/) y descomprimirlo.
4. Configurar las variables de entorno o añadir las librerías JavaFX al classpath y module-path en la configuración de VSCode.
5. En el archivo `launch.json` de VSCode, añadir los argumentos VM para JavaFX:
```
--module-path /ruta/a/javafx-sdk-17/lib --add-modules javafx.controls,javafx.fxml
```

### Compilar y ejecutar
- Usando Maven (si se configura):
```
mvn clean compile exec:java -Dexec.mainClass="com.escomeditor.gui.MainWindow"
```
- Manualmente:
```
javac -d out -cp /ruta/a/javafx-sdk-17/lib/* src/com/escomeditor/**/*.java
java --module-path /ruta/a/javafx-sdk-17/lib --add-modules javafx.controls,javafx.fxml -cp out com.escomeditor.gui.MainWindow
```

## Uso
- Abrir imágenes desde el menú o botón "Abrir".
- Aplicar filtros desde el panel lateral.
- Guardar imágenes editadas.
- Usar botones de zoom y ajuste para visualizar la imagen.

## Pruebas
Para probar que el porteo funciona correctamente:
- Abrir una imagen de prueba.
- Aplicar filtros básicos (escala de grises, brillo, contraste).
- Guardar la imagen y verificar que se haya guardado correctamente.
- Usar zoom y ajuste para verificar la visualización.

## Licencia
Este proyecto está bajo la licencia BSD de tres cláusulas. Consulte el archivo LICENSE para más detalles.
