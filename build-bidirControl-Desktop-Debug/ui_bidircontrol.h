/********************************************************************************
** Form generated from reading UI file 'bidircontrol.ui'
**
** Created by: Qt User Interface Compiler version 5.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_BIDIRCONTROL_H
#define UI_BIDIRCONTROL_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDial>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_bidirControl
{
public:
    QPushButton *bidir_start_pb;
    QPushButton *bidir_apply_pb;
    QTabWidget *tabWidget;
    QWidget *tab_bus;
    QLabel *label_35;
    QLabel *label_25;
    QLabel *label_28;
    QDial *dial_4;
    QLabel *label_36;
    QSpinBox *spinBox_4;
    QLabel *vdc_ref_bus;
    QDial *dial_3;
    QLabel *label_27;
    QSpinBox *spinBox_3;
    QLabel *label_33;
    QLabel *label_26;
    QLabel *label_41;
    QLabel *iq_ref_bus;
    QWidget *tab_pow;
    QLabel *label_29;
    QDial *dial_id_ref_pow;
    QLabel *label_set_ref_current;
    QLabel *label_37;
    QLabel *id_ref_pow;
    QDial *dial_iq_ref_pow;
    QLabel *label_30;
    QLabel *label_39;
    QLabel *label_40;
    QSpinBox *spinBox;
    QLabel *iq_ref_pow;
    QSpinBox *spinBox_2;
    QLabel *label_34;
    QLabel *label_38;
    QLabel *label_42;
    QLabel *label_title;

    void setupUi(QWidget *bidirControl)
    {
        if (bidirControl->objectName().isEmpty())
            bidirControl->setObjectName(QStringLiteral("bidirControl"));
        bidirControl->resize(380, 480);
        bidir_start_pb = new QPushButton(bidirControl);
        bidir_start_pb->setObjectName(QStringLiteral("bidir_start_pb"));
        bidir_start_pb->setEnabled(false);
        bidir_start_pb->setGeometry(QRect(170, 180, 71, 61));
        QFont font;
        font.setPointSize(14);
        font.setBold(true);
        font.setWeight(75);
        bidir_start_pb->setFont(font);
        bidir_start_pb->setStyleSheet(QStringLiteral("color: rgb(0, 0, 0);"));
        bidir_apply_pb = new QPushButton(bidirControl);
        bidir_apply_pb->setObjectName(QStringLiteral("bidir_apply_pb"));
        bidir_apply_pb->setGeometry(QRect(60, 180, 71, 61));
        QFont font1;
        font1.setPointSize(14);
        font1.setBold(true);
        font1.setItalic(false);
        font1.setWeight(75);
        bidir_apply_pb->setFont(font1);
        bidir_apply_pb->setCursor(QCursor(Qt::PointingHandCursor));
        bidir_apply_pb->setStyleSheet(QStringLiteral("color: rgb(0, 0, 0);"));
        tabWidget = new QTabWidget(bidirControl);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tabWidget->setGeometry(QRect(5, 250, 371, 191));
        QFont font2;
        font2.setPointSize(11);
        font2.setBold(true);
        font2.setWeight(75);
        tabWidget->setFont(font2);
        tabWidget->setStyleSheet(QStringLiteral("color: rgb(0, 0, 0);"));
        tab_bus = new QWidget();
        tab_bus->setObjectName(QStringLiteral("tab_bus"));
        label_35 = new QLabel(tab_bus);
        label_35->setObjectName(QStringLiteral("label_35"));
        label_35->setGeometry(QRect(290, 30, 20, 16));
        QFont font3;
        font3.setPointSize(10);
        font3.setBold(true);
        font3.setWeight(75);
        label_35->setFont(font3);
        label_25 = new QLabel(tab_bus);
        label_25->setObjectName(QStringLiteral("label_25"));
        label_25->setGeometry(QRect(40, 130, 50, 16));
        label_25->setFont(font3);
        label_28 = new QLabel(tab_bus);
        label_28->setObjectName(QStringLiteral("label_28"));
        label_28->setGeometry(QRect(100, 130, 50, 16));
        label_28->setFont(font3);
        dial_4 = new QDial(tab_bus);
        dial_4->setObjectName(QStringLiteral("dial_4"));
        dial_4->setGeometry(QRect(40, 50, 91, 81));
        dial_4->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        dial_4->setMinimum(-3000);
        dial_4->setMaximum(3000);
        label_36 = new QLabel(tab_bus);
        label_36->setObjectName(QStringLiteral("label_36"));
        label_36->setGeometry(QRect(240, 10, 100, 16));
        label_36->setFont(font3);
        spinBox_4 = new QSpinBox(tab_bus);
        spinBox_4->setObjectName(QStringLiteral("spinBox_4"));
        spinBox_4->setGeometry(QRect(310, 60, 20, 61));
        spinBox_4->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        spinBox_4->setMaximum(400);
        vdc_ref_bus = new QLabel(tab_bus);
        vdc_ref_bus->setObjectName(QStringLiteral("vdc_ref_bus"));
        vdc_ref_bus->setGeometry(QRect(70, 30, 31, 16));
        vdc_ref_bus->setFont(font3);
        vdc_ref_bus->setAlignment(Qt::AlignCenter);
        dial_3 = new QDial(tab_bus);
        dial_3->setObjectName(QStringLiteral("dial_3"));
        dial_3->setGeometry(QRect(220, 50, 91, 81));
        dial_3->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        dial_3->setMaximum(400);
        dial_3->setValue(380);
        dial_3->setTracking(true);
        label_27 = new QLabel(tab_bus);
        label_27->setObjectName(QStringLiteral("label_27"));
        label_27->setGeometry(QRect(280, 130, 31, 16));
        label_27->setFont(font3);
        spinBox_3 = new QSpinBox(tab_bus);
        spinBox_3->setObjectName(QStringLiteral("spinBox_3"));
        spinBox_3->setGeometry(QRect(130, 60, 20, 61));
        spinBox_3->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        spinBox_3->setMinimum(-3000);
        spinBox_3->setMaximum(3000);
        label_33 = new QLabel(tab_bus);
        label_33->setObjectName(QStringLiteral("label_33"));
        label_33->setGeometry(QRect(40, 10, 110, 16));
        label_33->setFont(font3);
        label_26 = new QLabel(tab_bus);
        label_26->setObjectName(QStringLiteral("label_26"));
        label_26->setGeometry(QRect(220, 130, 31, 16));
        label_26->setFont(font3);
        label_41 = new QLabel(tab_bus);
        label_41->setObjectName(QStringLiteral("label_41"));
        label_41->setGeometry(QRect(110, 30, 20, 16));
        label_41->setFont(font3);
        iq_ref_bus = new QLabel(tab_bus);
        iq_ref_bus->setObjectName(QStringLiteral("iq_ref_bus"));
        iq_ref_bus->setGeometry(QRect(250, 30, 31, 16));
        iq_ref_bus->setFont(font3);
        iq_ref_bus->setAlignment(Qt::AlignCenter);
        tabWidget->addTab(tab_bus, QString());
        tab_pow = new QWidget();
        tab_pow->setObjectName(QStringLiteral("tab_pow"));
        label_29 = new QLabel(tab_pow);
        label_29->setObjectName(QStringLiteral("label_29"));
        label_29->setGeometry(QRect(100, 130, 31, 16));
        label_29->setFont(font3);
        dial_id_ref_pow = new QDial(tab_pow);
        dial_id_ref_pow->setObjectName(QStringLiteral("dial_id_ref_pow"));
        dial_id_ref_pow->setGeometry(QRect(40, 50, 91, 81));
        dial_id_ref_pow->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        dial_id_ref_pow->setMinimum(-3000);
        dial_id_ref_pow->setMaximum(3000);
        label_set_ref_current = new QLabel(tab_pow);
        label_set_ref_current->setObjectName(QStringLiteral("label_set_ref_current"));
        label_set_ref_current->setGeometry(QRect(40, 40, 131, 21));
        label_set_ref_current->setFont(font2);
        label_set_ref_current->setStyleSheet(QStringLiteral("color: rgb(255, 255, 255);"));
        label_37 = new QLabel(tab_pow);
        label_37->setObjectName(QStringLiteral("label_37"));
        label_37->setGeometry(QRect(280, 130, 31, 16));
        label_37->setFont(font3);
        id_ref_pow = new QLabel(tab_pow);
        id_ref_pow->setObjectName(QStringLiteral("id_ref_pow"));
        id_ref_pow->setGeometry(QRect(70, 30, 31, 16));
        id_ref_pow->setFont(font3);
        id_ref_pow->setAlignment(Qt::AlignCenter);
        dial_iq_ref_pow = new QDial(tab_pow);
        dial_iq_ref_pow->setObjectName(QStringLiteral("dial_iq_ref_pow"));
        dial_iq_ref_pow->setGeometry(QRect(220, 50, 91, 81));
        dial_iq_ref_pow->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        dial_iq_ref_pow->setMaximum(400);
        dial_iq_ref_pow->setValue(380);
        dial_iq_ref_pow->setTracking(true);
        label_30 = new QLabel(tab_pow);
        label_30->setObjectName(QStringLiteral("label_30"));
        label_30->setGeometry(QRect(40, 130, 31, 16));
        label_30->setFont(font3);
        label_39 = new QLabel(tab_pow);
        label_39->setObjectName(QStringLiteral("label_39"));
        label_39->setGeometry(QRect(50, 10, 100, 16));
        label_39->setFont(font3);
        label_40 = new QLabel(tab_pow);
        label_40->setObjectName(QStringLiteral("label_40"));
        label_40->setGeometry(QRect(240, 10, 100, 16));
        label_40->setFont(font3);
        spinBox = new QSpinBox(tab_pow);
        spinBox->setObjectName(QStringLiteral("spinBox"));
        spinBox->setGeometry(QRect(130, 60, 20, 61));
        spinBox->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        spinBox->setMinimum(-3000);
        spinBox->setMaximum(3000);
        iq_ref_pow = new QLabel(tab_pow);
        iq_ref_pow->setObjectName(QStringLiteral("iq_ref_pow"));
        iq_ref_pow->setGeometry(QRect(250, 30, 31, 16));
        iq_ref_pow->setFont(font3);
        iq_ref_pow->setAlignment(Qt::AlignCenter);
        spinBox_2 = new QSpinBox(tab_pow);
        spinBox_2->setObjectName(QStringLiteral("spinBox_2"));
        spinBox_2->setGeometry(QRect(310, 60, 20, 61));
        spinBox_2->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        spinBox_2->setMaximum(400);
        label_34 = new QLabel(tab_pow);
        label_34->setObjectName(QStringLiteral("label_34"));
        label_34->setGeometry(QRect(220, 130, 31, 16));
        label_34->setFont(font3);
        label_38 = new QLabel(tab_pow);
        label_38->setObjectName(QStringLiteral("label_38"));
        label_38->setGeometry(QRect(100, 30, 20, 16));
        label_38->setFont(font3);
        label_42 = new QLabel(tab_pow);
        label_42->setObjectName(QStringLiteral("label_42"));
        label_42->setGeometry(QRect(290, 30, 20, 16));
        label_42->setFont(font3);
        tabWidget->addTab(tab_pow, QString());
        label_title = new QLabel(bidirControl);
        label_title->setObjectName(QStringLiteral("label_title"));
        label_title->setGeometry(QRect(0, 0, 381, 41));
        QFont font4;
        font4.setPointSize(20);
        font4.setBold(true);
        font4.setUnderline(false);
        font4.setWeight(75);
        label_title->setFont(font4);
        label_title->setLayoutDirection(Qt::LeftToRight);
        label_title->setStyleSheet(QLatin1String("color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0);"));
        label_title->setAlignment(Qt::AlignCenter);

        retranslateUi(bidirControl);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(bidirControl);
    } // setupUi

    void retranslateUi(QWidget *bidirControl)
    {
        bidirControl->setWindowTitle(QApplication::translate("bidirControl", "bidirControl", 0));
        bidir_start_pb->setText(QApplication::translate("bidirControl", "Start", 0));
        bidir_apply_pb->setText(QApplication::translate("bidirControl", "Apply", 0));
        label_35->setText(QApplication::translate("bidirControl", "A", 0));
        label_25->setText(QApplication::translate("bidirControl", "300 V", 0));
        label_28->setText(QApplication::translate("bidirControl", "400 V", 0));
        label_36->setText(QApplication::translate("bidirControl", "Iq Reference:", 0));
        vdc_ref_bus->setText(QApplication::translate("bidirControl", "380", 0));
        label_27->setText(QApplication::translate("bidirControl", "10 A", 0));
        label_33->setText(QApplication::translate("bidirControl", "Vdc Reference:", 0));
        label_26->setText(QApplication::translate("bidirControl", "-10 A", 0));
        label_41->setText(QApplication::translate("bidirControl", "V", 0));
        iq_ref_bus->setText(QApplication::translate("bidirControl", "0", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab_bus), QApplication::translate("bidirControl", "Bus Monitoring Mode", 0));
        label_29->setText(QApplication::translate("bidirControl", "10 A", 0));
        label_set_ref_current->setText(QApplication::translate("bidirControl", "Set Ref Current:", 0));
        label_37->setText(QApplication::translate("bidirControl", "10 A", 0));
        id_ref_pow->setText(QApplication::translate("bidirControl", "0", 0));
        label_30->setText(QApplication::translate("bidirControl", "-10 A", 0));
        label_39->setText(QApplication::translate("bidirControl", "Id Reference:", 0));
        label_40->setText(QApplication::translate("bidirControl", "Iq Reference:", 0));
        iq_ref_pow->setText(QApplication::translate("bidirControl", "0", 0));
        label_34->setText(QApplication::translate("bidirControl", "-10 A", 0));
        label_38->setText(QApplication::translate("bidirControl", "A", 0));
        label_42->setText(QApplication::translate("bidirControl", "A", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab_pow), QApplication::translate("bidirControl", "Power Dispatching Mode", 0));
        label_title->setText(QApplication::translate("bidirControl", "BIDIRECTIONAL CONTROL", 0));
    } // retranslateUi

};

namespace Ui {
    class bidirControl: public Ui_bidirControl {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_BIDIRCONTROL_H
