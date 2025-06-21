#include "BrightnessFilter.h"
#include <opencv2/imgproc.hpp>

namespace escomeditor {
namespace filters {

BrightnessFilter::BrightnessFilter()
    : Filter("Brillo"), _factor(1.0) {}

void BrightnessFilter::apply(core::Image& image) {
    cv::Mat cvImage = image.getCvImage();
    if (cvImage.empty()) return;

    cv::Mat newImage;
    cvImage.convertTo(newImage, -1, _factor, 0); // alpha = factor, beta = 0

    image.updateFromCv(newImage);
}

void BrightnessFilter::setFactor(double factor) {
    _factor = factor;
}

double BrightnessFilter::getFactor() const {
    return _factor;
}

} // namespace filters
} // namespace escomeditor
