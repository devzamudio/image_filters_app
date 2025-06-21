#ifndef ESCOMEDITOR_FILTERS_GRAYSCALEFILTER_H
#define ESCOMEDITOR_FILTERS_GRAYSCALEFILTER_H

#include "Filter.h"
#include <opencv2/opencv.hpp>

namespace escomeditor {
namespace filters {

class GrayscaleFilter : public Filter {
public:
    GrayscaleFilter();
    void apply(core::Image& image) override;
};

} // namespace filters
} // namespace escomeditor

#endif // ESCOMEDITOR_FILTERS_GRAYSCALEFILTER_H
