#include "ImageView.h"
#include <QPainter>
#include <QResizeEvent>

namespace escomeditor {
namespace gui {

ImageView::ImageView(QWidget* parent)
    : QWidget(parent), scaleFactor_(1.0) {}

void ImageView::setImage(const core::Image& image) {
    cv::Mat cvImage = image.getCvImage();
    if (cvImage.empty()) {
        pixmap_ = QPixmap();
        update();
        return;
    }
    QImage qimg = cvMatToQImage(cvImage);
    pixmap_ = QPixmap::fromImage(qimg);
    // Do not reset scaleFactor_ here to preserve zoom level
    update();
}

double ImageView::getScaleFactor() const {
    return scaleFactor_;
}

void ImageView::setScaleFactor(double scale) {
    scaleFactor_ = scale;
    update();
}

void ImageView::updateImage() {
    update();
}

void ImageView::zoomIn() {
    scaleFactor_ *= 1.25;
    update();
}

void ImageView::zoomOut() {
    scaleFactor_ /= 1.25;
    update();
}

void ImageView::fitToWindow() {
    if (pixmap_.isNull()) return;
    QSize widgetSize = size();
    QSize pixmapSize = pixmap_.size();
    double scaleX = static_cast<double>(widgetSize.width()) / pixmapSize.width();
    double scaleY = static_cast<double>(widgetSize.height()) / pixmapSize.height();
    scaleFactor_ = std::min(scaleX, scaleY);
    update();
}

void ImageView::paintEvent(QPaintEvent* event) {
    QPainter painter(this);
    painter.fillRect(rect(), Qt::black);
    if (pixmap_.isNull()) return;

    QSize scaledSize = pixmap_.size() * scaleFactor_;
    QPoint center = rect().center() - QPoint(scaledSize.width() / 2, scaledSize.height() / 2);
    painter.drawPixmap(center, pixmap_.scaled(scaledSize, Qt::KeepAspectRatio, Qt::SmoothTransformation));
}

QImage ImageView::cvMatToQImage(const cv::Mat& mat) const {
    if (mat.empty()) return QImage();

    switch (mat.type()) {
        case CV_8UC1: {
            QImage img(mat.data, mat.cols, mat.rows, static_cast<int>(mat.step), QImage::Format_Grayscale8);
            return img.copy();
        }
        case CV_8UC3: {
            QImage img(mat.data, mat.cols, mat.rows, static_cast<int>(mat.step), QImage::Format_RGB888);
            return img.rgbSwapped().copy();
        }
        case CV_8UC4: {
            QImage img(mat.data, mat.cols, mat.rows, static_cast<int>(mat.step), QImage::Format_ARGB32);
            return img.copy();
        }
        default:
            return QImage();
    }
}

} // namespace gui
} // namespace escomeditor
