#ifndef ESCOMEDITOR_FILTERS_FILTER_H
#define ESCOMEDITOR_FILTERS_FILTER_H

#include <string>
#include "../core/Image.h"

namespace escomeditor {
namespace filters {

class Filter {
public:
    Filter(const std::string& name);
    virtual ~Filter() = default;

    virtual void apply(core::Image& image) = 0;

    std::string getName() const;

protected:
    std::string _name;
};

} // namespace filters
} // namespace escomeditor

#endif // ESCOMEDITOR_FILTERS_FILTER_H
