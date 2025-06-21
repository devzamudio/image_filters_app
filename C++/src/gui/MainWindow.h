#ifndef ESCOMEDITOR_GUI_MAINWINDOW_H
#define ESCOMEDITOR_GUI_MAINWINDOW_H

#include <QMainWindow>
#include <memory>
#include "../core/Image.h"
#include "ToolBar.h"
#include "FilterPanel.h"
#include "ImageView.h"

namespace escomeditor {
namespace gui {

class MainWindow : public QMainWindow {
    Q_OBJECT
public:
    explicit MainWindow(QWidget* parent = nullptr);
    ~MainWindow() override = default;

private slots:
    void onOpenImage();
    void onSaveImage();
    void onZoomIn();
    void onZoomOut();
    void onFitToWindow();
    void onFilterApplied(std::shared_ptr<filters::Filter> filter);

private:
    void setupUI();
    void setupConnections();
    void updateUndoRedoState();

    std::unique_ptr<core::Image> currentImage_;
    ToolBar* toolbar_;
    FilterPanel* filterPanel_;
    ImageView* imageView_;
};

} // namespace gui
} // namespace escomeditor

#endif // ESCOMEDITOR_GUI_MAINWINDOW_H
