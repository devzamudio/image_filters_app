"""
Clase abstracta base para todos los filtros de imagen.
"""

from abc import ABC, abstractmethod
from src.core.image import Image


class BaseFilter(ABC):
    """
    Clase abstracta que define la interfaz para todos los filtros de imagen.
    Implementa el patrón Strategy para permitir intercambiar algoritmos de filtrado.
    """

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        """Retorna el nombre del filtro."""
        return self._name

    @abstractmethod
    def apply(self, image: Image) -> Image:
        """
        Aplica el filtro a la imagen proporcionada.
        
        Args:
            image: Imagen a la cual aplicar el filtro.
            
        Returns:
            Image: Nueva imagen con el filtro aplicado.
        """
        pass

    @abstractmethod
    def get_parameters(self) -> dict:
        """
        Retorna los parámetros configurables del filtro.
        
        Returns:
            dict: Diccionario con los parámetros del filtro.
        """
        pass

    @abstractmethod
    def set_parameters(self, **kwargs):
        """
        Establece los parámetros del filtro.
        
        Args:
            **kwargs: Parámetros del filtro como argumentos nombrados.
        """
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name='{self._name}')"

    def __repr__(self) -> str:
        return self.__str__()
