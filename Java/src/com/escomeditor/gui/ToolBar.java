package com.escomeditor.gui;

import javafx.geometry.Insets;
import javafx.scene.control.Button;
import javafx.scene.layout.HBox;

/**
 * Barra de herramientas personalizada con estilo moderno.
 */
public class ToolBar extends HBox {

    private Button openButton;
    private Button saveButton;
    private Button zoomInButton;
    private Button zoomOutButton;
    private Button fitToWindowButton;

    public ToolBar() {
        setPadding(new Insets(5));
        setSpacing(5);
        setStyle("-fx-background-color: #3c3c3c; -fx-border-color: #555555; -fx-border-width: 0 0 1 0;");

        openButton = new Button("📁 Abrir");
        saveButton = new Button("💾 Guardar");
        zoomInButton = new Button("🔍+ Acercar");
        zoomOutButton = new Button("🔍- Alejar");
        fitToWindowButton = new Button("⛶ Ajustar");

        saveButton.setDisable(true);
        zoomInButton.setDisable(true);
        zoomOutButton.setDisable(true);
        fitToWindowButton.setDisable(true);

        getChildren().addAll(openButton, saveButton, zoomInButton, zoomOutButton, fitToWindowButton);
    }

    public Button getOpenButton() {
        return openButton;
    }

    public Button getSaveButton() {
        return saveButton;
    }

    public Button getZoomInButton() {
        return zoomInButton;
    }

    public Button getZoomOutButton() {
        return zoomOutButton;
    }

    public Button getFitToWindowButton() {
        return fitToWindowButton;
    }

    public void enableImageActions(boolean enabled) {
        saveButton.setDisable(!enabled);
        zoomInButton.setDisable(!enabled);
        zoomOutButton.setDisable(!enabled);
        fitToWindowButton.setDisable(!enabled);
    }
}
