"""
Widget para la visualización de imágenes en la interfaz gráfica.
"""

from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QImage, QPixmap, QPainter
from typing import Optional

from src.core import Image


class ImageView(QLabel):
    """
    Widget personalizado para mostrar imágenes con capacidades de zoom y ajuste.
    """

    def __init__(self):
        super().__init__()
        self._image: Optional[Image] = None
        self._scale_factor = 1.0
        self._fit_to_window = True
        
        self._setup_ui()

    def _setup_ui(self):
        """Configura la interfaz del widget."""
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(400, 300)
        self.setStyleSheet("""
            QLabel {
                background-color: #1e1e1e;
                border: 2px dashed #555555;
                color: #888888;
                font-size: 16px;
            }
        """)
        self.setText("Arrastra una imagen aquí o usa Archivo > Abrir")
        
        # Habilitar drag and drop
        self.setAcceptDrops(True)

    def set_image(self, image: Image):
        """
        Establece la imagen a mostrar.
        
        Args:
            image: Instancia de Image a mostrar.
        """
        self._image = image
        self.update_image()

    def update_image(self):
        """Actualiza la visualización de la imagen."""
        if not self._image or not self._image.get_pil_image():
            return
            
        # Convertir PIL Image a QImage
        pil_image = self._image.get_pil_image()
        
        # Convertir PIL a QImage directamente
        w, h = pil_image.size
        qimage = QImage(pil_image.tobytes(), w, h, QImage.Format_RGB888)
        
        # Crear QPixmap desde QImage
        pixmap = QPixmap.fromImage(qimage)
        
        # Aplicar escala si es necesario
        if self._fit_to_window:
            pixmap = self._scale_pixmap_to_fit(pixmap)
        else:
            pixmap = pixmap.scaled(
                pixmap.size() * self._scale_factor,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        
        self.setPixmap(pixmap)

    def _scale_pixmap_to_fit(self, pixmap: QPixmap) -> QPixmap:
        """
        Escala el pixmap para que se ajuste al widget manteniendo la proporción.
        
        Args:
            pixmap: QPixmap a escalar.
            
        Returns:
            QPixmap escalado.
        """
        widget_size = self.size()
        return pixmap.scaled(
            widget_size,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

    def zoom_in(self):
        """Aumenta el zoom de la imagen."""
        if self._image:
            self._fit_to_window = False
            self._scale_factor *= 1.25
            self.update_image()

    def zoom_out(self):
        """Disminuye el zoom de la imagen."""
        if self._image:
            self._fit_to_window = False
            self._scale_factor /= 1.25
            self.update_image()

    def fit_to_window(self):
        """Ajusta la imagen al tamaño de la ventana."""
        if self._image:
            self._fit_to_window = True
            self._scale_factor = 1.0
            self.update_image()

    def actual_size(self):
        """Muestra la imagen en su tamaño real."""
        if self._image:
            self._fit_to_window = False
            self._scale_factor = 1.0
            self.update_image()

    def dragEnterEvent(self, event):
        """Maneja el evento de arrastrar archivos sobre el widget."""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        """Maneja el evento de soltar archivos en el widget."""
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            # Aquí se podría emitir una señal para notificar a la ventana principal
            # Por ahora, simplemente aceptamos el evento
            event.acceptProposedAction()

    def resizeEvent(self, event):
        """Maneja el redimensionamiento del widget."""
        super().resizeEvent(event)
        if self._fit_to_window and self._image:
            self.update_image()
