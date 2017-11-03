#include "bidircontrol.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    bidirControl w;
    w.show();

    return a.exec();
}
