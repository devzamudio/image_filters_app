# ESCOM-Editor C++ Port

## Overview

This is the C++ port of the ESCOM-Editor image editing application originally developed in Python. The application supports basic image editing features such as opening, saving, resizing, cropping, rotating, and applying filters like grayscale, brightness, contrast, blur, sharpen, and negative.

## Libraries Used

- **OpenCV**: For image loading, saving, and processing.
- **Qt (C++ version)**: For the graphical user interface.

## Project Structure

- `src/core/`: Core image handling classes.
- `src/filters/`: Image filter implementations.
- `src/gui/`: GUI components including main window, toolbar, filter panel, and image view.

## Building the Project

### Prerequisites

- C++17 compatible compiler (e.g., g++)
- CMake 3.15 or higher
- OpenCV 4.x
- Qt 6.x or Qt 5.x (Qt Widgets module)

### Installing Dependencies on Ubuntu

```bash
sudo apt update
sudo apt install build-essential cmake qtbase5-dev libopencv-dev
```

### Installing Dependencies on Fedora

```bash
sudo dnf install @development-tools cmake qt5-qtbase-devel opencv-devel
```

### Installing Dependencies on Arch Linux

```bash
sudo pacman -S base-devel cmake qt5-base opencv
```

### Installing Dependencies on openSUSE

```bash
sudo zypper install -t pattern devel_C_C++ cmake libqt5-qtbase-devel opencv-devel
```
sudo pacman -S base-devel cmake qt5-base opencv
sudo dnf install @development-tools cmake qt5-qtbase-devel opencv-devel

### Build Steps

```bash
mkdir build
cd build
cmake ..
make
```

### Running the Application

After building, run the executable:

```bash
./escomeditor
```

## Setting Up Visual Studio Code

1. Install the C/C++ extension by Microsoft.
2. Install the CMake Tools extension.
3. Configure your `c_cpp_properties.json` to include OpenCV and Qt include paths.
4. Use the CMake Tools extension to configure, build, and debug the project.

## Testing the Application

- Open an image file using the toolbar.
- Apply filters from the filter panel.
- Save the edited image.
- Use undo/redo functionality.
- Verify zoom and fit-to-window features.

## Notes

- The application replicates the Python version's functionality using OpenCV and Qt.
- Undo/redo history is implemented in the Image class.
- Filters are implemented as classes inheriting from a base Filter class.
