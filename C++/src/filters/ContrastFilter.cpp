#include "ContrastFilter.h"

namespace escomeditor {
namespace filters {

ContrastFilter::ContrastFilter()
    : Filter("Contraste"), _factor(1.0) {}

void ContrastFilter::apply(core::Image& image) {
    cv::Mat cvImage = image.getCvImage();
    if (cvImage.empty()) return;

    cv::Mat newImage;
    // Adjust contrast: new_image = alpha*image + beta
    // Here, alpha = factor, beta = 128*(1 - factor) to keep midtones stable
    double beta = 128 * (1.0 - _factor);
    cvImage.convertTo(newImage, -1, _factor, beta);

    image.updateFromCv(newImage);
}

void ContrastFilter::setFactor(double factor) {
    _factor = factor;
}

double ContrastFilter::getFactor() const {
    return _factor;
}

} // namespace filters
} // namespace escomeditor
