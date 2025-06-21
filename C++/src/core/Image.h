#ifndef ESCOMEDITOR_CORE_IMAGE_H
#define ESCOMEDITOR_CORE_IMAGE_H

#include <string>
#include <vector>
#include <opencv2/opencv.hpp>

namespace escomeditor {
namespace core {

class Image {
public:
    Image();
    ~Image();

    bool load(const std::string& filepath);
    bool save(const std::string& filepath) const;

    cv::Mat getCvImage() const;
    void updateFromCv(const cv::Mat& image);

    std::string getFilename() const;
    std::pair<int, int> getSize() const;
    bool isModified() const;

    bool canUndo() const;
    bool canRedo() const;
    bool undo();
    bool redo();

private:
    void addToHistory(const cv::Mat& image);

    cv::Mat _cvImage;
    std::string _filename;
    bool _modified;

    std::vector<cv::Mat> _history;
    int _currentIndex;
    const int _maxHistory = 20;
};

} // namespace core
} // namespace escomeditor

#endif // ESCOMEDITOR_CORE_IMAGE_H
