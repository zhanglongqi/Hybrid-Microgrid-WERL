#ifndef BATTERY1CONTROL_H
#define BATTERY1CONTROL_H

#include <QWidget>

namespace Ui {
class battery1Control;
}

class battery1Control : public QWidget
{
    Q_OBJECT

public:
    explicit battery1Control(QWidget *parent = 0);
    ~battery1Control();

private:
    Ui::battery1Control *ui;
};

#endif // BATTERY1CONTROL_H
