#include "battery1control.h"
#include "ui_battery1control.h"

battery1Control::battery1Control(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::battery1Control)
{
    ui->setupUi(this);
}

battery1Control::~battery1Control()
{
    delete ui;
}
