"""
Clase principal para el manejo de imágenes.
"""

from PIL import Image as PILImage
import cv2
import numpy as np
from typing import Tuple, Optional
from pathlib import Path


class Image:
    """
    Clase que encapsula una imagen y proporciona métodos para su manipulación.
    Utiliza tanto Pillow como OpenCV según sea necesario para diferentes operaciones.
    """

    def __init__(self):
        self._pil_image: Optional[PILImage.Image] = None
        self._cv_image: Optional[np.ndarray] = None
        self._filename: Optional[str] = None
        self._modified: bool = False
        
        # Historial para deshacer/rehacer
        self._history: list[PILImage.Image] = []
        self._current_index: int = -1
        self._max_history: int = 20  # Máximo número de estados guardados

    @property
    def filename(self) -> Optional[str]:
        """Retorna el nombre del archivo de la imagen."""
        return self._filename

    @property
    def size(self) -> Tuple[int, int]:
        """Retorna el tamaño de la imagen (ancho, alto)."""
        if self._pil_image:
            return self._pil_image.size
        return (0, 0)

    @property
    def modified(self) -> bool:
        """Indica si la imagen ha sido modificada desde su última carga o guardado."""
        return self._modified

    def load(self, filepath: str) -> bool:
        """
        Carga una imagen desde el archivo especificado.
        
        Args:
            filepath: Ruta al archivo de imagen.
            
        Returns:
            bool: True si la carga fue exitosa, False en caso contrario.
        """
        try:
            # Cargar con Pillow
            self._pil_image = PILImage.open(filepath)
            self._pil_image = self._pil_image.convert('RGB')
            
            # Convertir a formato OpenCV
            self._cv_image = cv2.cvtColor(np.array(self._pil_image), cv2.COLOR_RGB2BGR)
            
            self._filename = Path(filepath).name
            self._modified = False
            
            # Agregar al historial
            self._add_to_history(self._pil_image.copy())
            return True
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            return False

    def save(self, filepath: str) -> bool:
        """
        Guarda la imagen en el archivo especificado.
        
        Args:
            filepath: Ruta donde guardar la imagen.
            
        Returns:
            bool: True si el guardado fue exitoso, False en caso contrario.
        """
        try:
            if self._pil_image:
                self._pil_image.save(filepath)
                self._modified = False
                return True
            return False
        except Exception as e:
            print(f"Error al guardar la imagen: {e}")
            return False

    def get_pil_image(self) -> Optional[PILImage.Image]:
        """Retorna la imagen en formato Pillow."""
        return self._pil_image

    def get_cv_image(self) -> Optional[np.ndarray]:
        """Retorna la imagen en formato OpenCV."""
        return self._cv_image

    def update_from_cv(self, cv_image: np.ndarray):
        """
        Actualiza la imagen desde un array de OpenCV.
        
        Args:
            cv_image: Imagen en formato OpenCV (numpy array).
        """
        self._cv_image = cv_image
        # Convertir de BGR (OpenCV) a RGB (Pillow)
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        self._pil_image = PILImage.fromarray(rgb_image)
        self._modified = True

    def update_from_pil(self, pil_image: PILImage.Image, add_to_history: bool = True):
        """
        Actualiza la imagen desde una imagen Pillow.
        
        Args:
            pil_image: Imagen en formato Pillow.
            add_to_history: Si True, agrega el estado actual al historial antes de actualizar.
        """
        # Agregar al historial antes de actualizar si se solicita
        if add_to_history and self._pil_image is not None:
            self._add_to_history(self._pil_image.copy())
        
        self._pil_image = pil_image
        # Convertir a formato OpenCV
        self._cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
        self._modified = True

    def _add_to_history(self, image: PILImage.Image):
        """
        Agrega una imagen al historial para deshacer/rehacer.
        
        Args:
            image: Imagen a agregar al historial.
        """
        # Si estamos en el medio del historial, eliminar estados futuros
        if self._current_index < len(self._history) - 1:
            self._history = self._history[:self._current_index + 1]
        
        # Solo agregar si es diferente al último estado
        if not self._history or not np.array_equal(np.array(self._history[-1]), np.array(image)):
            # Agregar nueva imagen
            self._history.append(image)
            self._current_index += 1
            
            # Limitar el tamaño del historial
            if len(self._history) > self._max_history:
                self._history.pop(0)
                self._current_index -= 1

    def can_undo(self) -> bool:
        """Retorna True si se puede deshacer una acción."""
        return self._current_index > 0

    def can_redo(self) -> bool:
        """Retorna True si se puede rehacer una acción."""
        return self._current_index < len(self._history) - 1

    def undo(self) -> bool:
        """
        Deshace la última acción.
        
        Returns:
            bool: True si se pudo deshacer, False en caso contrario.
        """
        if not self.can_undo():
            return False
        
        self._current_index -= 1
        previous_image = self._history[self._current_index]
        
        # Actualizar sin agregar al historial
        self.update_from_pil(previous_image.copy(), add_to_history=False)
        
        return True

    def redo(self) -> bool:
        """
        Rehace la última acción deshecha.
        
        Returns:
            bool: True si se pudo rehacer, False en caso contrario.
        """
        if not self.can_redo():
            return False
        
        self._current_index += 1
        next_image = self._history[self._current_index]
        
        # Actualizar sin agregar al historial
        self.update_from_pil(next_image.copy(), add_to_history=False)
        
        return True
