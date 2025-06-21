#include "Image.h"
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

namespace escomeditor {
namespace core {

Image::Image()
    : _modified(false), _currentIndex(-1) {}

Image::~Image() {}

bool Image::load(const std::string& filepath) {
    cv::Mat img = cv::imread(filepath, cv::IMREAD_COLOR);
    if (img.empty()) {
        std::cerr << "Error loading image: " << filepath << std::endl;
        return false;
    }
    _cvImage = img;
    _filename = filepath;
    _modified = false;
    _history.clear();
    _currentIndex = -1;
    addToHistory(_cvImage.clone());
    return true;
}

bool Image::save(const std::string& filepath) const {
    if (_cvImage.empty()) {
        std::cerr << "No image to save." << std::endl;
        return false;
    }
    bool success = cv::imwrite(filepath, _cvImage);
    if (!success) {
        std::cerr << "Error saving image: " << filepath << std::endl;
    }
    return success;
}

cv::Mat Image::getCvImage() const {
    return _cvImage;
}

void Image::updateFromCv(const cv::Mat& image) {
    _cvImage = image.clone();
    _modified = true;
    addToHistory(_cvImage.clone());
}

std::string Image::getFilename() const {
    return _filename;
}

std::pair<int, int> Image::getSize() const {
    if (_cvImage.empty()) {
        return {0, 0};
    }
    return {_cvImage.cols, _cvImage.rows};
}

bool Image::isModified() const {
    return _modified;
}

void Image::addToHistory(const cv::Mat& image) {
    if (_currentIndex < static_cast<int>(_history.size()) - 1) {
        _history.erase(_history.begin() + _currentIndex + 1, _history.end());
    }
    if (_history.empty()) {
        _history.push_back(image);
        _currentIndex++;
    } else {
        cv::Mat diff;
        cv::absdiff(_history.back(), image, diff);
        std::vector<cv::Mat> channels;
        cv::split(diff, channels);
        cv::Mat diffGray = cv::Mat::zeros(diff.size(), CV_8UC1);
        for (const auto& ch : channels) {
            diffGray |= ch;
        }
        if (cv::countNonZero(diffGray) > 0) {
            _history.push_back(image);
            _currentIndex++;
            if (static_cast<int>(_history.size()) > _maxHistory) {
                _history.erase(_history.begin());
                _currentIndex--;
            }
        }
    }
}

bool Image::canUndo() const {
    return _currentIndex > 0;
}

bool Image::canRedo() const {
    return _currentIndex < static_cast<int>(_history.size()) - 1;
}

bool Image::undo() {
    if (!canUndo()) {
        return false;
    }
    _currentIndex--;
    _cvImage = _history[_currentIndex].clone();
    _modified = true;
    return true;
}

bool Image::redo() {
    if (!canRedo()) {
        return false;
    }
    _currentIndex++;
    _cvImage = _history[_currentIndex].clone();
    _modified = true;
    return true;
}

} // namespace core
} // namespace escomeditor
