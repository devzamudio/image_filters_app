#ifndef ESCOMEDITOR_FILTERS_BLURFILTER_H
#define ESCOMEDITOR_FILTERS_BLURFILTER_H

#include "Filter.h"
#include <opencv2/opencv.hpp>

namespace escomeditor {
namespace filters {

class BlurFilter : public Filter {
public:
    BlurFilter();
    void apply(core::Image& image) override;

    void setKernelSize(int size);
    int getKernelSize() const;

private:
    int _kernelSize; // must be odd
};

} // namespace filters
} // namespace escomeditor

#endif // ESCOMEDITOR_FILTERS_BLURFILTER_H
