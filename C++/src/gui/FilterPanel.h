#ifndef ESCOMEDITOR_GUI_FILTERPANEL_H
#define ESCOMEDITOR_GUI_FILTERPANEL_H

#include <QWidget>
#include <QPushButton>
#include <QSlider>
#include <QLabel>
#include <memory>
#include <vector>
#include "../filters/Filter.h"

namespace escomeditor {
namespace gui {

class FilterPanel : public QWidget {
    Q_OBJECT
public:
    explicit FilterPanel(QWidget* parent = nullptr);

signals:
    void filterApplied(std::shared_ptr<filters::Filter> filter);

private slots:
    void onGrayscaleClicked();
    void onNegativeClicked();
    void onBrightnessApplyClicked();
    void onContrastApplyClicked();
    void onBlurApplyClicked();
    void onSharpenApplyClicked();

private:
    QPushButton* grayscaleButton_;
    QPushButton* negativeButton_;

    QSlider* brightnessSlider_;
    QPushButton* brightnessApplyButton_;

    QSlider* contrastSlider_;
    QPushButton* contrastApplyButton_;

    QSlider* blurSlider_;
    QPushButton* blurApplyButton_;

    QSlider* sharpenSlider_;
    QPushButton* sharpenApplyButton_;

    void setupUI();
    void setupConnections();
};

} // namespace gui
} // namespace escomeditor

#endif // ESCOMEDITOR_GUI_FILTERPANEL_H
