"""
Barra de herramientas principal de la aplicación.
"""

from PySide6.QtWidgets import QToolBar, QWidget, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QIcon, QPixmap


class ToolBar(QWidget):
    """Barra de herramientas personalizada con estilo moderno."""
    
    # Señales para las acciones
    open_action = Signal()
    save_action = Signal()
    zoom_in_action = Signal()
    zoom_out_action = Signal()
    fit_to_window_action = Signal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        """Configura la interfaz de la barra de herramientas."""
        self.setFixedHeight(60)
        self.setStyleSheet("""
            QWidget {
                background-color: #3c3c3c;
                border-bottom: 1px solid #555555;
            }
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 5px;
                padding: 8px;
                margin: 2px;
                color: #ffffff;
                font-size: 12px;
                min-width: 60px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #4a4a4a;
            }
            QPushButton:pressed {
                background-color: #2a2a2a;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
                font-weight: bold;
                margin: 0 10px;
            }
        """)
        
        # Layout principal
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(5)
        
        # Logo/Título de la aplicación
        title_label = QLabel("📸 ESCOM-Editor")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-right: 20px;")
        layout.addWidget(title_label)
        
        # Grupo de archivos
        self._create_file_buttons(layout)
        
        # Separador
        self._add_separator(layout)
        
        # Grupo de edición
        self._create_edit_buttons(layout)
        
        # Separador
        self._add_separator(layout)
        
        # Grupo de vista
        self._create_view_buttons(layout)
        
        # Espaciador flexible
        layout.addStretch()
        
        # Información adicional
        info_label = QLabel("v1.0")
        info_label.setStyleSheet("color: #888888; font-size: 10px;")
        layout.addWidget(info_label)

    def _create_file_buttons(self, layout):
        """Crea los botones del grupo de archivos."""
        # Botón Abrir
        self.open_btn = QPushButton("📁\nAbrir")
        self.open_btn.setToolTip("Abrir imagen (Ctrl+O)")
        self.open_btn.clicked.connect(self.open_action.emit)
        layout.addWidget(self.open_btn)
        
        # Botón Guardar
        self.save_btn = QPushButton("💾\nGuardar")
        self.save_btn.setToolTip("Guardar imagen (Ctrl+S)")
        self.save_btn.clicked.connect(self.save_action.emit)
        self.save_btn.setEnabled(False)  # Inicialmente deshabilitado
        layout.addWidget(self.save_btn)

    def _create_edit_buttons(self, layout):
        """Crea los botones del grupo de edición."""
        # No se crean botones de deshacer ni rehacer

    def _create_view_buttons(self, layout):
        """Crea los botones del grupo de vista."""
        # Botón Zoom In
        self.zoom_in_btn = QPushButton("🔍+\nAcercar")
        self.zoom_in_btn.setToolTip("Acercar (Ctrl++)")
        self.zoom_in_btn.clicked.connect(self.zoom_in_action.emit)
        self.zoom_in_btn.setEnabled(False)  # Inicialmente deshabilitado
        layout.addWidget(self.zoom_in_btn)
        
        # Botón Zoom Out
        self.zoom_out_btn = QPushButton("🔍-\nAlejar")
        self.zoom_out_btn.setToolTip("Alejar (Ctrl+-)")
        self.zoom_out_btn.clicked.connect(self.zoom_out_action.emit)
        self.zoom_out_btn.setEnabled(False)  # Inicialmente deshabilitado
        layout.addWidget(self.zoom_out_btn)
        
        # Botón Ajustar a ventana
        self.fit_btn = QPushButton("⛶\nAjustar")
        self.fit_btn.setToolTip("Ajustar a ventana (Ctrl+0)")
        self.fit_btn.clicked.connect(self.fit_to_window_action.emit)
        self.fit_btn.setEnabled(False)  # Inicialmente deshabilitado
        layout.addWidget(self.fit_btn)

    def _add_separator(self, layout):
        """Añade un separador visual."""
        separator = QLabel("|")
        separator.setStyleSheet("""
            color: #666666;
            font-size: 20px;
            margin: 0 5px;
        """)
        layout.addWidget(separator)

    def enable_image_actions(self, enabled: bool):
        """Habilita o deshabilita las acciones que requieren una imagen."""
        self.save_btn.setEnabled(enabled)
        self.zoom_in_btn.setEnabled(enabled)
        self.zoom_out_btn.setEnabled(enabled)
        self.fit_btn.setEnabled(enabled)
