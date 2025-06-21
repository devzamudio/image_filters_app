package com.escomeditor.filters;

import com.escomeditor.core.Image;

import java.awt.image.BufferedImage;
import java.awt.image.ConvolveOp;
import java.awt.image.Kernel;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

/**
 * Filtro para aplicar desenfoque (blur) a la imagen.
 * El parámetro "blur" es un porcentaje (0-200).
 */
public class BlurFilter implements Filter {
    private final String name = "Desenfoque";
    private float blurRadius = 1.0f; // 1.0 = 100%

    @Override
    public Image apply(Image image) {
        BufferedImage src = image.getBufferedImage();
        if (src == null) return image;

        int radius = Math.max(1, Math.round(blurRadius));
        int size = radius * 2 + 1;
        float[] data = new float[size * size];
        float value = 1.0f / (size * size);
        for (int i = 0; i < data.length; i++) {
            data[i] = value;
        }
        Kernel kernel = new Kernel(size, size, data);
        ConvolveOp op = new ConvolveOp(kernel, ConvolveOp.EDGE_NO_OP, null);
        BufferedImage blurred = op.filter(src, null);

        image.updateImage(blurred);
        return image;
    }

    @Override
    public Map<String, Object> getParameters() {
        Map<String, Object> params = new HashMap<>();
        params.put("blur", blurRadius);
        return params;
    }

    @Override
    public void setParameters(Map<String, Object> parameters) {
        if (parameters.containsKey("blur")) {
            Object val = parameters.get("blur");
            if (val instanceof Number) {
                blurRadius = ((Number) val).floatValue();
            }
        }
    }

    @Override
    public String getName() {
        return name;
    }
}
