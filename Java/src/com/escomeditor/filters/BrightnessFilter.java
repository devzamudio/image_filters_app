package com.escomeditor.filters;

import com.escomeditor.core.Image;

import java.awt.image.BufferedImage;
import java.awt.Color;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

/**
 * Filtro para ajustar el brillo de la imagen.
 * El parámetro "brightness" es un porcentaje (0-200).
 */
public class BrightnessFilter implements Filter {
    private final String name = "Brillo";
    private double brightness = 1.0; // 1.0 = 100%

    @Override
    public Image apply(Image image) {
        BufferedImage src = image.getBufferedImage();
        if (src == null) return image;

        BufferedImage output = new BufferedImage(src.getWidth(), src.getHeight(), BufferedImage.TYPE_INT_RGB);

        for (int y = 0; y < src.getHeight(); y++) {
            for (int x = 0; x < src.getWidth(); x++) {
                Color c = new Color(src.getRGB(x, y));
                int r = clamp((int)(c.getRed() * brightness));
                int g = clamp((int)(c.getGreen() * brightness));
                int b = clamp((int)(c.getBlue() * brightness));
                Color newColor = new Color(r, g, b);
                output.setRGB(x, y, newColor.getRGB());
            }
        }

        image.updateImage(output);
        return image;
    }

    private int clamp(int val) {
        return Math.min(255, Math.max(0, val));
    }

    @Override
    public Map<String, Object> getParameters() {
        Map<String, Object> params = new HashMap<>();
        params.put("brightness", brightness);
        return params;
    }

    @Override
    public void setParameters(Map<String, Object> parameters) {
        if (parameters.containsKey("brightness")) {
            Object val = parameters.get("brightness");
            if (val instanceof Number) {
                brightness = ((Number) val).doubleValue();
            }
        }
    }

    @Override
    public String getName() {
        return name;
    }
}
