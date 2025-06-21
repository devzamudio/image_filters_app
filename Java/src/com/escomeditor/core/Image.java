package com.escomeditor.core;

import javafx.scene.image.WritableImage;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Stack;

/**
 * Clase que encapsula una imagen y proporciona métodos para su manipulación.
 * Utiliza BufferedImage para la representación de imágenes y mantiene un historial para deshacer/rehacer.
 */
public class Image {
    private BufferedImage bufferedImage;
    private String filename;
    private boolean modified;

    private final Stack<BufferedImage> history = new Stack<>();
    private final Stack<BufferedImage> future = new Stack<>();
    private final int maxHistory = 20;

    public Image() {
        this.bufferedImage = null;
        this.filename = null;
        this.modified = false;
    }

    public String getFilename() {
        return filename;
    }

    public int getWidth() {
        return bufferedImage != null ? bufferedImage.getWidth() : 0;
    }

    public int getHeight() {
        return bufferedImage != null ? bufferedImage.getHeight() : 0;
    }

    public boolean isModified() {
        return modified;
    }

    public boolean load(String filepath) {
        try {
            File file = new File(filepath);
            bufferedImage = ImageIO.read(file);
            filename = file.getName();
            modified = false;
            clearHistory();
            addToHistory(copyImage(bufferedImage));
            return true;
        } catch (IOException e) {
            System.err.println("Error al cargar la imagen: " + e.getMessage());
            return false;
        }
    }

    public boolean save(String filepath) {
        try {
            if (bufferedImage != null) {
                File file = new File(filepath);
                String ext = getFileExtension(filepath);
                if (ext == null) {
                    ext = "png"; // default
                }
                ImageIO.write(bufferedImage, ext, file);
                modified = false;
                return true;
            }
            return false;
        } catch (IOException e) {
            System.err.println("Error al guardar la imagen: " + e.getMessage());
            return false;
        }
    }

    public BufferedImage getBufferedImage() {
        return bufferedImage;
    }

    public void updateImage(BufferedImage newImage) {
        if (newImage != null) {
            addToHistory(copyImage(bufferedImage));
            bufferedImage = newImage;
            modified = true;
            future.clear();
        }
    }

    private void addToHistory(BufferedImage image) {
        if (history.size() >= maxHistory) {
            history.remove(0);
        }
        history.push(image);
    }

    private void clearHistory() {
        history.clear();
        future.clear();
    }

    public boolean canUndo() {
        return !history.isEmpty();
    }

    public boolean canRedo() {
        return !future.isEmpty();
    }

    public boolean undo() {
        if (!canUndo()) {
            return false;
        }
        future.push(copyImage(bufferedImage));
        bufferedImage = history.pop();
        modified = true;
        return true;
    }

    public boolean redo() {
        if (!canRedo()) {
            return false;
        }
        history.push(copyImage(bufferedImage));
        bufferedImage = future.pop();
        modified = true;
        return true;
    }

    private BufferedImage copyImage(BufferedImage source) {
        if (source == null) return null;
        BufferedImage copy = new BufferedImage(source.getWidth(), source.getHeight(), source.getType());
        copy.setData(source.getData());
        return copy;
    }

    private String getFileExtension(String filename) {
        int dotIndex = filename.lastIndexOf('.');
        if (dotIndex > 0 && dotIndex < filename.length() - 1) {
            return filename.substring(dotIndex + 1).toLowerCase();
        }
        return null;
    }
}
