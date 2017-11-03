#ifndef PVCONTROL_H
#define PVCONTROL_H

#include <QWidget>

namespace Ui {
class pvControl;
}

class pvControl : public QWidget
{
    Q_OBJECT

public:
    explicit pvControl(QWidget *parent = 0);
    ~pvControl();

private:
    Ui::pvControl *ui;
};

#endif // PVCONTROL_H
