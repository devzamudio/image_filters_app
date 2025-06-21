#ifndef ESCOMEDITOR_FILTERS_NEGATIVEFILTER_H
#define ESCOMEDITOR_FILTERS_NEGATIVEFILTER_H

#include "Filter.h"
#include <opencv2/opencv.hpp>

namespace escomeditor {
namespace filters {

class NegativeFilter : public Filter {
public:
    NegativeFilter();
    void apply(core::Image& image) override;
};

} // namespace filters
} // namespace escomeditor

#endif // ESCOMEDITOR_FILTERS_NEGATIVEFILTER_H
