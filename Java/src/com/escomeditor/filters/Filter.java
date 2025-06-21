package com.escomeditor.filters;

import com.escomeditor.core.Image;

import java.util.Map;

/**
 * Interfaz para filtros de imagen.
 */
public interface Filter {
    /**
     * Aplica el filtro a la imagen proporcionada.
     * @param image Imagen a procesar.
     * @return Imagen procesada.
     */
    Image apply(Image image);

    /**
     * Obtiene los parámetros configurables del filtro.
     * @return Mapa con los parámetros.
     */
    Map<String, Object> getParameters();

    /**
     * Establece los parámetros del filtro.
     * @param parameters Parámetros a establecer.
     */
    void setParameters(Map<String, Object> parameters);

    /**
     * Obtiene el nombre del filtro.
     * @return Nombre del filtro.
     */
    String getName();
}
