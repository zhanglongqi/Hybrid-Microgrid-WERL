/********************************************************************************
** Form generated from reading UI file 'battery1control.ui'
**
** Created by: Qt User Interface Compiler version 5.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_BATTERY1CONTROL_H
#define UI_BATTERY1CONTROL_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDial>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_battery1Control
{
public:
    QLabel *label_title;
    QLabel *label_op_state;
    QSpinBox *spinBox;
    QLabel *batt1_control_mode;
    QPushButton *batt1_apply_current_pb;
    QDial *dial;
    QLabel *label_control;
    QLabel *batt1_operating_state;
    QLabel *batt1_set_ref_voltage;
    QSpinBox *spinBox_2;
    QLabel *batt1_ref_voltage;
    QPushButton *batt1_apply_voltage_pb;
    QLabel *batt1_set_ref_current;
    QPushButton *batt1_switch_control_mode_pb;
    QLabel *label_ref_current;
    QLabel *batt1_ref_current;
    QLabel *label_status_2;
    QLabel *label_ref_voltage;
    QLabel *label_set_ref_voltage;
    QDial *dial_2;
    QLabel *batt1_on_off_indicator;
    QLabel *label_set_ref_current;
    QPushButton *batt1_on_off_pb;

    void setupUi(QWidget *battery1Control)
    {
        if (battery1Control->objectName().isEmpty())
            battery1Control->setObjectName(QStringLiteral("battery1Control"));
        battery1Control->resize(380, 480);
        battery1Control->setStyleSheet(QStringLiteral("background-color: rgb(0, 0, 0);"));
        label_title = new QLabel(battery1Control);
        label_title->setObjectName(QStringLiteral("label_title"));
        label_title->setGeometry(QRect(0, 10, 381, 41));
        QFont font;
        font.setPointSize(20);
        font.setBold(true);
        font.setUnderline(false);
        font.setWeight(75);
        label_title->setFont(font);
        label_title->setLayoutDirection(Qt::LeftToRight);
        label_title->setStyleSheet(QLatin1String("color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0);"));
        label_title->setAlignment(Qt::AlignCenter);
        label_op_state = new QLabel(battery1Control);
        label_op_state->setObjectName(QStringLiteral("label_op_state"));
        label_op_state->setGeometry(QRect(40, 120, 192, 21));
        QFont font1;
        font1.setPointSize(14);
        font1.setBold(true);
        font1.setWeight(75);
        label_op_state->setFont(font1);
        label_op_state->setStyleSheet(QLatin1String("color: rgb(255, 255, 255);\n"
""));
        spinBox = new QSpinBox(battery1Control);
        spinBox->setObjectName(QStringLiteral("spinBox"));
        spinBox->setGeometry(QRect(140, 360, 20, 61));
        spinBox->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        spinBox->setMinimum(-3000);
        spinBox->setMaximum(3000);
        batt1_control_mode = new QLabel(battery1Control);
        batt1_control_mode->setObjectName(QStringLiteral("batt1_control_mode"));
        batt1_control_mode->setGeometry(QRect(210, 290, 150, 20));
        QFont font2;
        font2.setPointSize(11);
        font2.setBold(true);
        font2.setWeight(75);
        batt1_control_mode->setFont(font2);
        batt1_control_mode->setStyleSheet(QStringLiteral("color: rgb(255, 170, 0);"));
        batt1_control_mode->setAlignment(Qt::AlignBottom|Qt::AlignHCenter);
        batt1_apply_current_pb = new QPushButton(battery1Control);
        batt1_apply_current_pb->setObjectName(QStringLiteral("batt1_apply_current_pb"));
        batt1_apply_current_pb->setGeometry(QRect(60, 430, 71, 31));
        batt1_apply_current_pb->setStyleSheet(QLatin1String("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 0);"));
        dial = new QDial(battery1Control);
        dial->setObjectName(QStringLiteral("dial"));
        dial->setGeometry(QRect(50, 353, 91, 81));
        dial->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        dial->setMinimum(-3000);
        dial->setMaximum(3000);
        label_control = new QLabel(battery1Control);
        label_control->setObjectName(QStringLiteral("label_control"));
        label_control->setGeometry(QRect(40, 220, 81, 17));
        QFont font3;
        font3.setPointSize(16);
        font3.setBold(true);
        font3.setWeight(75);
        label_control->setFont(font3);
        label_control->setStyleSheet(QStringLiteral("color: rgb(255, 255, 0);"));
        batt1_operating_state = new QLabel(battery1Control);
        batt1_operating_state->setObjectName(QStringLiteral("batt1_operating_state"));
        batt1_operating_state->setGeometry(QRect(220, 120, 131, 21));
        QFont font4;
        font4.setPointSize(12);
        font4.setBold(true);
        font4.setWeight(75);
        batt1_operating_state->setFont(font4);
        batt1_operating_state->setStyleSheet(QLatin1String("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);"));
        batt1_operating_state->setAlignment(Qt::AlignCenter);
        batt1_set_ref_voltage = new QLabel(battery1Control);
        batt1_set_ref_voltage->setObjectName(QStringLiteral("batt1_set_ref_voltage"));
        batt1_set_ref_voltage->setGeometry(QRect(265, 340, 31, 17));
        batt1_set_ref_voltage->setFont(font4);
        batt1_set_ref_voltage->setStyleSheet(QStringLiteral("color: rgb(255, 170, 0);"));
        spinBox_2 = new QSpinBox(battery1Control);
        spinBox_2->setObjectName(QStringLiteral("spinBox_2"));
        spinBox_2->setGeometry(QRect(320, 360, 20, 61));
        spinBox_2->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        spinBox_2->setMaximum(400);
        batt1_ref_voltage = new QLabel(battery1Control);
        batt1_ref_voltage->setObjectName(QStringLiteral("batt1_ref_voltage"));
        batt1_ref_voltage->setGeometry(QRect(270, 180, 81, 21));
        batt1_ref_voltage->setFont(font4);
        batt1_ref_voltage->setStyleSheet(QLatin1String("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);"));
        batt1_ref_voltage->setAlignment(Qt::AlignCenter);
        batt1_apply_voltage_pb = new QPushButton(battery1Control);
        batt1_apply_voltage_pb->setObjectName(QStringLiteral("batt1_apply_voltage_pb"));
        batt1_apply_voltage_pb->setGeometry(QRect(240, 430, 71, 31));
        batt1_apply_voltage_pb->setStyleSheet(QLatin1String("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 0);"));
        batt1_set_ref_current = new QLabel(battery1Control);
        batt1_set_ref_current->setObjectName(QStringLiteral("batt1_set_ref_current"));
        batt1_set_ref_current->setGeometry(QRect(80, 340, 51, 17));
        batt1_set_ref_current->setFont(font4);
        batt1_set_ref_current->setStyleSheet(QStringLiteral("color: rgb(255, 170, 0);"));
        batt1_switch_control_mode_pb = new QPushButton(battery1Control);
        batt1_switch_control_mode_pb->setObjectName(QStringLiteral("batt1_switch_control_mode_pb"));
        batt1_switch_control_mode_pb->setGeometry(QRect(230, 250, 101, 41));
        batt1_switch_control_mode_pb->setStyleSheet(QLatin1String("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 0);"));
        label_ref_current = new QLabel(battery1Control);
        label_ref_current->setObjectName(QStringLiteral("label_ref_current"));
        label_ref_current->setGeometry(QRect(40, 149, 241, 21));
        label_ref_current->setFont(font1);
        label_ref_current->setStyleSheet(QLatin1String("color: rgb(255, 255, 255);\n"
""));
        batt1_ref_current = new QLabel(battery1Control);
        batt1_ref_current->setObjectName(QStringLiteral("batt1_ref_current"));
        batt1_ref_current->setGeometry(QRect(270, 150, 81, 21));
        batt1_ref_current->setFont(font4);
        batt1_ref_current->setStyleSheet(QLatin1String("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);"));
        batt1_ref_current->setAlignment(Qt::AlignCenter);
        label_status_2 = new QLabel(battery1Control);
        label_status_2->setObjectName(QStringLiteral("label_status_2"));
        label_status_2->setGeometry(QRect(70, 80, 71, 30));
        label_status_2->setFont(font1);
        label_status_2->setStyleSheet(QLatin1String("color: rgb(255, 255, 255);\n"
""));
        label_ref_voltage = new QLabel(battery1Control);
        label_ref_voltage->setObjectName(QStringLiteral("label_ref_voltage"));
        label_ref_voltage->setGeometry(QRect(40, 179, 221, 21));
        label_ref_voltage->setFont(font1);
        label_ref_voltage->setStyleSheet(QLatin1String("color: rgb(255, 255, 255);\n"
""));
        label_set_ref_voltage = new QLabel(battery1Control);
        label_set_ref_voltage->setObjectName(QStringLiteral("label_set_ref_voltage"));
        label_set_ref_voltage->setGeometry(QRect(230, 320, 131, 21));
        label_set_ref_voltage->setFont(font2);
        label_set_ref_voltage->setStyleSheet(QStringLiteral("color: rgb(255, 255, 255);"));
        label_set_ref_voltage->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        dial_2 = new QDial(battery1Control);
        dial_2->setObjectName(QStringLiteral("dial_2"));
        dial_2->setGeometry(QRect(230, 353, 91, 81));
        dial_2->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        dial_2->setMaximum(400);
        dial_2->setValue(380);
        dial_2->setTracking(true);
        batt1_on_off_indicator = new QLabel(battery1Control);
        batt1_on_off_indicator->setObjectName(QStringLiteral("batt1_on_off_indicator"));
        batt1_on_off_indicator->setGeometry(QRect(220, 90, 131, 20));
        batt1_on_off_indicator->setFont(font4);
        batt1_on_off_indicator->setStyleSheet(QStringLiteral("color: rgb(0, 0, 0);"));
        batt1_on_off_indicator->setAlignment(Qt::AlignCenter);
        label_set_ref_current = new QLabel(battery1Control);
        label_set_ref_current->setObjectName(QStringLiteral("label_set_ref_current"));
        label_set_ref_current->setGeometry(QRect(50, 320, 131, 21));
        label_set_ref_current->setFont(font2);
        label_set_ref_current->setStyleSheet(QStringLiteral("color: rgb(255, 255, 255);"));
        batt1_on_off_pb = new QPushButton(battery1Control);
        batt1_on_off_pb->setObjectName(QStringLiteral("batt1_on_off_pb"));
        batt1_on_off_pb->setGeometry(QRect(60, 250, 91, 41));
        batt1_on_off_pb->setStyleSheet(QLatin1String("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 0);"));
        label_set_ref_voltage->raise();
        label_title->raise();
        label_op_state->raise();
        spinBox->raise();
        batt1_control_mode->raise();
        batt1_apply_current_pb->raise();
        dial->raise();
        label_control->raise();
        batt1_operating_state->raise();
        batt1_set_ref_voltage->raise();
        spinBox_2->raise();
        batt1_ref_voltage->raise();
        batt1_apply_voltage_pb->raise();
        batt1_set_ref_current->raise();
        batt1_switch_control_mode_pb->raise();
        label_ref_current->raise();
        batt1_ref_current->raise();
        label_status_2->raise();
        label_ref_voltage->raise();
        dial_2->raise();
        batt1_on_off_indicator->raise();
        label_set_ref_current->raise();
        batt1_on_off_pb->raise();

        retranslateUi(battery1Control);
        QObject::connect(dial_2, SIGNAL(valueChanged(int)), batt1_set_ref_voltage, SLOT(setNum(int)));
        QObject::connect(dial_2, SIGNAL(valueChanged(int)), spinBox_2, SLOT(setValue(int)));
        QObject::connect(spinBox_2, SIGNAL(valueChanged(int)), batt1_set_ref_voltage, SLOT(setNum(int)));
        QObject::connect(dial, SIGNAL(valueChanged(int)), batt1_set_ref_current, SLOT(setNum(int)));
        QObject::connect(dial, SIGNAL(valueChanged(int)), spinBox, SLOT(setValue(int)));
        QObject::connect(spinBox, SIGNAL(valueChanged(int)), batt1_set_ref_current, SLOT(setNum(int)));

        QMetaObject::connectSlotsByName(battery1Control);
    } // setupUi

    void retranslateUi(QWidget *battery1Control)
    {
        battery1Control->setWindowTitle(QApplication::translate("battery1Control", "battery1Control", 0));
        label_title->setText(QApplication::translate("battery1Control", "BATTERY CONTROL", 0));
        label_op_state->setText(QApplication::translate("battery1Control", "Operating Mode:", 0));
        batt1_control_mode->setText(QApplication::translate("battery1Control", "Monitor Bus", 0));
        batt1_apply_current_pb->setText(QApplication::translate("battery1Control", "Apply", 0));
        label_control->setText(QApplication::translate("battery1Control", "Control", 0));
        batt1_operating_state->setText(QApplication::translate("battery1Control", "Constant Current", 0));
        batt1_set_ref_voltage->setText(QApplication::translate("battery1Control", "380", 0));
        batt1_ref_voltage->setText(QApplication::translate("battery1Control", "Nil", 0));
        batt1_apply_voltage_pb->setText(QApplication::translate("battery1Control", "Apply", 0));
        batt1_set_ref_current->setText(QApplication::translate("battery1Control", "0", 0));
        batt1_switch_control_mode_pb->setText(QApplication::translate("battery1Control", "Switch\n"
" Control Mode", 0));
        label_ref_current->setText(QApplication::translate("battery1Control", "Reference Current (mA): ", 0));
        batt1_ref_current->setText(QApplication::translate("battery1Control", "Nil", 0));
        label_status_2->setText(QApplication::translate("battery1Control", "Status:", 0));
        label_ref_voltage->setText(QApplication::translate("battery1Control", "Reference Voltage (V): ", 0));
        label_set_ref_voltage->setText(QApplication::translate("battery1Control", "Set Ref Voltage:", 0));
        batt1_on_off_indicator->setText(QApplication::translate("battery1Control", "OFF", 0));
        label_set_ref_current->setText(QApplication::translate("battery1Control", "Set Ref Current:", 0));
        batt1_on_off_pb->setText(QApplication::translate("battery1Control", "On/Off", 0));
    } // retranslateUi

};

namespace Ui {
    class battery1Control: public Ui_battery1Control {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_BATTERY1CONTROL_H
