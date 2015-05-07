#include "hybridgridUI.h"
#include "ui_hybridgridUI.h"

hybridgridUI::hybridgridUI(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::hybridgridUI)
{
    ui->setupUi(this);
}

hybridgridUI::~hybridgridUI()
{
    delete ui;
}
