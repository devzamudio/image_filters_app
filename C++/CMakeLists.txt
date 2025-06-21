cmake_minimum_required(VERSION 3.15)
project(escomeditor)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)
find_package(Qt6 COMPONENTS Widgets REQUIRED)

set(SOURCES
    src/core/Image.cpp
    src/filters/Filter.cpp
    src/filters/GrayscaleFilter.cpp
    src/filters/BrightnessFilter.cpp
    src/filters/ContrastFilter.cpp
    src/filters/BlurFilter.cpp
    src/filters/SharpenFilter.cpp
    src/filters/NegativeFilter.cpp
    src/gui/MainWindow.cpp
    src/gui/ToolBar.cpp
    src/gui/FilterPanel.cpp
    src/gui/ImageView.cpp
    src/main.cpp
)

set(HEADERS
    src/core/Image.h
    src/filters/Filter.h
    src/filters/GrayscaleFilter.h
    src/filters/BrightnessFilter.h
    src/filters/ContrastFilter.h
    src/filters/BlurFilter.h
    src/filters/SharpenFilter.h
    src/filters/NegativeFilter.h
    src/gui/MainWindow.h
    src/gui/ToolBar.h
    src/gui/FilterPanel.h
    src/gui/ImageView.h
)

qt_wrap_cpp(MOC_SOURCES
    ${HEADERS}
)

add_executable(escomeditor ${SOURCES} ${MOC_SOURCES})

target_include_directories(escomeditor PRIVATE ${OpenCV_INCLUDE_DIRS} ${Qt6Widgets_INCLUDE_DIRS} src)

target_link_libraries(escomeditor PRIVATE ${OpenCV_LIBS} Qt6::Widgets)
