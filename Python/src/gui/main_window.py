"""
Ventana principal de la aplicación de edición de imágenes.
"""

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QScrollArea,
    QSplitter, QFrame
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QImage, QPixmap
from pathlib import Path

from src.core import Image
from src.gui.image_view import ImageView
from src.gui.filter_panel import FilterPanel
from src.gui.toolbar import ToolBar


class MainWindow(QMainWindow):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ESCOM-Editor")
        self.setMinimumSize(1200, 800)
        
        # Atributos principales
        self._current_image = Image()
        
        # Configurar la interfaz
        self._setup_ui()
        self._setup_connections()
        
        # Configurar el estilo
        self._setup_style()

    def _setup_ui(self):
        """Configura los elementos de la interfaz de usuario."""
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Barra de herramientas
        self.toolbar = ToolBar()
        main_layout.addWidget(self.toolbar)
        
        # Contenedor principal con splitter
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        
        # Panel de filtros (izquierda)
        self.filter_panel = FilterPanel()
        splitter.addWidget(self.filter_panel)
        
        # Área de visualización de imagen (centro)
        self.image_view = ImageView()
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.image_view)
        scroll_area.setWidgetResizable(True)
        splitter.addWidget(scroll_area)
        
        # Establecer proporciones del splitter
        splitter.setStretchFactor(0, 1)  # Panel de filtros
        splitter.setStretchFactor(1, 4)  # Área de imagen
        
        # Barra de estado
        self.statusBar().showMessage("Listo")
        
        # Agregar copyright en la esquina inferior derecha
        copyright_label = QLabel("© Leonardo Zamudio López 2025")
        copyright_label.setStyleSheet("color: #888888; font-size: 10px; margin-right: 10px;")
        self.statusBar().addPermanentWidget(copyright_label)

    def _setup_connections(self):
        """Configura las conexiones de señales y slots."""
        # Conexiones de la barra de herramientas
        self.toolbar.open_action.connect(self._on_open_image)
        self.toolbar.save_action.connect(self._on_save_image)
        self.toolbar.zoom_in_action.connect(self._on_zoom_in)
        self.toolbar.zoom_out_action.connect(self._on_zoom_out)
        self.toolbar.fit_to_window_action.connect(self._on_fit_to_window)
        
        # Conexiones del panel de filtros
        self.filter_panel.filter_applied.connect(self._on_filter_applied)

    def _setup_style(self):
        """Configura el estilo visual de la ventana."""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
            }
            QScrollArea {
                background-color: #1e1e1e;
                border: none;
            }
            QSplitter::handle {
                background-color: #3c3c3c;
            }
            QStatusBar {
                background-color: #2b2b2b;
                color: #ffffff;
            }
        """)

    def _on_open_image(self):
        """Maneja el evento de abrir una imagen."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir Imagen",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif);;Todos los archivos (*.*)"
        )
        
        if file_path:
            if self._current_image.load(file_path):
                self.image_view.set_image(self._current_image)
                self.statusBar().showMessage(f"Imagen cargada: {Path(file_path).name}")
                # Habilitar botones que requieren imagen
                self.toolbar.enable_image_actions(True)
                # Actualizar estado de botones deshacer/rehacer
                self._update_undo_redo_state()
            else:
                self.statusBar().showMessage("Error al cargar la imagen")

    def _on_save_image(self):
        """Maneja el evento de guardar una imagen."""
        if not self._current_image.get_pil_image():
            self.statusBar().showMessage("No hay imagen para guardar")
            return
            
        file_path, selected_filter = QFileDialog.getSaveFileName(
            self,
            "Guardar Imagen",
            "",
            "PNG (*.png);;JPEG (*.jpg);;BMP (*.bmp)"
        )
        
        if file_path:
            # Asegurar que el archivo tenga una extensión válida
            if not any(file_path.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.bmp']):
                # Obtener la extensión del filtro seleccionado
                if "PNG" in selected_filter:
                    file_path += '.png'
                elif "JPEG" in selected_filter:
                    file_path += '.jpg'
                elif "BMP" in selected_filter:
                    file_path += '.bmp'
                else:
                    file_path += '.png'  # Por defecto usar PNG
            
            if self._current_image.save(file_path):
                self.statusBar().showMessage(f"Imagen guardada como: {Path(file_path).name}")
            else:
                self.statusBar().showMessage("Error al guardar la imagen")

    def _on_zoom_in(self):
        """Maneja el evento de acercar zoom."""
        self.image_view.zoom_in()
        self.statusBar().showMessage("Zoom aumentado")

    def _on_zoom_out(self):
        """Maneja el evento de alejar zoom."""
        self.image_view.zoom_out()
        self.statusBar().showMessage("Zoom disminuido")

    def _on_fit_to_window(self):
        """Maneja el evento de ajustar imagen a ventana."""
        self.image_view.fit_to_window()
        self.statusBar().showMessage("Imagen ajustada a ventana")

    def _on_filter_applied(self, filter_obj):
        """
        Maneja el evento de aplicación de un filtro.
        
        Args:
            filter_obj: Instancia del filtro a aplicar.
        """
        if self._current_image.get_pil_image():
            # Aplicar el filtro (esto automáticamente manejará el historial)
            filter_obj.apply(self._current_image)
            self.image_view.update_image()
            self.statusBar().showMessage(f"Filtro aplicado: {filter_obj.name}")
        else:
            self.statusBar().showMessage("No hay imagen para aplicar el filtro")
