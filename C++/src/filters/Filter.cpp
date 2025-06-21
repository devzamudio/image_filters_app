#include "Filter.h"

namespace escomeditor {
namespace filters {

Filter::Filter(const std::string& name) : _name(name) {}

std::string Filter::getName() const {
    return _name;
}

} // namespace filters
} // namespace escomeditor
