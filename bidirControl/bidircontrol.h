#ifndef BIDIRCONTROL_H
#define BIDIRCONTROL_H

#include <QWidget>

namespace Ui {
class bidirControl;
}

class bidirControl : public QWidget
{
    Q_OBJECT

public:
    explicit bidirControl(QWidget *parent = 0);
    ~bidirControl();

private:
    Ui::bidirControl *ui;
};

#endif // BIDIRCONTROL_H
