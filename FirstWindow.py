
from PyQt5 import QtCore, QtGui, QtWidgets
from SecondWindow import Ui_SecondWindow

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 783)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Facultate/Licenta/dot-crossed_icon-icons.com_68558.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        with open('FirstWindow.qss', 'r') as f:
            style = f.read()
            MainWindow.setStyleSheet(style)

        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setStyleSheet("")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topFrame = QtWidgets.QFrame(self.mainFrame)
        self.topFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.topFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topFrame.setObjectName("topFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.topFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.titleLabel = QtWidgets.QLabel(self.topFrame)
        self.titleLabel.setStyleSheet("")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.topFrame)
        self.bottomFrame = QtWidgets.QFrame(self.mainFrame)
        self.bottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomFrame.setObjectName("bottomFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.bottomFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.bottomFrame)
        self.frame_3.setMinimumSize(QtCore.QSize(230, 300))
        self.frame_3.setMaximumSize(QtCore.QSize(350, 250))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.image1Label = QtWidgets.QLabel(self.frame_3)
        self.image1Label.setMinimumSize(QtCore.QSize(220, 220))
        self.image1Label.setMaximumSize(QtCore.QSize(220, 220))
        self.image1Label.setText("")
        self.image1Label.setPixmap(QtGui.QPixmap("Images/scatter_chart_icon_215551.ico"))
        self.image1Label.setScaledContents(False)
        self.image1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.image1Label.setObjectName("image1Label")
        self.gridLayout_5.addWidget(self.image1Label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.bottomFrame)
        self.frame.setMinimumSize(QtCore.QSize(250, 300))
        self.frame.setMaximumSize(QtCore.QSize(350, 250))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.image2Label = QtWidgets.QLabel(self.frame)
        self.image2Label.setMinimumSize(QtCore.QSize(220, 220))
        self.image2Label.setMaximumSize(QtCore.QSize(220, 220))
        self.image2Label.setText("")
        self.image2Label.setPixmap(QtGui.QPixmap("Images/rotateaxisxy_120494.ico"))
        self.image2Label.setScaledContents(False)
        self.image2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.image2Label.setObjectName("image2Label")
        self.gridLayout_2.addWidget(self.image2Label, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.bottomFrame)
        self.frame_4.setMinimumSize(QtCore.QSize(230, 300))
        self.frame_4.setMaximumSize(QtCore.QSize(350, 250))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.image3Label = QtWidgets.QLabel(self.frame_4)
        self.image3Label.setMinimumSize(QtCore.QSize(220, 220))
        self.image3Label.setMaximumSize(QtCore.QSize(220, 220))
        self.image3Label.setText("")
        self.image3Label.setPixmap(QtGui.QPixmap("Images/levels (3).png"))
        self.image3Label.setScaledContents(False)
        self.image3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.image3Label.setObjectName("image3Label")
        self.gridLayout_6.addWidget(self.image3Label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_4, 0, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.bottomFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_2, clicked=lambda: self.openWindow())
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.bottomFrame)
        self.verticalLayout_2.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SVM Visualizer"))
        self.mainFrame.setAccessibleName(_translate("MainWindow", "frameMain"))
        self.topFrame.setAccessibleName(_translate("MainWindow", "topFrame"))
        self.titleLabel.setAccessibleName(_translate("MainWindow", "titleLabel"))
        self.titleLabel.setText(_translate("MainWindow", "SVM Visualizer"))
        self.bottomFrame.setAccessibleName(_translate("MainWindow", "bottomFrame"))
        self.image1Label.setAccessibleName(_translate("MainWindow", "image1Label"))
        self.image2Label.setAccessibleName(_translate("MainWindow", "image2Label"))
        self.image3Label.setAccessibleName(_translate("MainWindow", "image3Label"))
        self.pushButton.setAccessibleName(_translate("MainWindow", "btnStart"))
        self.pushButton.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
