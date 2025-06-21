#include "NegativeFilter.h"

namespace escomeditor {
namespace filters {

NegativeFilter::NegativeFilter()
    : Filter("Negativo") {}

void NegativeFilter::apply(core::Image& image) {
    cv::Mat cvImage = image.getCvImage();
    if (cvImage.empty()) return;

    cv::Mat negativeImage = cv::Scalar::all(255) - cvImage;

    image.updateFromCv(negativeImage);
}

} // namespace filters
} // namespace escomeditor
