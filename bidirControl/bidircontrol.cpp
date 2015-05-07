#include "bidircontrol.h"
#include "ui_bidircontrol.h"

bidirControl::bidirControl(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::bidirControl)
{
    ui->setupUi(this);
}

bidirControl::~bidirControl()
{
    delete ui;
}
