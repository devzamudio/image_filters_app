package com.escomeditor.gui;

import com.escomeditor.core.Image;
import com.escomeditor.filters.Filter;
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.SplitPane;
import javafx.scene.image.WritableImage;
import javafx.scene.layout.*;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

/**
 * Ventana principal de la aplicación.
 */
public class MainWindow extends Application {

    private Image currentImage;
    private javafx.scene.image.ImageView imageView;
    private ToolBar toolBar;
    private FilterPanel filterPanel;
    private javafx.scene.control.Label statusLabel;

    @Override
    public void start(javafx.stage.Stage primaryStage) {
        primaryStage.setTitle("ESCOM-Editor por Leonardo Zamudio López");

        currentImage = new Image();

        javafx.scene.layout.BorderPane root = new javafx.scene.layout.BorderPane();

        // Toolbar
        toolBar = new ToolBar();
        toolBar.setPadding(new javafx.geometry.Insets(5));
        root.setTop(toolBar);

        // Filter panel
        filterPanel = new FilterPanel();
        filterPanel.setPrefWidth(300);

        // Image view
        imageView = new javafx.scene.image.ImageView();
        imageView.setPreserveRatio(true);
        javafx.scene.control.ScrollPane imageScrollPane = new javafx.scene.control.ScrollPane(imageView);
        imageScrollPane.setFitToWidth(true);
        imageScrollPane.setFitToHeight(true);

        javafx.scene.control.SplitPane splitPane = new javafx.scene.control.SplitPane();
        splitPane.getItems().addAll(filterPanel, imageScrollPane);
        splitPane.setDividerPositions(0.25);
        root.setCenter(splitPane);

        // Status bar
        statusLabel = new javafx.scene.control.Label("Listo");
        javafx.scene.layout.HBox statusBar = new javafx.scene.layout.HBox(statusLabel);
        statusBar.setPadding(new javafx.geometry.Insets(5));
        statusBar.setStyle("-fx-background-color: #2b2b2b; -fx-text-fill: white;");
        root.setBottom(statusBar);

        setupEventHandlers(primaryStage);

        javafx.scene.Scene scene = new javafx.scene.Scene(root, 1200, 800);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void setupEventHandlers(javafx.stage.Stage stage) {
        toolBar.getOpenButton().setOnAction(e -> openImage(stage));
        toolBar.getSaveButton().setOnAction(e -> saveImage(stage));
        toolBar.getZoomInButton().setOnAction(e -> zoomIn());
        toolBar.getZoomOutButton().setOnAction(e -> zoomOut());
        toolBar.getFitToWindowButton().setOnAction(e -> fitToWindow());

        filterPanel.setOnFilterApplied(filter -> {
            if (currentImage.getBufferedImage() != null) {
                filter.apply(currentImage);
                updateImageView();
                setStatus("Filtro aplicado: " + filter.getName());
            } else {
                setStatus("No hay imagen para aplicar el filtro");
            }
        });
    }

    private void openImage(javafx.stage.Stage stage) {
        javafx.stage.FileChooser fileChooser = new javafx.stage.FileChooser();
        fileChooser.setTitle("Abrir Imagen");
        fileChooser.getExtensionFilters().addAll(
                new javafx.stage.FileChooser.ExtensionFilter("Imágenes", "*.png", "*.jpg", "*.jpeg", "*.bmp", "*.gif"),
                new javafx.stage.FileChooser.ExtensionFilter("Todos los archivos", "*.*")
        );
        java.io.File file = fileChooser.showOpenDialog(stage);
        if (file != null) {
            if (currentImage.load(file.getAbsolutePath())) {
                updateImageView();
                setStatus("Imagen cargada: " + file.getName());
                toolBar.enableImageActions(true);
            } else {
                setStatus("Error al cargar la imagen");
            }
        }
    }

    private void saveImage(javafx.stage.Stage stage) {
        if (currentImage.getBufferedImage() == null) {
            setStatus("No hay imagen para guardar");
            return;
        }
        javafx.stage.FileChooser fileChooser = new javafx.stage.FileChooser();
        fileChooser.setTitle("Guardar Imagen");
        fileChooser.getExtensionFilters().addAll(
                new javafx.stage.FileChooser.ExtensionFilter("PNG", "*.png"),
                new javafx.stage.FileChooser.ExtensionFilter("JPEG", "*.jpg"),
                new javafx.stage.FileChooser.ExtensionFilter("BMP", "*.bmp")
        );
        java.io.File file = fileChooser.showSaveDialog(stage);
        if (file != null) {
            String path = file.getAbsolutePath();
            if (!path.toLowerCase().endsWith(".png") && !path.toLowerCase().endsWith(".jpg") && !path.toLowerCase().endsWith(".bmp")) {
                path += ".png"; // default extension
            }
            if (currentImage.save(path)) {
                setStatus("Imagen guardada como: " + file.getName());
            } else {
                setStatus("Error al guardar la imagen");
            }
        }
    }

    private void updateImageView() {
        java.awt.image.BufferedImage bufferedImage = currentImage.getBufferedImage();
        if (bufferedImage != null) {
            javafx.scene.image.WritableImage fxImage = javafx.embed.swing.SwingFXUtils.toFXImage(bufferedImage, null);
            imageView.setImage(fxImage);
            fitToWindow();
        }
    }

    private void zoomIn() {
        imageView.setScaleX(imageView.getScaleX() * 1.25);
        imageView.setScaleY(imageView.getScaleY() * 1.25);
        setStatus("Zoom aumentado");
    }

    private void zoomOut() {
        imageView.setScaleX(imageView.getScaleX() / 1.25);
        imageView.setScaleY(imageView.getScaleY() / 1.25);
        setStatus("Zoom disminuido");
    }

    private void fitToWindow() {
        // Adjust the imageView to fit the scroll pane size and center the image
        // Fix ClassCastException by storing the ScrollPane reference
        javafx.scene.control.ScrollPane scrollPane = null;
        if (imageView.getParent() instanceof javafx.scene.control.ScrollPane) {
            scrollPane = (javafx.scene.control.ScrollPane) imageView.getParent();
        } else if (imageView.getParent() instanceof javafx.scene.layout.Region) {
            // Try to find ScrollPane in the parent hierarchy
            javafx.scene.Parent parent = imageView.getParent();
            while (parent != null && !(parent instanceof javafx.scene.control.ScrollPane)) {
                parent = parent.getParent();
            }
            if (parent instanceof javafx.scene.control.ScrollPane) {
                scrollPane = (javafx.scene.control.ScrollPane) parent;
            }
        }

        if (scrollPane == null) {
            setStatus("No se pudo encontrar el ScrollPane para ajustar la imagen");
            return;
        }

        double scrollWidth = scrollPane.getViewportBounds().getWidth();
        double scrollHeight = scrollPane.getViewportBounds().getHeight();

        if (imageView.getImage() != null) {
            double imageWidth = imageView.getImage().getWidth();
            double imageHeight = imageView.getImage().getHeight();

            double scaleX = scrollWidth / imageWidth;
            double scaleY = scrollHeight / imageHeight;
            double scale = Math.min(scaleX, scaleY);

            imageView.setFitWidth(imageWidth * scale);
            imageView.setFitHeight(imageHeight * scale);
            imageView.setScaleX(1.0);
            imageView.setScaleY(1.0);

            // Center the imageView inside the scroll pane by setting alignment
            scrollPane.setHvalue(0.5);
            scrollPane.setVvalue(0.5);
        }
        setStatus("Imagen ajustada a ventana y centrada");
    }

    private void setStatus(String message) {
        statusLabel.setText(message);
    }

    public static void main(String[] args) {
        javafx.application.Application.launch(args);
    }
}
