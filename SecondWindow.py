
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import os
from sklearn.datasets import make_blobs, make_circles, make_moons
from ThirdWindow import Ui_ThirdWindow
from pandas import DataFrame
from HowToCreateAFile import Ui_HowToCreateAFile


class Ui_SecondWindow(object):
    def openWindow(self):
        if self.X_both_classes is None:
            self.noDataChosenAlert()
        else:
            # Open the third window
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ThirdWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            # Transfer the data
            self.ui.feature1 = self.feature1
            self.ui.feature2 = self.feature2
            self.ui.file_name = self.file_name
            self.ui.X_class0 = self.X_class0
            self.ui.X_class1 = self.X_class1
            self.ui.y_class0 = self.y_class0
            self.ui.y_class1 = self.y_class1
            self.ui.firstLabel = self.firstLabel
            self.ui.secondLabel = self.secondLabel
            self.ui.X_both_classes = self.X_both_classes
            self.ui.y_both_classes = self.y_both_classes
            self.ui.color1 = self.color1
            self.ui.color2 = self.color2
            self.ui.randomGenerated = self.randomGenerated
            self.ui.randomX = self.randomX
            self.ui.randomy = self.randomy

    plt.rcParams.update({'font.family': 'Century Gothic'})  # setting the font for all elements of the plot

    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.showMaximized()
        with open('SecondWindow.qss', 'r') as f:
            style = f.read()
            SecondWindow.setStyleSheet(style)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Facultate/Licenta/dot-crossed_icon-icons.com_68558.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        SecondWindow.setWindowIcon(icon)

        self.color1 = '#ec6302'
        self.color2 = '#1b8697'
        self.feature1 = None
        self.feature2 = None
        self.data = None
        self.file_name = None
        self.X_class0 = None
        self.X_class1 = None
        self.y_class0 = None
        self.y_class1 = None
        self.X_both_classes = None
        self.y_both_classes = None
        self.firstLabel = None
        self.secondLabel = None
        self.randomGenerated = False
        self.randomX = None
        self.randomy = None

        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bodyFrame = QtWidgets.QFrame(self.centralwidget)
        self.bodyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bodyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bodyFrame.setObjectName("bodyFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.bodyFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleFrame = QtWidgets.QFrame(self.bodyFrame)
        self.titleFrame.setMinimumSize(QtCore.QSize(0, 70))
        self.titleFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titleFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleLabel = QtWidgets.QLabel(self.titleFrame)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        self.verticalLayout.addWidget(self.titleFrame)
        self.mainFrame = QtWidgets.QFrame(self.bodyFrame)
        self.mainFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftFrame = QtWidgets.QFrame(self.mainFrame)
        self.leftFrame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.leftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftFrame.setObjectName("leftFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.leftFrameTop = QtWidgets.QFrame(self.leftFrame)
        self.leftFrameTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftFrameTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftFrameTop.setObjectName("leftFrameTop")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftFrameTop)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.numeFisierLabel = QtWidgets.QLabel(self.leftFrameTop)
        self.numeFisierLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.numeFisierLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numeFisierLabel.setObjectName("numeFisierLabel")
        self.verticalLayout_3.addWidget(self.numeFisierLabel)
        self.howToCreateAFile = QtWidgets.QPushButton(self.leftFrameTop, clicked = lambda: self.openHowTo())
        self.howToCreateAFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.howToCreateAFile.setObjectName("howToCreateAFile")
        self.verticalLayout_3.addWidget(self.howToCreateAFile)
        self.feature1Label = QtWidgets.QLabel(self.leftFrameTop)
        self.feature1Label.setObjectName("feature1Label")
        self.verticalLayout_3.addWidget(self.feature1Label)
        self.feature1ComboBox = QtWidgets.QComboBox(self.leftFrameTop)
        self.feature1ComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.feature1ComboBox.setObjectName("feature1ComboBox")
        self.verticalLayout_3.addWidget(self.feature1ComboBox)
        self.feature2Label = QtWidgets.QLabel(self.leftFrameTop)
        self.feature2Label.setObjectName("feature2Label")
        self.verticalLayout_3.addWidget(self.feature2Label)
        self.feature2ComboBox = QtWidgets.QComboBox(self.leftFrameTop)
        self.feature2ComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.feature2ComboBox.setObjectName("feature2ComboBox")
        self.verticalLayout_3.addWidget(self.feature2ComboBox)
        self.frame = QtWidgets.QFrame(self.leftFrameTop)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.importFisierButton = QtWidgets.QPushButton(self.frame, clicked=lambda: self.fileImport())
        self.importFisierButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.importFisierButton.setObjectName("importFisierButton")
        self.verticalLayout_4.addWidget(self.importFisierButton)
        self.loadDataButton = QtWidgets.QPushButton(self.frame, clicked=lambda: self.loadData())
        self.loadDataButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loadDataButton.setObjectName("loadDataButton")
        self.verticalLayout_4.addWidget(self.loadDataButton)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.leftFrameTop)
        self.leftFrameBottom = QtWidgets.QFrame(self.leftFrame)
        self.leftFrameBottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftFrameBottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftFrameBottom.setObjectName("leftFrameBottom")
        self.gridLayout = QtWidgets.QGridLayout(self.leftFrameBottom)
        self.gridLayout.setObjectName("gridLayout")
        self.dataSet4Button = QtWidgets.QPushButton(self.leftFrameBottom,
                                                    clicked=lambda: self.plotOnCanvasExistentData(4))
        self.dataSet4Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataSet4Button.setObjectName("dataSet4Button")
        self.gridLayout.addWidget(self.dataSet4Button, 1, 1, 1, 1)
        self.dataSet2Button = QtWidgets.QPushButton(self.leftFrameBottom,
                                                    clicked=lambda: self.plotOnCanvasExistentData(2))
        self.dataSet2Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataSet2Button.setObjectName("dataSet2Button")
        self.gridLayout.addWidget(self.dataSet2Button, 0, 1, 1, 1)
        self.dataSet1Button = QtWidgets.QPushButton(self.leftFrameBottom,
                                                    clicked=lambda: self.plotOnCanvasExistentData(1))
        self.dataSet1Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataSet1Button.setObjectName("dataSet1Button")
        self.gridLayout.addWidget(self.dataSet1Button, 0, 0, 1, 1)
        self.dataSet3Button = QtWidgets.QPushButton(self.leftFrameBottom,
                                                    clicked=lambda: self.plotOnCanvasExistentData(3))
        self.dataSet3Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataSet3Button.setObjectName("dataSet3Button")
        self.gridLayout.addWidget(self.dataSet3Button, 1, 0, 1, 1)
        self.randomDataButton = QtWidgets.QPushButton(self.leftFrameBottom, clicked=lambda: self.random_data())
        self.randomDataButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.randomDataButton.setObjectName("randomDataButton")
        self.gridLayout.addWidget(self.randomDataButton, 2, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.leftFrameBottom)
        self.horizontalLayout_2.addWidget(self.leftFrame)
        self.rightFrame = QtWidgets.QFrame(self.mainFrame)
        self.rightFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightFrame.setObjectName("rightFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.rightFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.startSVMButton = QtWidgets.QPushButton(self.rightFrame, clicked=lambda: self.openWindow())
        self.startSVMButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startSVMButton.setObjectName("startSVMButton")
        self.gridLayout_2.addWidget(self.startSVMButton, 0, 0, 1, 1)
        self.plotFrame = QtWidgets.QFrame(self.rightFrame)
        self.plotFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plotFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plotFrame.setObjectName("plotFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.plotFrame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        ##Canvas here
        self.figure1 = plt.figure(1)
        self.canvas1 = FigureCanvas(self.figure1)
        ##end of Canvas
        self.horizontalLayout_5.addWidget(self.canvas1)
        ##end of horizontal layout
        self.gridLayout_2.addWidget(self.plotFrame, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.rightFrame)
        self.verticalLayout.addWidget(self.mainFrame)
        self.horizontalLayout_3.addWidget(self.bodyFrame)
        SecondWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "SVM Visualizer"))
        self.bodyFrame.setAccessibleName(_translate("SecondWindow", "bodyFrame"))
        self.titleFrame.setAccessibleName(_translate("SecondWindow", "titleFrame"))
        self.titleLabel.setAccessibleName(_translate("SecondWindow", "titleLabel"))
        self.titleLabel.setText(_translate("SecondWindow", "SVM Visualizer"))
        self.mainFrame.setAccessibleName(_translate("SecondWindow", "mainFrame"))
        self.leftFrame.setAccessibleName(_translate("SecondWindow", "leftFrame"))
        self.leftFrameTop.setAccessibleName(_translate("SecondWindow", "leftFrameTop"))
        self.numeFisierLabel.setAccessibleName(_translate("SecondWindow", "numeFisierLabel"))
        self.numeFisierLabel.setText(_translate("SecondWindow", "No file chosen..."))
        self.feature1Label.setAccessibleName(_translate("SecondWindow", "feature1Label"))
        self.feature1Label.setText(_translate("SecondWindow", "Feature 1:"))
        self.feature1ComboBox.setAccessibleName(_translate("SecondWindow", "feature1ComboBox"))
        self.feature1ComboBox.setCurrentText(_translate("SecondWindow", "one"))
        self.feature2Label.setAccessibleName(_translate("SecondWindow", "feature2Label"))
        self.feature2Label.setText(_translate("SecondWindow", "Feature 2:"))
        self.feature2ComboBox.setAccessibleName(_translate("SecondWindow", "feature2ComboBox"))
        self.importFisierButton.setAccessibleName(_translate("SecondWindow", "importFisierButton"))
        self.importFisierButton.setText(_translate("SecondWindow", "File Import"))
        self.loadDataButton.setAccessibleName(_translate("SecondWindow", "loadDataButton"))
        self.loadDataButton.setText(_translate("SecondWindow", "Load Data"))
        self.leftFrameBottom.setAccessibleName(_translate("SecondWindow", "leftFrameButtom"))
        self.dataSet4Button.setAccessibleName(_translate("SecondWindow", "dataSet4Button"))
        self.dataSet4Button.setText(_translate("SecondWindow", "DataSet4"))
        self.dataSet2Button.setAccessibleName(_translate("SecondWindow", "dataSet2Button"))
        self.dataSet2Button.setText(_translate("SecondWindow", "DataSet2"))
        self.dataSet1Button.setAccessibleName(_translate("SecondWindow", "dataSet1Button"))
        self.dataSet1Button.setText(_translate("SecondWindow", "DataSet1"))
        self.dataSet3Button.setAccessibleName(_translate("SecondWindow", "dataSet3Button"))
        self.dataSet3Button.setText(_translate("SecondWindow", "DataSet3"))
        self.randomDataButton.setAccessibleName(_translate("SecondWindow", "randomDataButton"))
        self.randomDataButton.setText(_translate("SecondWindow", "Random Data"))
        self.rightFrame.setAccessibleName(_translate("SecondWindow", "rightFrame"))
        self.startSVMButton.setAccessibleName(_translate("SecondWindow", "startSVMButton"))
        self.startSVMButton.setText(_translate("SecondWindow", "START"))
        self.plotFrame.setAccessibleName(_translate("SecondWindow", "plotFrame"))
        self.howToCreateAFile.setAccessibleName(_translate("SecondWindow", "howToCreateAFile"))
        self.howToCreateAFile.setText(_translate("SecondWindow", "How to create a file?"))

    def plotOnCanvasExistentData(self, number):
        if number == 1:
            self.file_name = 'Iris.csv'
        elif number == 2:
            self.file_name = 'Diseases.csv'
        elif number == 3:
            self.file_name = 'Circles.csv'
        elif number == 4:
            self.file_name = 'Moons.csv'

        self.numeFisierLabel.setText(self.file_name)  # set the text label as the name of the chosen file
        self.numeFisierLabel.setStyleSheet(
            "font-size:40px;\nmargin:10px;\nfont-weight:bold;\nbackground-color:rgb(27, 134, 151);\ncolor:rgb(244, 244, 244)\n")

        data = pd.read_csv(self.file_name)
        feature_names = data.head().columns[2:]
        # Add the features to the first combo box
        self.feature1ComboBox.clear()
        for i in feature_names:
            self.feature1ComboBox.addItem(str(i))
        self.feature1ComboBox.setCurrentIndex(0)

        # Add the features to the second combo box
        self.feature2ComboBox.clear()
        for i in feature_names:
            self.feature2ComboBox.addItem(str(i))
        self.feature2ComboBox.setCurrentIndex(1)
        self.loadData()

    def fileImport(self):
        dialog = QFileDialog()  # open a file dialog
        dialog.setNameFilter("*.csv")  # allow only files with the .csv extension
        dialog.exec_()
        file = dialog.selectedFiles()  # get the path of the chosen file
        if len(file) > 0:
            data = pd.read_csv(file[0])  # get the data from the chosen file
            basename = os.path.basename(file[0])  # get the file basename as a tuple
            file_name = os.path.splitext(basename)[0]  # the name of the file
            file_extension = os.path.splitext(basename)[1]  # the extension of the file
            self.file_name = str(file_name + file_extension)
            self.numeFisierLabel.setText(self.file_name)  # set the text label as the name of the chosen file
            self.numeFisierLabel.setStyleSheet(
                "font-size:40px;\nmargin:10px;\nfont-weight:bold;\nbackground-color:rgb(27, 134, 151);\ncolor:rgb(244, 244, 244)\n")

            feature_names = data.head().columns[2:]
            # Add the features to the first combo box
            self.feature1ComboBox.clear()
            for i in feature_names:
                self.feature1ComboBox.addItem(str(i))
            self.feature1ComboBox.setCurrentIndex(0)

            # Add the features to the second combo box
            self.feature2ComboBox.clear()
            for i in feature_names:
                self.feature2ComboBox.addItem(str(i))
            self.feature2ComboBox.setCurrentIndex(1)

    def loadData(self):
        # only available if a file is chosen
        if self.file_name == None:
            self.show_popup_no_file()
        else:
            self.figure1.clear()
            self.feature1 = self.feature1ComboBox.currentText()  # get the first selected feature
            self.feature2 = self.feature2ComboBox.currentText()  # get the second selected feature

            data = pd.read_csv(self.file_name)  # read the data from the selected file
            data.sort_values(by=['Target'], inplace=True)  # sort the data based on the target value

            self.X_class0 = data.query('Target == 0')[[self.feature1, self.feature2]].to_numpy()  # first class features
            self.X_class1 = data.query('Target == 1')[
                [self.feature1, self.feature2]].to_numpy()  # second class features
            self.y_class0 = data.query('Target == 0')['Target'].to_numpy()  # first class labels
            self.y_class1 = data.query('Target == 1')['Target'].to_numpy()  # second class labels

            self.X_both_classes = data[[self.feature1, self.feature2]].to_numpy()
            self.y_both_classes = data['Target'].to_numpy()

            self.firstLabel = data.groupby('Target').first()['TargetName'].values[0]  # first target name
            self.secondLabel = data.groupby('Target').first()['TargetName'].values[1]  # second target name

            plt.scatter(self.X_class0[:, 0], self.X_class0[:, 1], color=self.color1,
                        zorder=2)  # plot the elements of the first class
            plt.scatter(self.X_class1[:, 0], self.X_class1[:, 1], color=self.color2,
                        zorder=2)  # plot the elements of the second class

            plt.axis('tight')
            self.randomGenerated = False
            plt.title(f'Data from the {self.file_name} file')  # title
            plt.xlabel(f'{self.feature1}')  # x-axis label
            plt.ylabel(f'{self.feature2}')  # y-axis label
            plt.legend([self.firstLabel, self.secondLabel])  # add the legend to the plot

            self.canvas1.draw()  # refresh the canvas

    def show_popup_no_file(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("You need to choose a file in order to proceed")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def random_data(self):
        self.figure1.clear()

        plotModels = [1, 2, 3]
        X, y = make_blobs(n_samples=200, centers=2, cluster_std=1, center_box=(-10, 10))
        if random.choice(plotModels) == 1:
            X, y = make_blobs(n_samples=200, centers=2, cluster_std=1, center_box=(-10, 10))
        elif random.choice(plotModels) == 2:
            X, y = make_moons(n_samples=200, noise=0.15)
        elif random.choice(plotModels) == 3:
            X, y = make_circles(n_samples=200, noise=0.1)

        self.randomX = X
        self.randomy = y

        data = DataFrame(dict(x=X[:, 0], y=X[:, 1], Target=y))
        data.sort_values(by=['Target'], inplace=True)

        self.X_class0 = data.query('Target == 0')[['x', 'y']].to_numpy()  # first class features
        self.X_class1 = data.query('Target == 1')[['x', 'y']].to_numpy()  # second class features
        self.y_class0 = data.query('Target == 0')['Target'].to_numpy()  # first class labels
        self.y_class1 = data.query('Target == 1')['Target'].to_numpy()  # second class labels

        self.X_both_classes = data[['x', 'y']].to_numpy()
        self.y_both_classes = data['Target'].to_numpy()
        self.firstLabel = 'SecondLabel'
        self.secondLabel = 'FirstLabel'
        self.feature1 = 'First feature'
        self.feature2 = 'Second feature'
        self.randomGenerated = True

        plt.scatter(self.X_class0[:, 0], self.X_class0[:, 1], color=self.color1,
                    zorder=2)  # plot the elements of the first class
        plt.scatter(self.X_class1[:, 0], self.X_class1[:, 1], color=self.color2,
                    zorder=2)  # plot the elements of the second class

        plt.axis('tight')
        plt.title('Randomly generated data (200 samples)')  # title
        plt.xlabel(f'{self.feature1}')  # x axis label
        plt.ylabel(f'{self.feature2}')  # y axis label
        plt.legend([self.firstLabel, self.secondLabel])  # add the legend to the plot
        self.canvas1.draw()

    def noDataChosenAlert(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("You need data in order to proceed\nChoose a file, one of the datasets or\ngenerate a random "
                    "dataset")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def openHowTo(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HowToCreateAFile()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
