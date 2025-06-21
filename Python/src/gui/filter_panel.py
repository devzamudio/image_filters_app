"""
Panel de filtros para la interfaz gráfica.
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLabel, QSlider, QGroupBox, QScrollArea
)
from PySide6.QtCore import Qt, Signal
from typing import Dict, Any

from src.filters import (
    GrayscaleFilter, BrightnessFilter, BlurFilter,
    SharpenFilter, ContrastFilter, NegativeFilter
)


class FilterPanel(QWidget):
    """Panel que contiene todos los filtros disponibles."""
    
    # Señal emitida cuando se aplica un filtro
    filter_applied = Signal(object)

    def __init__(self):
        super().__init__()
        self._filters = {}
        self._setup_ui()
        self._create_filters()

    def _setup_ui(self):
        """Configura la interfaz del panel."""
        self.setFixedWidth(300)
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #555555;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
            QPushButton {
                background-color: #4a4a4a;
                border: 1px solid #666666;
                border-radius: 3px;
                padding: 5px;
                min-height: 25px;
            }
            QPushButton:hover {
                background-color: #5a5a5a;
            }
            QPushButton:pressed {
                background-color: #3a3a3a;
            }
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 8px;
                background: #3a3a3a;
                margin: 2px 0;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #ffffff;
                border: 1px solid #5c5c5c;
                width: 18px;
                margin: -2px 0;
                border-radius: 9px;
            }
        """)
        
        # Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Título del panel
        title_label = QLabel("Filtros")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        main_layout.addWidget(title_label)
        
        # Área de scroll para los filtros
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # Widget contenedor de filtros
        self.filters_widget = QWidget()
        self.filters_layout = QVBoxLayout(self.filters_widget)
        self.filters_layout.setSpacing(10)
        
        scroll_area.setWidget(self.filters_widget)
        main_layout.addWidget(scroll_area)
        
        # Espaciador al final
        main_layout.addStretch()

    def _create_filters(self):
        """Crea los widgets para cada filtro."""
        # Filtros básicos sin parámetros
        basic_filters = [
            ("Escala de Grises", GrayscaleFilter()),
            ("Negativo", NegativeFilter())
        ]
        
        basic_group = QGroupBox("Filtros Básicos")
        basic_layout = QVBoxLayout(basic_group)
        
        for name, filter_obj in basic_filters:
            btn = QPushButton(name)
            btn.clicked.connect(lambda checked=False, f=filter_obj: self.filter_applied.emit(f))
            basic_layout.addWidget(btn)
            self._filters[name] = filter_obj
        
        self.filters_layout.addWidget(basic_group)
        
        # Filtros con parámetros
        self._create_brightness_filter()
        self._create_contrast_filter()
        self._create_blur_filter()
        self._create_sharpen_filter()

    def _create_brightness_filter(self):
        """Crea el widget para el filtro de brillo."""
        group = QGroupBox("Brillo")
        layout = QVBoxLayout(group)
        
        # Slider para el brillo
        brightness_slider = QSlider(Qt.Horizontal)
        brightness_slider.setRange(0, 200)  # 0% a 200%
        brightness_slider.setValue(100)  # 100% es normal
        
        # Label para mostrar el valor
        value_label = QLabel("100%")
        value_label.setAlignment(Qt.AlignCenter)
        
        # Botón para aplicar
        apply_btn = QPushButton("Aplicar Brillo")
        
        # Filtro
        brightness_filter = BrightnessFilter()
        self._filters["Brillo"] = brightness_filter
        
        def update_brightness():
            value = brightness_slider.value()
            value_label.setText(f"{value}%")
            brightness_filter.set_parameters(factor=value / 100.0)
        
        def apply_brightness():
            self.filter_applied.emit(brightness_filter)
        
        brightness_slider.valueChanged.connect(update_brightness)
        apply_btn.clicked.connect(apply_brightness)
        
        layout.addWidget(QLabel("Ajustar:"))
        layout.addWidget(brightness_slider)
        layout.addWidget(value_label)
        layout.addWidget(apply_btn)
        
        self.filters_layout.addWidget(group)

    def _create_contrast_filter(self):
        """Crea el widget para el filtro de contraste."""
        group = QGroupBox("Contraste")
        layout = QVBoxLayout(group)
        
        contrast_slider = QSlider(Qt.Horizontal)
        contrast_slider.setRange(0, 200)
        contrast_slider.setValue(100)
        
        value_label = QLabel("100%")
        value_label.setAlignment(Qt.AlignCenter)
        
        apply_btn = QPushButton("Aplicar Contraste")
        
        contrast_filter = ContrastFilter()
        self._filters["Contraste"] = contrast_filter
        
        def update_contrast():
            value = contrast_slider.value()
            value_label.setText(f"{value}%")
            contrast_filter.set_parameters(factor=value / 100.0)
        
        def apply_contrast():
            self.filter_applied.emit(contrast_filter)
        
        contrast_slider.valueChanged.connect(update_contrast)
        apply_btn.clicked.connect(apply_contrast)
        
        layout.addWidget(QLabel("Ajustar:"))
        layout.addWidget(contrast_slider)
        layout.addWidget(value_label)
        layout.addWidget(apply_btn)
        
        self.filters_layout.addWidget(group)

    def _create_blur_filter(self):
        """Crea el widget para el filtro de desenfoque."""
        group = QGroupBox("Desenfoque")
        layout = QVBoxLayout(group)
        
        blur_slider = QSlider(Qt.Horizontal)
        blur_slider.setRange(1, 25)  # Tamaño del kernel
        blur_slider.setValue(5)
        
        value_label = QLabel("5")
        value_label.setAlignment(Qt.AlignCenter)
        
        apply_btn = QPushButton("Aplicar Desenfoque")
        
        blur_filter = BlurFilter()
        self._filters["Desenfoque"] = blur_filter
        
        def update_blur():
            value = blur_slider.value()
            # Asegurar que sea impar
            if value % 2 == 0:
                value += 1
            value_label.setText(str(value))
            blur_filter.set_parameters(kernel_size=value)
        
        def apply_blur():
            self.filter_applied.emit(blur_filter)
        
        blur_slider.valueChanged.connect(update_blur)
        apply_btn.clicked.connect(apply_blur)
        
        layout.addWidget(QLabel("Intensidad:"))
        layout.addWidget(blur_slider)
        layout.addWidget(value_label)
        layout.addWidget(apply_btn)
        
        self.filters_layout.addWidget(group)

    def _create_sharpen_filter(self):
        """Crea el widget para el filtro de nitidez."""
        group = QGroupBox("Nitidez")
        layout = QVBoxLayout(group)
        
        sharpen_slider = QSlider(Qt.Horizontal)
        sharpen_slider.setRange(50, 300)  # 0.5x a 3.0x
        sharpen_slider.setValue(150)  # 1.5x por defecto
        
        value_label = QLabel("1.5x")
        value_label.setAlignment(Qt.AlignCenter)
        
        apply_btn = QPushButton("Aplicar Nitidez")
        
        sharpen_filter = SharpenFilter()
        self._filters["Nitidez"] = sharpen_filter
        
        def update_sharpen():
            value = sharpen_slider.value()
            factor = value / 100.0
            value_label.setText(f"{factor:.1f}x")
            sharpen_filter.set_parameters(factor=factor)
        
        def apply_sharpen():
            self.filter_applied.emit(sharpen_filter)
        
        sharpen_slider.valueChanged.connect(update_sharpen)
        apply_btn.clicked.connect(apply_sharpen)
        
        layout.addWidget(QLabel("Intensidad:"))
        layout.addWidget(sharpen_slider)
        layout.addWidget(value_label)
        layout.addWidget(apply_btn)
        
        self.filters_layout.addWidget(group)
