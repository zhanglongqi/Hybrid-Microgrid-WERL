#include "battery1control.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    battery1Control w;
    w.show();

    return a.exec();
}
