#include "BlurFilter.h"

namespace escomeditor {
namespace filters {

BlurFilter::BlurFilter()
    : Filter("Desenfoque"), _kernelSize(5) {}

void BlurFilter::apply(core::Image& image) {
    cv::Mat cvImage = image.getCvImage();
    if (cvImage.empty()) return;

    cv::Mat blurred;
    cv::GaussianBlur(cvImage, blurred, cv::Size(_kernelSize, _kernelSize), 0);

    image.updateFromCv(blurred);
}

void BlurFilter::setKernelSize(int size) {
    if (size % 2 == 0) {
        size += 1; // ensure odd kernel size
    }
    _kernelSize = size;
}

int BlurFilter::getKernelSize() const {
    return _kernelSize;
}

} // namespace filters
} // namespace escomeditor
