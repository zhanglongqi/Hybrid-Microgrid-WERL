/********************************************************************************
** Form generated from reading UI file 'pvcontrol.ui'
**
** Created by: Qt User Interface Compiler version 5.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PVCONTROL_H
#define UI_PVCONTROL_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_pvControl
{
public:
    QPushButton *mppt_chnl3_on_off;
    QLabel *mppt_chnl2_operating_state;
    QLabel *mppt_chnl3_on_off_indicator;
    QLabel *label_mppt_chnl2;
    QPushButton *mppt_chnl2_on_off;
    QLabel *mppt_chnl2_on_off_indicator;
    QLabel *mppt_chnl3_operating_state;
    QLabel *label_operating_state;
    QLabel *label_status_2;
    QLabel *label_mppt_chnl3;
    QLabel *label_control;
    QLabel *label_operating_state_2;
    QLabel *label_status_3;
    QLabel *label_title;

    void setupUi(QWidget *pvControl)
    {
        if (pvControl->objectName().isEmpty())
            pvControl->setObjectName(QStringLiteral("pvControl"));
        pvControl->resize(380, 480);
        pvControl->setStyleSheet(QStringLiteral("background-color: rgb(0, 0, 0);"));
        mppt_chnl3_on_off = new QPushButton(pvControl);
        mppt_chnl3_on_off->setObjectName(QStringLiteral("mppt_chnl3_on_off"));
        mppt_chnl3_on_off->setGeometry(QRect(220, 332, 81, 51));
        mppt_chnl3_on_off->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        mppt_chnl2_operating_state = new QLabel(pvControl);
        mppt_chnl2_operating_state->setObjectName(QStringLiteral("mppt_chnl2_operating_state"));
        mppt_chnl2_operating_state->setGeometry(QRect(190, 140, 131, 21));
        mppt_chnl2_operating_state->setStyleSheet(QLatin1String("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);"));
        mppt_chnl2_operating_state->setAlignment(Qt::AlignCenter);
        mppt_chnl3_on_off_indicator = new QLabel(pvControl);
        mppt_chnl3_on_off_indicator->setObjectName(QStringLiteral("mppt_chnl3_on_off_indicator"));
        mppt_chnl3_on_off_indicator->setGeometry(QRect(186, 202, 131, 26));
        mppt_chnl3_on_off_indicator->setStyleSheet(QStringLiteral("color: rgb(0, 0, 0);"));
        mppt_chnl3_on_off_indicator->setAlignment(Qt::AlignCenter);
        label_mppt_chnl2 = new QLabel(pvControl);
        label_mppt_chnl2->setObjectName(QStringLiteral("label_mppt_chnl2"));
        label_mppt_chnl2->setGeometry(QRect(50, 62, 101, 27));
        QFont font;
        font.setPointSize(14);
        font.setBold(true);
        font.setWeight(75);
        label_mppt_chnl2->setFont(font);
        label_mppt_chnl2->setStyleSheet(QLatin1String("color: rgb(0, 0, 255);\n"
""));
        mppt_chnl2_on_off = new QPushButton(pvControl);
        mppt_chnl2_on_off->setObjectName(QStringLiteral("mppt_chnl2_on_off"));
        mppt_chnl2_on_off->setGeometry(QRect(80, 332, 81, 51));
        mppt_chnl2_on_off->setStyleSheet(QStringLiteral("background-color: rgb(255, 170, 0);"));
        mppt_chnl2_on_off_indicator = new QLabel(pvControl);
        mppt_chnl2_on_off_indicator->setObjectName(QStringLiteral("mppt_chnl2_on_off_indicator"));
        mppt_chnl2_on_off_indicator->setGeometry(QRect(190, 100, 131, 21));
        mppt_chnl2_on_off_indicator->setStyleSheet(QStringLiteral("color: rgb(0, 0, 0);"));
        mppt_chnl2_on_off_indicator->setAlignment(Qt::AlignCenter);
        mppt_chnl3_operating_state = new QLabel(pvControl);
        mppt_chnl3_operating_state->setObjectName(QStringLiteral("mppt_chnl3_operating_state"));
        mppt_chnl3_operating_state->setGeometry(QRect(190, 248, 131, 21));
        mppt_chnl3_operating_state->setStyleSheet(QLatin1String("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);"));
        mppt_chnl3_operating_state->setAlignment(Qt::AlignCenter);
        label_operating_state = new QLabel(pvControl);
        label_operating_state->setObjectName(QStringLiteral("label_operating_state"));
        label_operating_state->setGeometry(QRect(50, 143, 131, 16));
        QFont font1;
        font1.setPointSize(12);
        font1.setBold(true);
        font1.setWeight(75);
        label_operating_state->setFont(font1);
        label_operating_state->setStyleSheet(QStringLiteral("color: rgb(255, 255, 255);"));
        label_status_2 = new QLabel(pvControl);
        label_status_2->setObjectName(QStringLiteral("label_status_2"));
        label_status_2->setGeometry(QRect(50, 101, 91, 20));
        label_status_2->setFont(font1);
        label_status_2->setStyleSheet(QStringLiteral("color: rgb(255, 255, 255);"));
        label_status_2->setFrameShape(QFrame::NoFrame);
        label_mppt_chnl3 = new QLabel(pvControl);
        label_mppt_chnl3->setObjectName(QStringLiteral("label_mppt_chnl3"));
        label_mppt_chnl3->setGeometry(QRect(50, 172, 101, 27));
        label_mppt_chnl3->setFont(font);
        label_mppt_chnl3->setStyleSheet(QLatin1String("color: rgb(0, 0, 255);\n"
""));
        label_control = new QLabel(pvControl);
        label_control->setObjectName(QStringLiteral("label_control"));
        label_control->setGeometry(QRect(50, 282, 71, 17));
        label_control->setFont(font);
        label_control->setStyleSheet(QStringLiteral("color: rgb(255, 255, 0);"));
        label_operating_state_2 = new QLabel(pvControl);
        label_operating_state_2->setObjectName(QStringLiteral("label_operating_state_2"));
        label_operating_state_2->setGeometry(QRect(50, 248, 131, 21));
        label_operating_state_2->setFont(font1);
        label_operating_state_2->setStyleSheet(QStringLiteral("color: rgb(255, 255, 255);"));
        label_status_3 = new QLabel(pvControl);
        label_status_3->setObjectName(QStringLiteral("label_status_3"));
        label_status_3->setGeometry(QRect(50, 206, 81, 20));
        label_status_3->setFont(font1);
        label_status_3->setStyleSheet(QStringLiteral("color: rgb(255, 255, 255);"));
        label_status_3->setFrameShape(QFrame::NoFrame);
        label_title = new QLabel(pvControl);
        label_title->setObjectName(QStringLiteral("label_title"));
        label_title->setGeometry(QRect(0, 0, 361, 41));
        QFont font2;
        font2.setPointSize(20);
        font2.setBold(true);
        font2.setUnderline(false);
        font2.setWeight(75);
        label_title->setFont(font2);
        label_title->setLayoutDirection(Qt::LeftToRight);
        label_title->setStyleSheet(QLatin1String("color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0);"));
        label_title->setAlignment(Qt::AlignCenter);

        retranslateUi(pvControl);

        QMetaObject::connectSlotsByName(pvControl);
    } // setupUi

    void retranslateUi(QWidget *pvControl)
    {
        pvControl->setWindowTitle(QApplication::translate("pvControl", "pvControl", 0));
        mppt_chnl3_on_off->setText(QApplication::translate("pvControl", "On/Off \n"
"Chnl 3", 0));
        mppt_chnl2_operating_state->setText(QApplication::translate("pvControl", "-", 0));
        mppt_chnl3_on_off_indicator->setText(QApplication::translate("pvControl", "Off", 0));
        label_mppt_chnl2->setText(QApplication::translate("pvControl", "Channel 2", 0));
        mppt_chnl2_on_off->setText(QApplication::translate("pvControl", "On/Off \n"
"Chnl 2", 0));
        mppt_chnl2_on_off_indicator->setText(QApplication::translate("pvControl", "Off", 0));
        mppt_chnl3_operating_state->setText(QApplication::translate("pvControl", "-", 0));
        label_operating_state->setText(QApplication::translate("pvControl", "Operating State:", 0));
        label_status_2->setText(QApplication::translate("pvControl", "Status:", 0));
        label_mppt_chnl3->setText(QApplication::translate("pvControl", "Channel 3", 0));
        label_control->setText(QApplication::translate("pvControl", "Control", 0));
        label_operating_state_2->setText(QApplication::translate("pvControl", "Operating State:", 0));
        label_status_3->setText(QApplication::translate("pvControl", "Status:", 0));
        label_title->setText(QApplication::translate("pvControl", "PHOTOVOLTAIC CONTROL", 0));
    } // retranslateUi

};

namespace Ui {
    class pvControl: public Ui_pvControl {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PVCONTROL_H
