#include "MainWindow.h"
#include <QFileDialog>
#include <QScrollArea>
#include <QSplitter>
#include <QLabel>
#include <QStatusBar>
#include <QMessageBox>
#include <QPixmap>
#include <QImage>
#include <QDebug>
#include <QVBoxLayout>

namespace escomeditor {
namespace gui {

MainWindow::MainWindow(QWidget* parent)
    : QMainWindow(parent),
      currentImage_(std::make_unique<core::Image>()),
      toolbar_(new ToolBar(this)),
      filterPanel_(new FilterPanel(this)),
      imageView_(new ImageView(this))
{
    setupUI();
    setupConnections();
}

void MainWindow::setupUI() {
    setWindowTitle("ESCOM-Editor");
    setMinimumSize(1200, 800);

    QWidget* centralWidget = new QWidget(this);
    setCentralWidget(centralWidget);

    QVBoxLayout* mainLayout = new QVBoxLayout(centralWidget);
    mainLayout->setContentsMargins(0, 0, 0, 0);
    mainLayout->setSpacing(0);

    mainLayout->addWidget(toolbar_);

    QSplitter* splitter = new QSplitter(Qt::Horizontal, centralWidget);
    mainLayout->addWidget(splitter);

    splitter->addWidget(filterPanel_);

    QScrollArea* scrollArea = new QScrollArea(splitter);
    scrollArea->setWidget(imageView_);
    scrollArea->setWidgetResizable(true);
    splitter->addWidget(scrollArea);

    splitter->setStretchFactor(0, 1);
    splitter->setStretchFactor(1, 4);

    statusBar()->showMessage("Listo");

    QLabel* copyrightLabel = new QLabel("© Leonardo Zamudio López 2025", this);
    copyrightLabel->setStyleSheet("color: #888888; font-size: 10px; margin-right: 10px;");
    statusBar()->addPermanentWidget(copyrightLabel);

    setStyleSheet(R"(
        QMainWindow {
            background-color: #2b2b2b;
        }
        QScrollArea {
            background-color: #1e1e1e;
            border: none;
        }
        QSplitter::handle {
            background-color: #3c3c3c;
        }
        QStatusBar {
            background-color: #2b2b2b;
            color: #ffffff;
        }
    )");
}

void MainWindow::setupConnections() {
    connect(toolbar_, &ToolBar::openAction, this, &MainWindow::onOpenImage);
    connect(toolbar_, &ToolBar::saveAction, this, &MainWindow::onSaveImage);
    connect(toolbar_, &ToolBar::zoomInAction, this, &MainWindow::onZoomIn);
    connect(toolbar_, &ToolBar::zoomOutAction, this, &MainWindow::onZoomOut);
    connect(toolbar_, &ToolBar::fitToWindowAction, this, &MainWindow::onFitToWindow);

    connect(filterPanel_, &FilterPanel::filterApplied, this, &MainWindow::onFilterApplied);
}

void MainWindow::onOpenImage() {
    QString filePath = QFileDialog::getOpenFileName(
        this,
        "Abrir Imagen",
        QString(),
        "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif);;Todos los archivos (*.*)"
    );

    if (!filePath.isEmpty()) {
        if (currentImage_->load(filePath.toStdString())) {
            imageView_->setImage(*currentImage_);
            imageView_->fitToWindow();  // Fit and center image on load
            statusBar()->showMessage(QString("Imagen cargada: %1").arg(QFileInfo(filePath).fileName()));
            toolbar_->enableImageActions(true);
            updateUndoRedoState();
        } else {
            statusBar()->showMessage("Error al cargar la imagen");
        }
    }
}

void MainWindow::onSaveImage() {
    if (currentImage_->getCvImage().empty()) {
        statusBar()->showMessage("No hay imagen para guardar");
        return;
    }

    QString filePath = QFileDialog::getSaveFileName(
        this,
        "Guardar Imagen",
        QString(),
        "PNG (*.png);;JPEG (*.jpg);;BMP (*.bmp)"
    );

    if (!filePath.isEmpty()) {
        QString ext = QFileInfo(filePath).suffix().toLower();
        if (!QStringList({"png", "jpg", "jpeg", "bmp"}).contains(ext)) {
            if (filePath.endsWith('.')) {
                filePath.chop(1);
            }
            if (filePath.endsWith('.')) {
                filePath.chop(1);
            }
            if (filePath.endsWith('.')) {
                filePath.chop(1);
            }
            // Default to PNG
            filePath += ".png";
        }

        if (currentImage_->save(filePath.toStdString())) {
            statusBar()->showMessage(QString("Imagen guardada como: %1").arg(QFileInfo(filePath).fileName()));
        } else {
            statusBar()->showMessage("Error al guardar la imagen");
        }
    }
}

void MainWindow::onZoomIn() {
    imageView_->zoomIn();
    statusBar()->showMessage("Zoom aumentado");
}

void MainWindow::onZoomOut() {
    imageView_->zoomOut();
    statusBar()->showMessage("Zoom disminuido");
}

void MainWindow::onFitToWindow() {
    imageView_->fitToWindow();
    statusBar()->showMessage("Imagen ajustada a ventana");
}

void MainWindow::onFilterApplied(std::shared_ptr<filters::Filter> filter) {
    if (!currentImage_->getCvImage().empty()) {
        double currentScale = imageView_->getScaleFactor();
        filter->apply(*currentImage_);
        imageView_->setImage(*currentImage_);
        imageView_->setScaleFactor(currentScale);  // Restore zoom level after applying filter
        statusBar()->showMessage(QString("Filtro aplicado: %1").arg(QString::fromStdString(filter->getName())));
    } else {
        statusBar()->showMessage("No hay imagen para aplicar el filtro");
    }
}

void MainWindow::updateUndoRedoState() {
    // Implementation to update undo/redo buttons if any
}

} // namespace gui
} // namespace escomeditor
