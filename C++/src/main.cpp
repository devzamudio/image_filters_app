#include <QApplication>
#include "gui/MainWindow.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    escomeditor::gui::MainWindow mainWindow;
    mainWindow.show();

    return app.exec();
}
