"""
Implementación de filtros básicos para el procesamiento de imágenes.
"""

import cv2
import numpy as np
from PIL import ImageEnhance, Image as PILImage
from .base_filter import BaseFilter
from src.core.image import Image


class GrayscaleFilter(BaseFilter):
    """Convierte la imagen a escala de grises."""
    
    def __init__(self):
        super().__init__("Escala de Grises")
    
    def apply(self, image: Image) -> Image:
        cv_image = image.get_cv_image()
        gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
        image.update_from_cv(gray_image)
        return image

    def get_parameters(self) -> dict:
        return {}  # No tiene parámetros configurables

    def set_parameters(self, **kwargs):
        pass  # No tiene parámetros configurables


class BrightnessFilter(BaseFilter):
    """Ajusta el brillo de la imagen."""
    
    def __init__(self):
        super().__init__("Brillo")
        self._factor = 1.0  # Factor de brillo (1.0 es normal)
    
    def apply(self, image: Image) -> Image:
        pil_image = image.get_pil_image()
        enhancer = ImageEnhance.Brightness(pil_image)
        enhanced_image = enhancer.enhance(self._factor)
        image.update_from_pil(enhanced_image)
        return image

    def get_parameters(self) -> dict:
        return {"factor": self._factor}

    def set_parameters(self, **kwargs):
        if "factor" in kwargs:
            self._factor = float(kwargs["factor"])


class BlurFilter(BaseFilter):
    """Aplica un efecto de desenfoque gaussiano."""
    
    def __init__(self):
        super().__init__("Desenfoque")
        self._kernel_size = 5  # Tamaño del kernel (debe ser impar)
    
    def apply(self, image: Image) -> Image:
        cv_image = image.get_cv_image()
        blurred = cv2.GaussianBlur(cv_image, (self._kernel_size, self._kernel_size), 0)
        image.update_from_cv(blurred)
        return image

    def get_parameters(self) -> dict:
        return {"kernel_size": self._kernel_size}

    def set_parameters(self, **kwargs):
        if "kernel_size" in kwargs:
            size = int(kwargs["kernel_size"])
            # Asegurar que el tamaño del kernel sea impar
            self._kernel_size = size if size % 2 == 1 else size + 1


class SharpenFilter(BaseFilter):
    """Aplica un efecto de nitidez a la imagen."""
    
    def __init__(self):
        super().__init__("Nitidez")
        self._factor = 1.5  # Factor de nitidez
    
    def apply(self, image: Image) -> Image:
        pil_image = image.get_pil_image()
        enhancer = ImageEnhance.Sharpness(pil_image)
        enhanced_image = enhancer.enhance(self._factor)
        image.update_from_pil(enhanced_image)
        return image

    def get_parameters(self) -> dict:
        return {"factor": self._factor}

    def set_parameters(self, **kwargs):
        if "factor" in kwargs:
            self._factor = float(kwargs["factor"])


class ContrastFilter(BaseFilter):
    """Ajusta el contraste de la imagen."""
    
    def __init__(self):
        super().__init__("Contraste")
        self._factor = 1.0  # Factor de contraste
    
    def apply(self, image: Image) -> Image:
        pil_image = image.get_pil_image()
        enhancer = ImageEnhance.Contrast(pil_image)
        enhanced_image = enhancer.enhance(self._factor)
        image.update_from_pil(enhanced_image)
        return image

    def get_parameters(self) -> dict:
        return {"factor": self._factor}

    def set_parameters(self, **kwargs):
        if "factor" in kwargs:
            self._factor = float(kwargs["factor"])


class NegativeFilter(BaseFilter):
    """Filtro para crear el negativo de la imagen."""

    def __init__(self):
        super().__init__("Negativo")

    def apply(self, image: Image) -> Image:
        """
        Aplica el filtro negativo a la imagen.
        
        Args:
            image: Imagen a procesar.
            
        Returns:
            Imagen procesada.
        """
        pil_image = image.get_pil_image()
        if not pil_image:
            return image

        # Convertir a array numpy para facilitar la operación
        img_array = np.array(pil_image)
        
        # Invertir los valores (255 - valor_original)
        negative_array = 255 - img_array
        
        # Convertir de vuelta a PIL Image
        negative_image = PILImage.fromarray(negative_array.astype(np.uint8))
        
        image.update_from_pil(negative_image)
        return image

    def get_parameters(self) -> dict:
        return {}  # No tiene parámetros configurables

    def set_parameters(self, **kwargs):
        pass  # No tiene parámetros configurables
