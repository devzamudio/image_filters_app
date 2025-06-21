# Repositorio Multiversión de ESCOM-Editor

Este repositorio contiene tres versiones de la aplicación de edición de imágenes ESCOM-Editor:

* **Versión en Python**
* **Versión en Java**
* **Versión en C++**

Cada versión ofrece funciones básicas de edición de imágenes como abrir, guardar, redimensionar, recortar, rotar y aplicar filtros como escala de grises, brillo, contraste, desenfoque, nitidez y negativo.

---

## Funcionalidades Comunes

* Cargar y guardar imágenes en formatos comunes (PNG, JPEG, BMP, GIF).
* Funcionalidad de deshacer/rehacer.
* Filtros de imagen implementados como clases modulares.
* Interfaz gráfica con barra de herramientas, panel de filtros y vista de imagen.
* Compatibilidad multiplataforma (Windows, macOS, Linux).

---

## Versión en Python

### Detalles Técnicos

* Lenguaje: Python 3.x
* Procesamiento de imágenes: Pillow (PIL)
* Framework de GUI: Qt para Python (PySide6)
* Estructura: `Python/src/` contiene los módulos de núcleo, filtros e interfaz gráfica.

### Instalación y Ejecución

#### Requisitos Previos

* Python 3.7 o superior **(recomendado Python 3.10)**
* Administrador de paquetes `pip`

#### Instalar Dependencias

```bash
pip install -r Python/requirements.txt
```

#### Ejecutar Aplicación

```bash
python Python/main.py
```

---

## Versión en Java

### Detalles Técnicos

* Lenguaje: Java 11 o superior
* Procesamiento de imágenes: Java 2D API
* Framework de GUI: Swing y JavaFX
* Estructura: `Java/src/com/escomeditor/` contiene los paquetes de núcleo, filtros e interfaz gráfica.

### Compilación y Ejecución

#### Requisitos Previos

* JDK 11 o superior
* Maven o Gradle (dependiendo de la configuración del proyecto)

#### Compilar

Usa tu herramienta de compilación preferida para compilar el proyecto.

#### Ejecutar

Ejecuta la clase principal `com.escomeditor.gui.MainWindow`.

---

## Versión en C++

### Detalles Técnicos

* Lenguaje: C++17
* Procesamiento de imágenes: OpenCV 4.x
* Framework de GUI: Qt 5.x o 6.x (Qt Widgets)
* Estructura: `C++/src/` contiene las carpetas de núcleo, filtros e interfaz gráfica.

### Compilación y Ejecución

#### Requisitos Previos

* Compilador compatible con C++17 (g++, clang, MSVC)
* CMake 3.15 o superior
* OpenCV 4.x
* Qt 5.x o 6.x (módulo Qt Widgets)

#### Instalación de Dependencias

##### Debian/Ubuntu y derivados

```bash
sudo apt update
sudo apt install build-essential cmake qtbase5-dev libopencv-dev
```

##### Fedora y derivados

```bash
sudo dnf install @development-tools cmake qt5-qtbase-devel opencv-devel
```

##### Arch Linux y derivados

```bash
sudo pacman -S base-devel cmake qt5-base opencv
```

##### openSUSE y derivados

```bash
sudo zypper install -t pattern devel_C_C++ cmake libqt5-qtbase-devel opencv-devel
```

##### Windows

* Instala [Qt](https://www.qt.io/download)
* Instala [OpenCV](https://opencv.org/releases/)
* Usa Visual Studio con soporte para CMake

##### macOS

* Instala Qt y OpenCV con Homebrew:

```bash
brew install qt opencv
```

#### Pasos de Compilación

```bash
mkdir build
cd build
cmake ..
make
```

#### Ejecutar Aplicación

```bash
./escomeditor
```

---

## Pruebas

Para todas las versiones, prueba lo siguiente:

* Abrir y mostrar imágenes.
* Aplicar todos los filtros y verificar los cambios visuales.
* Guardar imágenes editadas.
* Funcionalidades de zoom y ajuste a ventana.

---

## Notas

* Cada versión replica la funcionalidad central usando bibliotecas adecuadas al lenguaje.
* La versión en C++ está optimizada para rendimiento utilizando OpenCV y Qt.
* La versión en Java utiliza APIs nativas de Java para procesamiento de imágenes e interfaz gráfica.
* La versión en Python ofrece desarrollo rápido y facilidad de uso.

---

Para instrucciones más detalladas, por favor consulta los archivos README dentro de la carpeta de cada versión.

---
