#ifndef ESCOMEDITOR_GUI_IMAGEVIEW_H
#define ESCOMEDITOR_GUI_IMAGEVIEW_H

#include <QWidget>
#include <QImage>
#include <QPixmap>
#include <opencv2/opencv.hpp>
#include "../core/Image.h"

namespace escomeditor {
namespace gui {

class ImageView : public QWidget {
    Q_OBJECT
public:
    explicit ImageView(QWidget* parent = nullptr);

    void setImage(const core::Image& image);
    void updateImage();

    void zoomIn();
    void zoomOut();
    void fitToWindow();

    double getScaleFactor() const;
    void setScaleFactor(double scale);

protected:
    void paintEvent(QPaintEvent* event) override;

private:
    QImage cvMatToQImage(const cv::Mat& mat) const;

    QPixmap pixmap_;
    double scaleFactor_;
};

} // namespace gui
} // namespace escomeditor

#endif // ESCOMEDITOR_GUI_IMAGEVIEW_H
