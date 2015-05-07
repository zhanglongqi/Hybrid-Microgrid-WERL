#include "pvcontrol.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    pvControl w;
    w.show();

    return a.exec();
}
