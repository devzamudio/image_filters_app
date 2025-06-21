#include "GrayscaleFilter.h"
#include <opencv2/imgproc.hpp>

namespace escomeditor {
namespace filters {

GrayscaleFilter::GrayscaleFilter() : Filter("Grayscale") {}

void GrayscaleFilter::apply(core::Image& image) {
    cv::Mat cvImage = image.getCvImage();
    if (cvImage.empty()) return;

    cv::Mat gray;
    cv::cvtColor(cvImage, gray, cv::COLOR_BGR2GRAY);
    cv::cvtColor(gray, cvImage, cv::COLOR_GRAY2BGR);

    image.updateFromCv(cvImage);
}

} // namespace filters
} // namespace escomeditor
