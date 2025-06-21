#include "ToolBar.h"
#include <QIcon>

namespace escomeditor {
namespace gui {

ToolBar::ToolBar(QWidget* parent)
    : QToolBar(parent)
{
    openAct_ = addAction(QIcon::fromTheme("document-open"), tr("Open"));
    saveAct_ = addAction(QIcon::fromTheme("document-save"), tr("Save"));
    zoomInAct_ = addAction(QIcon::fromTheme("zoom-in"), tr("Zoom In"));
    zoomOutAct_ = addAction(QIcon::fromTheme("zoom-out"), tr("Zoom Out"));
    fitToWindowAct_ = addAction(QIcon::fromTheme("zoom-fit-best"), tr("Fit to Window"));

    connect(openAct_, &QAction::triggered, this, &ToolBar::openAction);
    connect(saveAct_, &QAction::triggered, this, &ToolBar::saveAction);
    connect(zoomInAct_, &QAction::triggered, this, &ToolBar::zoomInAction);
    connect(zoomOutAct_, &QAction::triggered, this, &ToolBar::zoomOutAction);
    connect(fitToWindowAct_, &QAction::triggered, this, &ToolBar::fitToWindowAction);

    enableImageActions(false);
}

void ToolBar::enableImageActions(bool enabled) {
    saveAct_->setEnabled(enabled);
    zoomInAct_->setEnabled(enabled);
    zoomOutAct_->setEnabled(enabled);
    fitToWindowAct_->setEnabled(enabled);
}

} // namespace gui
} // namespace escomeditor
