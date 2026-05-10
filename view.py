# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.verticalLayout.addWidget(self.titleLabel)

        self.inputLabel = QLabel(self.centralwidget)
        self.inputLabel.setObjectName(u"inputLabel")

        self.verticalLayout.addWidget(self.inputLabel)

        self.celsiusInput = QLineEdit(self.centralwidget)
        self.celsiusInput.setObjectName(u"celsiusInput")

        self.verticalLayout.addWidget(self.celsiusInput)

        self.convertButton = QPushButton(self.centralwidget)
        self.convertButton.setObjectName(u"convertButton")

        self.verticalLayout.addWidget(self.convertButton)

        self.resultLabel = QLabel(self.centralwidget)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setAlignment(Qt.AlignCenter)
        font1 = QFont()
        font1.setPointSize(13)
        self.resultLabel.setFont(font1)

        self.verticalLayout.addWidget(self.resultLabel)

        self.errorLabel = QLabel(self.centralwidget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.errorLabel)

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")

        self.verticalLayout.addWidget(self.clearButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Temperature Converter (\u00b0C \u2192 \u00b0F)", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"\U0001f321 Temperature Converter", None))
        self.inputLabel.setText(QCoreApplication.translate("MainWindow", u"Enter temperature in Celsius (\u00b0C):", None))
        self.celsiusInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g. 100", None))
        self.convertButton.setText(QCoreApplication.translate("MainWindow", u"Convert to Fahrenheit", None))
        self.resultLabel.setText(QCoreApplication.translate("MainWindow", u"Result will appear here", None))
        self.errorLabel.setText("")
        self.errorLabel.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: red;", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

