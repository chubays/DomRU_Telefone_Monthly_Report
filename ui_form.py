# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, Qt, QMetaObject)
from PySide6.QtWidgets import (QComboBox, QDateEdit, QGridLayout,
                               QGroupBox, QHBoxLayout, QLabel,
                               QLayout, QLineEdit, QListView,
                               QPushButton, QStatusBar, QTabWidget,
                               QTableView, QTableWidget, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_22 = QLabel(self.groupBox_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_3.addWidget(self.label_22)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(7)

        self.verticalLayout_3.addWidget(self.comboBox)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.start_date = QDateEdit(self.groupBox_2)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setEnabled(False)
        self.start_date.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.start_date)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.end_date = QDateEdit(self.groupBox_2)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setEnabled(False)
        self.end_date.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.end_date)

        self.btn_request = QPushButton(self.groupBox_2)
        self.btn_request.setObjectName(u"btn_request")

        self.verticalLayout_3.addWidget(self.btn_request)

        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.btn_calculate = QPushButton(self.groupBox)
        self.btn_calculate.setObjectName(u"btn_calculate")
        self.btn_calculate.setEnabled(False)

        self.verticalLayout_2.addWidget(self.btn_calculate)

        self.btn_save_report = QPushButton(self.groupBox)
        self.btn_save_report.setObjectName(u"btn_save_report")
        self.btn_save_report.setEnabled(False)

        self.verticalLayout_2.addWidget(self.btn_save_report)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.gridLayout.addWidget(self.groupBox, 0, 3, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_5)

        self.le_subscription = QLineEdit(self.groupBox_3)
        self.le_subscription.setObjectName(u"le_subscription")
        self.le_subscription.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.le_subscription)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_6)

        self.le_personal = QLineEdit(self.groupBox_3)
        self.le_personal.setObjectName(u"le_personal")

        self.horizontalLayout.addWidget(self.le_personal)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.le_divisions_cost = QLineEdit(self.groupBox_3)
        self.le_divisions_cost.setObjectName(u"le_divisions_cost")

        self.horizontalLayout.addWidget(self.le_divisions_cost)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.le_minuts = QLineEdit(self.groupBox_3)
        self.le_minuts.setObjectName(u"le_minuts")

        self.horizontalLayout.addWidget(self.le_minuts)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_9)

        self.le_cost_for_number = QLineEdit(self.groupBox_3)
        self.le_cost_for_number.setObjectName(u"le_cost_for_number")

        self.horizontalLayout.addWidget(self.le_cost_for_number)

        self.btn_from_invoice = QPushButton(self.groupBox_3)
        self.btn_from_invoice.setObjectName(u"btn_from_invoice")

        self.horizontalLayout.addWidget(self.btn_from_invoice)

        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 3)

        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 0, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.lv_divisions = QListView(self.groupBox_4)
        self.lv_divisions.setObjectName(u"lv_divisions")

        self.verticalLayout_4.addWidget(self.lv_divisions)

        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_5.addWidget(self.label_10)

        self.tw_phones = QTableWidget(self.groupBox_5)
        self.tw_phones.setObjectName(u"tw_phones")

        self.verticalLayout_5.addWidget(self.tw_phones)

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_20 = QLabel(self.groupBox_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_20)

        self.le_name = QLineEdit(self.groupBox_5)
        self.le_name.setObjectName(u"le_name")

        self.verticalLayout_6.addWidget(self.le_name)

        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_21)

        self.lineEdit_5 = QLineEdit(self.groupBox_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)

        self.verticalLayout_6.addWidget(self.lineEdit_5)

        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_11)

        self.le_divisions = QLineEdit(self.groupBox_5)
        self.le_divisions.setObjectName(u"le_divisions")

        self.verticalLayout_6.addWidget(self.le_divisions)

        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_12)

        self.le_personals = QLineEdit(self.groupBox_5)
        self.le_personals.setObjectName(u"le_personals")

        self.verticalLayout_6.addWidget(self.le_personals)

        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_6.addWidget(self.label_17)

        self.btn_save_divisions = QPushButton(self.groupBox_5)
        self.btn_save_divisions.setObjectName(u"btn_save_divisions")

        self.verticalLayout_6.addWidget(self.btn_save_divisions)

        self.label_18 = QLabel(self.groupBox_5)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_6.addWidget(self.label_18)

        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_6.addWidget(self.label_19)

        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_6.addWidget(self.label_16)

        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_6.addWidget(self.label_15)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_6.addWidget(self.label_14)

        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_6.addWidget(self.label_13)

        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.gridLayout_2.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0438\u0438 \u0414\u043e\u043c\u0420\u0443",
                                                             None))
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow",
                                                            u"\u041f\u0435\u0440\u0438\u043e\u0434 \u043e\u0442\u0447\u0451\u0442\u0430",
                                                            None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434", None))
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430",
                                       None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f",
                                                        None))
        self.btn_request.setText(
            QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.btn_calculate.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u0442\u0447\u0451\u0442",
                                                              None))
        self.btn_save_report.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043e\u0442\u0447\u0451\u0442",
                                                                None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.groupBox_3.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0410\u0431\u043e\u043d\u0435\u043d\u0442\u0441\u043a\u0430\u044f \u043f\u043b\u0430\u0442\u0430",
                                                        None))
        self.le_subscription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"3500", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043d\u043e\u043c\u0435\u0440\u0430",
                                                        None))
        self.le_personal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b\u044b", None))
        self.le_divisions_cost.setPlaceholderText(QCoreApplication.translate("MainWindow", u"900", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0443\u0442\u044b", None))
        self.le_minuts.setPlaceholderText(QCoreApplication.translate("MainWindow", u"23500", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0426\u0435\u043d\u0430 \u0437\u0430 \u043d\u043e\u043c\u0435\u0440",
                                                        None))
        self.le_cost_for_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"160", None))
        self.btn_from_invoice.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0438\u0437 \u0441\u0447\u0451\u0442\u0430",
                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0451\u0442", None))
        self.groupBox_4.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b\u044b", None))
        self.groupBox_5.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u044b \u043e\u0442\u0434\u0435\u043b\u0430",
                                                         None))
        self.label_20.setText(
            QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0442\u0434\u0435\u043b\u043e\u0432",
                                                         None))
        self.label_12.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432",
                                                         None))
        self.label_17.setText("")
        self.btn_save_divisions.setText(QCoreApplication.translate("MainWindow",
                                                                   u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f",
                                                                   None))
        self.label_18.setText("")
        self.label_19.setText("")
        self.label_16.setText("")
        self.label_15.setText("")
        self.label_14.setText("")
        self.label_13.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043e\u0442\u0434\u0435\u043b\u043e\u0432",
                                                                                                 None))
    # retranslateUi
