package com.escomeditor.filters;

import com.escomeditor.core.Image;

import java.awt.image.BufferedImage;
import java.awt.image.ConvolveOp;
import java.awt.image.Kernel;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

/**
 * Filtro para aplicar nitidez (sharpen) a la imagen.
 * El parámetro "sharpen" es un porcentaje (0-200).
 */
public class SharpenFilter implements Filter {
    private final String name = "Nitidez";
    private float sharpenAmount = 1.0f; // 1.0 = 100%

    @Override
    public Image apply(Image image) {
        BufferedImage src = image.getBufferedImage();
        if (src == null) return image;

        float amount = sharpenAmount;
        float[] kernelData = {
            0, -amount, 0,
            -amount, 1 + 4 * amount, -amount,
            0, -amount, 0
        };
        Kernel kernel = new Kernel(3, 3, kernelData);
        ConvolveOp op = new ConvolveOp(kernel, ConvolveOp.EDGE_NO_OP, null);
        BufferedImage sharpened = op.filter(src, null);

        image.updateImage(sharpened);
        return image;
    }

    @Override
    public Map<String, Object> getParameters() {
        Map<String, Object> params = new HashMap<>();
        params.put("sharpen", sharpenAmount);
        return params;
    }

    @Override
    public void setParameters(Map<String, Object> parameters) {
        if (parameters.containsKey("sharpen")) {
            Object val = parameters.get("sharpen");
            if (val instanceof Number) {
                sharpenAmount = ((Number) val).floatValue();
            }
        }
    }

    @Override
    public String getName() {
        return name;
    }
}
