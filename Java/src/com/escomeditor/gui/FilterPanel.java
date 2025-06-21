package com.escomeditor.gui;

import com.escomeditor.filters.Filter;
import com.escomeditor.filters.GrayscaleFilter;
import com.escomeditor.filters.NegativeFilter;
import com.escomeditor.filters.BrightnessFilter;
import com.escomeditor.filters.ContrastFilter;
import com.escomeditor.filters.BlurFilter;
import com.escomeditor.filters.SharpenFilter;
import javafx.geometry.Insets;
import javafx.scene.control.*;
import javafx.scene.layout.VBox;

import java.util.Map;
import java.util.function.Consumer;

/**
 * Panel que contiene todos los filtros disponibles.
 */
public class FilterPanel extends VBox {

    private Consumer<Filter> onFilterApplied;

    private Slider brightnessSlider;
    private Button brightnessApplyBtn;

    private Slider contrastSlider;
    private Button contrastApplyBtn;

    private Slider blurSlider;
    private Button blurApplyBtn;

    private Slider sharpenSlider;
    private Button sharpenApplyBtn;

    public FilterPanel() {
        setPadding(new Insets(10));
        setSpacing(10);
        setPrefWidth(300);

        Label title = new Label("Filtros");
        title.setStyle("-fx-font-size: 18px; -fx-font-weight: bold;");
        getChildren().add(title);

        // Basic filters group
        TitledPane basicGroup = new TitledPane();
        basicGroup.setText("Filtros Básicos");
        VBox basicBox = new VBox(5);

        Button grayscaleBtn = new Button("Escala de Grises");
        grayscaleBtn.setOnAction(e -> applyFilter(new GrayscaleFilter()));
        basicBox.getChildren().add(grayscaleBtn);

        Button negativeBtn = new Button("Negativo");
        negativeBtn.setOnAction(e -> applyFilter(new NegativeFilter()));
        basicBox.getChildren().add(negativeBtn);

        basicGroup.setContent(basicBox);
        getChildren().add(basicGroup);

        // Advanced filters group with sliders
        TitledPane advancedGroup = new TitledPane();
        advancedGroup.setText("Ajustes Avanzados");
        VBox advancedBox = new VBox(10);

        // Brightness slider and button
        brightnessSlider = createSlider();
        brightnessApplyBtn = createApplyButton("Aplicar Brillo");
        brightnessApplyBtn.setOnAction(e -> {
            BrightnessFilter filter = new BrightnessFilter();
            filter.setParameters(Map.of("brightness", brightnessSlider.getValue() / 100.0));
            applyFilter(filter);
        });
        advancedBox.getChildren().addAll(new Label("Brillo"), brightnessSlider, brightnessApplyBtn);

        // Contrast slider and button
        contrastSlider = createSlider();
        contrastApplyBtn = createApplyButton("Aplicar Contraste");
        contrastApplyBtn.setOnAction(e -> {
            ContrastFilter filter = new ContrastFilter();
            filter.setParameters(Map.of("contrast", contrastSlider.getValue() / 100.0));
            applyFilter(filter);
        });
        advancedBox.getChildren().addAll(new Label("Contraste"), contrastSlider, contrastApplyBtn);

        // Blur slider and button
        blurSlider = createSlider();
        blurApplyBtn = createApplyButton("Aplicar Desenfoque");
        blurApplyBtn.setOnAction(e -> {
            BlurFilter filter = new BlurFilter();
            filter.setParameters(Map.of("blur", blurSlider.getValue() * 2 / 100.0)); // scale blur radius
            applyFilter(filter);
        });
        advancedBox.getChildren().addAll(new Label("Desenfoque"), blurSlider, blurApplyBtn);

        // Sharpen slider and button
        sharpenSlider = createSlider();
        sharpenApplyBtn = createApplyButton("Aplicar Nitidez");
        sharpenApplyBtn.setOnAction(e -> {
            SharpenFilter filter = new SharpenFilter();
            filter.setParameters(Map.of("sharpen", sharpenSlider.getValue() * 2 / 100.0)); // scale sharpen amount
            applyFilter(filter);
        });
        advancedBox.getChildren().addAll(new Label("Nitidez"), sharpenSlider, sharpenApplyBtn);

        advancedGroup.setContent(advancedBox);
        getChildren().add(advancedGroup);
    }

    private Slider createSlider() {
        Slider slider = new Slider(0, 200, 100);
        slider.setShowTickLabels(true);
        slider.setShowTickMarks(true);
        slider.setMajorTickUnit(50);
        slider.setBlockIncrement(10);
        slider.setSnapToTicks(true);
        slider.setPrefWidth(250);
        return slider;
    }

    private Button createApplyButton(String text) {
        Button btn = new Button(text);
        btn.setMaxWidth(Double.MAX_VALUE);
        return btn;
    }

    private void applyFilter(Filter filter) {
        if (onFilterApplied != null) {
            onFilterApplied.accept(filter);
        }
    }

    public void setOnFilterApplied(Consumer<Filter> handler) {
        this.onFilterApplied = handler;
    }
}
