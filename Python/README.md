# ESCOM-Editor Python Version

ESCOM-Editor es una aplicación robusta, mantenible y escalable para la edición de imágenes desarrollada en Python 3.10, siguiendo los principios de Programación Orientada a Objetos (OOP). Aprovecha potentes bibliotecas de procesamiento de imágenes como Pillow y OpenCV, combinadas con una interfaz gráfica moderna y fácil de usar construida con PySide6.

---

## Características

- Carga y guarda imágenes en múltiples formatos (PNG, JPEG, BMP).
- Aplica varios filtros de imagen incluyendo escala de grises, desenfoque, nitidez, brillo, contraste y negativo.
- Zoom in, zoom out y ajuste de imagen a la ventana.
- Arquitectura modular y extensible que permite la fácil adición de nuevos filtros.
- Interfaz gráfica limpia y moderna inspirada en Picsart para una experiencia de usuario fluida.

---

## Versión recomendada de Python

Se recomienda ejecutar este proyecto con **Python 3.10** para una compatibilidad y rendimiento óptimos.

---

## Instalación y configuración

1. **Clona el repositorio:**

   ```bash
   git clone <repository_url>
   cd image_filters_app/Python
   ```

2. **Crea y activa un entorno virtual:**

   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Ejecución de la aplicación

Para iniciar la aplicación ESCOM-Editor, ejecuta:

```bash
python main.py
```

Esto lanzará la interfaz gráfica donde podrás abrir imágenes, aplicar filtros y guardar tus imágenes editadas.

---

## Estructura del proyecto

- `src/core/`: Clases principales para el manejo de imágenes.
- `src/filters/`: Clase base de filtros e implementaciones concretas de filtros.
- `src/gui/`: Componentes de la interfaz gráfica incluyendo ventana principal, barra de herramientas, panel de filtros y vista de imagen.
- `assets/`: Imágenes de ejemplo e íconos.
- `main.py`: Punto de entrada de la aplicación.
- `requirements.txt`: Dependencias de Python.
- `.gitignore`: Reglas para ignorar archivos en Git.

---

## Licencia

Este proyecto está licenciado bajo la Licencia BSD de 3 cláusulas.

Por favor, consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## Autor

Leonardo Zamudio López © 2025
