package com.escomeditor.filters;

import com.escomeditor.core.Image;

import java.awt.image.BufferedImage;
import java.awt.Color;
import java.util.Collections;
import java.util.Map;

/**
 * Filtro para convertir la imagen a escala de grises.
 */
public class GrayscaleFilter implements Filter {
    private final String name = "Escala de Grises";

    @Override
    public Image apply(Image image) {
        BufferedImage src = image.getBufferedImage();
        if (src == null) return image;

        BufferedImage gray = new BufferedImage(src.getWidth(), src.getHeight(), BufferedImage.TYPE_INT_RGB);

        for (int y = 0; y < src.getHeight(); y++) {
            for (int x = 0; x < src.getWidth(); x++) {
                Color c = new Color(src.getRGB(x, y));
                int grayValue = (int)(0.299 * c.getRed() + 0.587 * c.getGreen() + 0.114 * c.getBlue());
                Color gColor = new Color(grayValue, grayValue, grayValue);
                gray.setRGB(x, y, gColor.getRGB());
            }
        }

        image.updateImage(gray);
        return image;
    }

    @Override
    public Map<String, Object> getParameters() {
        return Collections.emptyMap();
    }

    @Override
    public void setParameters(Map<String, Object> parameters) {
        // No parameters
    }

    @Override
    public String getName() {
        return name;
    }
}
