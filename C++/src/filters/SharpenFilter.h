#ifndef ESCOMEDITOR_FILTERS_SHARPENFILTER_H
#define ESCOMEDITOR_FILTERS_SHARPENFILTER_H

#include "Filter.h"
#include <opencv2/opencv.hpp>

namespace escomeditor {
namespace filters {

class SharpenFilter : public Filter {
public:
    SharpenFilter();
    void apply(core::Image& image) override;

    void setFactor(double factor);
    double getFactor() const;

private:
    double _factor; // sharpening intensity
};

} // namespace filters
} // namespace escomeditor

#endif // ESCOMEDITOR_FILTERS_SHARPENFILTER_H
