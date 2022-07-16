# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheckResultsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *


class Ui_CheckResultsWindow(object):
    def setupUi(self, CheckResultsWindow):
        CheckResultsWindow.setObjectName("CheckResultsWindow")
        CheckResultsWindow.resize(858, 793)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Facultate/Licenta/dot-crossed_icon-icons.com_68558.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        CheckResultsWindow.setWindowIcon(icon)

        with open('CheckResultsWindow.qss', 'r') as f:
            style = f.read()
            CheckResultsWindow.setStyleSheet(style)

        self.w = None
        self.b = None
        self.indices = None
        self.vectors = None
        self.noSV = None
        self.coef = None

        self.centralwidget = QtWidgets.QWidget(CheckResultsWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bodyFrame = QtWidgets.QFrame(self.centralwidget)
        self.bodyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bodyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bodyFrame.setObjectName("bodyFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bodyFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleFrame = QtWidgets.QFrame(self.bodyFrame)
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titleFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleLabel = QtWidgets.QLabel(self.titleFrame)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        self.verticalLayout_2.addWidget(self.titleFrame)
        self.scrollArea = QtWidgets.QScrollArea(self.bodyFrame)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 794, 603))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wLabel.setObjectName("wLabel")
        self.verticalLayout_3.addWidget(self.wLabel)
        self.wTextLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wTextLabel.setText("")
        self.wTextLabel.setObjectName("wTextLabel")
        self.verticalLayout_3.addWidget(self.wTextLabel)
        self.bLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.bLabel.setObjectName("bLabel")
        self.verticalLayout_3.addWidget(self.bLabel)
        self.bTextLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.bTextLabel.setText("")
        self.bTextLabel.setObjectName("bTextLabel")
        self.verticalLayout_3.addWidget(self.bTextLabel)
        self.indicesLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.indicesLabel.setObjectName("indicesLabel")
        self.verticalLayout_3.addWidget(self.indicesLabel)
        self.indicesTextLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.indicesTextLabel.setText("")
        self.indicesTextLabel.setObjectName("indicesTextLabel")
        self.verticalLayout_3.addWidget(self.indicesTextLabel)
        self.vectorsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.vectorsLabel.setObjectName("vectorsLabel")
        self.verticalLayout_3.addWidget(self.vectorsLabel)
        self.vectorsTextLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.vectorsTextLabel.setText("")
        self.vectorsTextLabel.setObjectName("vectorsTextLabel")
        self.verticalLayout_3.addWidget(self.vectorsTextLabel)
        self.noSVLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.noSVLabel.setObjectName("noSVLabel")
        self.verticalLayout_3.addWidget(self.noSVLabel)
        self.noSVTextLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.noSVTextLabel.setText("")
        self.noSVTextLabel.setObjectName("noSVTextLabel")
        self.verticalLayout_3.addWidget(self.noSVTextLabel)
        self.coefLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.coefLabel.setObjectName("coefLabel")
        self.verticalLayout_3.addWidget(self.coefLabel)
        self.coefTextLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.coefTextLabel.setText("")
        self.coefTextLabel.setObjectName("coefTextLabel")
        self.verticalLayout_3.addWidget(self.coefTextLabel)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.LoadTextButton = QtWidgets.QPushButton(self.bodyFrame, clicked=lambda: self.loadText())
        self.LoadTextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoadTextButton.setObjectName("LoadTextButton")
        self.verticalLayout_2.addWidget(self.LoadTextButton)
        self.saveFrame = QtWidgets.QFrame(self.bodyFrame)
        self.saveFrame.setMinimumSize(QtCore.QSize(0, 120))
        self.saveFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.saveFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.saveFrame.setObjectName("saveFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.saveFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.saveFrame)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.saveTextButton = QtWidgets.QPushButton(self.saveFrame, clicked=lambda: self.saveToTextFile())
        self.saveTextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveTextButton.setObjectName("saveTextButton")
        self.verticalLayout_4.addWidget(self.saveTextButton)
        self.verticalLayout_2.addWidget(self.saveFrame)
        self.verticalLayout.addWidget(self.bodyFrame)
        CheckResultsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CheckResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(CheckResultsWindow)

    def retranslateUi(self, CheckResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        CheckResultsWindow.setWindowTitle(_translate("CheckResultsWindow", "SVM Visualizer"))
        self.bodyFrame.setAccessibleName(_translate("CheckResultsWindow", "bodyFrame"))
        self.titleFrame.setAccessibleName(_translate("CheckResultsWindow", "titleFrame"))
        self.titleLabel.setAccessibleName(_translate("CheckResultsWindow", "titleLabel"))
        self.titleLabel.setText(_translate("CheckResultsWindow", "SVM Visualizer"))
        self.wLabel.setAccessibleName(_translate("CheckResultsWindow", "wLabel"))
        self.wLabel.setText(_translate("CheckResultsWindow", "Weights assigned to the features:"))
        self.wTextLabel.setAccessibleName(_translate("CheckResultsWindow", "wTextLabel"))
        self.bLabel.setAccessibleName(_translate("CheckResultsWindow", "bLabel"))
        self.bLabel.setText(_translate("CheckResultsWindow", "Constants in the decision function:"))
        self.bTextLabel.setAccessibleName(_translate("CheckResultsWindow", "bTextLabel"))
        self.indicesLabel.setAccessibleName(_translate("CheckResultsWindow", "indicesLabel"))
        self.indicesLabel.setText(_translate("CheckResultsWindow", "Indices of support vectors:"))
        self.indicesTextLabel.setAccessibleName(_translate("CheckResultsWindow", "indicesTextLabel"))
        self.vectorsLabel.setAccessibleName(_translate("CheckResultsWindow", "vectorsLabel"))
        self.vectorsLabel.setText(_translate("CheckResultsWindow", "Support vectors:"))
        self.vectorsTextLabel.setAccessibleName(_translate("CheckResultsWindow", "vectorsTextLabel"))
        self.noSVLabel.setAccessibleName(_translate("CheckResultsWindow", "noSVLabel"))
        self.noSVLabel.setText(_translate("CheckResultsWindow", "Number of support vectors for each class:"))
        self.noSVTextLabel.setAccessibleName(_translate("CheckResultsWindow", "noSVTextLabel"))
        self.coefLabel.setAccessibleName(_translate("CheckResultsWindow", "coefLabel"))
        self.coefLabel.setText(
            _translate("CheckResultsWindow", "Dual coefficients of the support vector in the decision function"))
        self.coefTextLabel.setAccessibleName(_translate("CheckResultsWindow", "coefTextLabel"))
        self.LoadTextButton.setAccessibleName(_translate("CheckResultsWindow", "LoadTextButton"))
        self.LoadTextButton.setText(_translate("CheckResultsWindow", "Load"))
        self.saveFrame.setAccessibleName(_translate("CheckResultsWindow", "saveFrame"))
        self.lineEdit.setPlaceholderText(
            _translate("CheckResultsWindow", "Type here the name of the file in which you want to save the result"))
        self.saveTextButton.setAccessibleName(_translate("CheckResultsWindow", "saveTextButton"))
        self.saveTextButton.setText(_translate("CheckResultsWindow", "Save"))

    def loadText(self):
        self.wTextLabel.setText(str(self.w))
        self.bTextLabel.setText(str(self.b))
        self.vectorsTextLabel.setText(str(self.vectors))
        self.indicesTextLabel.setText(str(self.indices))
        self.coefTextLabel.setText(str(self.coef))
        self.noSVTextLabel.setText(str(self.noSV))

    def saveToTextFile(self):
        givenFileName = self.lineEdit.text()
        f = open(f'{givenFileName}.txt', 'w+')
        f.write('Weights assigned to the features:\n')
        f.write(self.w)
        f.write('\nConstants in the decision function:\n')
        f.write(self.b)
        f.write('\nIndices of support vectors:\n')
        f.write(self.indices)
        f.write('\nSupport vectors:\n')
        f.write(self.vectors)
        f.write('\nNumber of support vectors for each class:\n')
        f.write(self.noSV)
        f.write('\nDual coefficients of the support vector in the decision function:\n')
        f.write(self.coef)
        f.close()
        self.textFileCreated(givenFileName)

    def textFileCreated(self, givenFileName):
        msg = QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText(f"Data saved to the {givenFileName}.txt file")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    CheckResultsWindow = QtWidgets.QMainWindow()
    ui = Ui_CheckResultsWindow()
    ui.setupUi(CheckResultsWindow)
    CheckResultsWindow.show()
    sys.exit(app.exec_())