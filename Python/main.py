"""
Punto de entrada principal de la aplicación de edición de imágenes.
"""

import sys
from PySide6.QtWidgets import QApplication
from src.gui.main_window import MainWindow


def main():
    """Función principal que inicializa la aplicación."""
    app = QApplication(sys.argv)
    app.setApplicationName("ESCOM-Editor")
    app.setApplicationVersion("1.0.0")
    
    # Configurar estilo de la aplicación
    app.setStyleSheet("""
        QMainWindow {
            background-color: #2b2b2b;
        }
    """)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
