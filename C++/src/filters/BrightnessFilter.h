#ifndef ESCOMEDITOR_FILTERS_BRIGHTNESSFILTER_H
#define ESCOMEDITOR_FILTERS_BRIGHTNESSFILTER_H

#include "Filter.h"
#include <opencv2/opencv.hpp>

namespace escomeditor {
namespace filters {

class BrightnessFilter : public Filter {
public:
    BrightnessFilter();
    void apply(core::Image& image) override;

    void setFactor(double factor);
    double getFactor() const;

private:
    double _factor; // 1.0 = no change
};

} // namespace filters
} // namespace escomeditor

#endif // ESCOMEDITOR_FILTERS_BRIGHTNESSFILTER_H
