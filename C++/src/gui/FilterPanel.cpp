#include "FilterPanel.h"
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QSlider>
#include <memory>
#include "../filters/GrayscaleFilter.h"
#include "../filters/BrightnessFilter.h"
#include "../filters/ContrastFilter.h"
#include "../filters/BlurFilter.h"
#include "../filters/SharpenFilter.h"
#include "../filters/NegativeFilter.h"

namespace escomeditor {
namespace gui {

FilterPanel::FilterPanel(QWidget* parent)
    : QWidget(parent)
{
    setupUI();
    setupConnections();
}

void FilterPanel::setupUI() {
    QVBoxLayout* mainLayout = new QVBoxLayout(this);

    // Grayscale button
    grayscaleButton_ = new QPushButton("Escala de Grises", this);
    mainLayout->addWidget(grayscaleButton_);

    // Negative button
    negativeButton_ = new QPushButton("Negativo", this);
    mainLayout->addWidget(negativeButton_);

    // Brightness slider and apply button
    QLabel* brightnessLabel = new QLabel("Brillo", this);
    brightnessSlider_ = new QSlider(Qt::Horizontal, this);
    brightnessSlider_->setRange(0, 200);
    brightnessSlider_->setValue(100);
    brightnessApplyButton_ = new QPushButton("Aplicar Brillo", this);

    mainLayout->addWidget(brightnessLabel);
    mainLayout->addWidget(brightnessSlider_);
    mainLayout->addWidget(brightnessApplyButton_);

    // Contrast slider and apply button
    QLabel* contrastLabel = new QLabel("Contraste", this);
    contrastSlider_ = new QSlider(Qt::Horizontal, this);
    contrastSlider_->setRange(0, 200);
    contrastSlider_->setValue(100);
    contrastApplyButton_ = new QPushButton("Aplicar Contraste", this);

    mainLayout->addWidget(contrastLabel);
    mainLayout->addWidget(contrastSlider_);
    mainLayout->addWidget(contrastApplyButton_);

    // Blur slider and apply button
    QLabel* blurLabel = new QLabel("Desenfoque", this);
    blurSlider_ = new QSlider(Qt::Horizontal, this);
    blurSlider_->setRange(0, 200);
    blurSlider_->setValue(100);
    blurApplyButton_ = new QPushButton("Aplicar Desenfoque", this);

    mainLayout->addWidget(blurLabel);
    mainLayout->addWidget(blurSlider_);
    mainLayout->addWidget(blurApplyButton_);

    // Sharpen slider and apply button
    QLabel* sharpenLabel = new QLabel("Nitidez", this);
    sharpenSlider_ = new QSlider(Qt::Horizontal, this);
    sharpenSlider_->setRange(0, 200);
    sharpenSlider_->setValue(100);
    sharpenApplyButton_ = new QPushButton("Aplicar Nitidez", this);

    mainLayout->addWidget(sharpenLabel);
    mainLayout->addWidget(sharpenSlider_);
    mainLayout->addWidget(sharpenApplyButton_);

    setLayout(mainLayout);
}

void FilterPanel::setupConnections() {
    connect(grayscaleButton_, &QPushButton::clicked, this, &FilterPanel::onGrayscaleClicked);
    connect(negativeButton_, &QPushButton::clicked, this, &FilterPanel::onNegativeClicked);
    connect(brightnessApplyButton_, &QPushButton::clicked, this, &FilterPanel::onBrightnessApplyClicked);
    connect(contrastApplyButton_, &QPushButton::clicked, this, &FilterPanel::onContrastApplyClicked);
    connect(blurApplyButton_, &QPushButton::clicked, this, &FilterPanel::onBlurApplyClicked);
    connect(sharpenApplyButton_, &QPushButton::clicked, this, &FilterPanel::onSharpenApplyClicked);
}

void FilterPanel::onGrayscaleClicked() {
    auto filter = std::make_shared<filters::GrayscaleFilter>();
    emit filterApplied(filter);
}

void FilterPanel::onNegativeClicked() {
    auto filter = std::make_shared<filters::NegativeFilter>();
    emit filterApplied(filter);
}

void FilterPanel::onBrightnessApplyClicked() {
    auto filter = std::make_shared<filters::BrightnessFilter>();
    filter->setFactor(brightnessSlider_->value() / 100.0);
    emit filterApplied(filter);
}

void FilterPanel::onContrastApplyClicked() {
    auto filter = std::make_shared<filters::ContrastFilter>();
    filter->setFactor(contrastSlider_->value() / 100.0);
    emit filterApplied(filter);
}

void FilterPanel::onBlurApplyClicked() {
    auto filter = std::make_shared<filters::BlurFilter>();
    int kernelSize = blurSlider_->value();
    if (kernelSize % 2 == 0) {
        kernelSize += 1; // ensure odd kernel size
    }
    filter->setKernelSize(kernelSize);
    emit filterApplied(filter);
}

void FilterPanel::onSharpenApplyClicked() {
    auto filter = std::make_shared<filters::SharpenFilter>();
    filter->setFactor(sharpenSlider_->value() / 100.0);
    emit filterApplied(filter);
}

} // namespace gui
} // namespace escomeditor
