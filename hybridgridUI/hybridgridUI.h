#ifndef HYBRIDGRIDUI_H
#define HYBRIDGRIDUI_H

#include <QWidget>

namespace Ui {
class hybridgridUI;
}

class hybridgridUI : public QWidget
{
    Q_OBJECT

public:
    explicit hybridgridUI(QWidget *parent = 0);
    ~hybridgridUI();

private:
    Ui::hybridgridUI *ui;
};

#endif // HYBRIDGRIDUI_H
