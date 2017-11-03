#include "pvcontrol.h"
#include "ui_pvcontrol.h"

pvControl::pvControl(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::pvControl)
{
    ui->setupUi(this);
}

pvControl::~pvControl()
{
    delete ui;
}
