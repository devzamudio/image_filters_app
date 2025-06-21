#include "SharpenFilter.h"

namespace escomeditor {
namespace filters {

SharpenFilter::SharpenFilter()
    : Filter("Nitidez"), _factor(1.5) {}

void SharpenFilter::apply(core::Image& image) {
    cv::Mat cvImage = image.getCvImage();
    if (cvImage.empty()) return;

    cv::Mat blurred;
    cv::GaussianBlur(cvImage, blurred, cv::Size(0, 0), 3);
    cv::Mat sharpened;
    cv::addWeighted(cvImage, 1 + _factor, blurred, -_factor, 0, sharpened);

    image.updateFromCv(sharpened);
}

void SharpenFilter::setFactor(double factor) {
    _factor = factor;
}

double SharpenFilter::getFactor() const {
    return _factor;
}

} // namespace filters
} // namespace escomeditor
