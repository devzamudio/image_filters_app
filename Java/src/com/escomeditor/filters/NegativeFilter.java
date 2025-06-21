package com.escomeditor.filters;

import com.escomeditor.core.Image;

import java.awt.image.BufferedImage;
import java.awt.Color;
import java.util.Collections;
import java.util.Map;

/**
 * Filtro para invertir los colores de la imagen (negativo).
 */
public class NegativeFilter implements Filter {
    private final String name = "Negativo";

    @Override
    public Image apply(Image image) {
        BufferedImage src = image.getBufferedImage();
        if (src == null) return image;

        BufferedImage negative = new BufferedImage(src.getWidth(), src.getHeight(), BufferedImage.TYPE_INT_RGB);

        for (int y = 0; y < src.getHeight(); y++) {
            for (int x = 0; x < src.getWidth(); x++) {
                Color c = new Color(src.getRGB(x, y));
                int r = 255 - c.getRed();
                int g = 255 - c.getGreen();
                int b = 255 - c.getBlue();
                Color negColor = new Color(r, g, b);
                negative.setRGB(x, y, negColor.getRGB());
            }
        }

        image.updateImage(negative);
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
