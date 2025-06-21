#ifndef ESCOMEDITOR_GUI_TOOLBAR_H
#define ESCOMEDITOR_GUI_TOOLBAR_H

#include <QWidget>
#include <QToolBar>
#include <QAction>

namespace escomeditor {
namespace gui {

class ToolBar : public QToolBar {
    Q_OBJECT
public:
    explicit ToolBar(QWidget* parent = nullptr);

    void enableImageActions(bool enabled);

signals:
    void openAction();
    void saveAction();
    void zoomInAction();
    void zoomOutAction();
    void fitToWindowAction();

private:
    QAction* openAct_;
    QAction* saveAct_;
    QAction* zoomInAct_;
    QAction* zoomOutAct_;
    QAction* fitToWindowAct_;
};

} // namespace gui
} // namespace escomeditor

#endif // ESCOMEDITOR_GUI_TOOLBAR_H
