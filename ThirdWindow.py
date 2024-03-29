import seaborn
import _thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.colors import ListedColormap
import numpy as np
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from CheckResultsWindow import Ui_CheckResultsWindow
from GammaHyperparameterWindow import Ui_infoAboutGammaWindow
from CHyperparameterWindow import Ui_InfoAboutCWindow
from DegreeParameterWindow import Ui_infoAboutDegreeWindow
from sklearn.model_selection import train_test_split
from ClassificationReport import Ui_ClassificationReportWindow
from _datetime import datetime


class Ui_ThirdWindow(object):
    def openCheckResults(self):
        if self.loaded is False:
            self.loadDataAlert()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_CheckResultsWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            self.ui.w = self.w
            self.ui.b = self.b
            self.ui.indices = self.indices
            self.ui.vectors = self.vectors
            self.ui.coef = self.coef
            self.ui.noSV = self.noSV
            self.ui.X_class0 = self.X_class0
            self.ui.X_class1 = self.X_class1
            self.ui.y_class0 = self.y_class0
            self.ui.y_class1 = self.y_class1
            self.ui.randomX = self.randomX
            self.ui.randomy = self.randomy

    def setupUi(self, ThirdWindow):
        ThirdWindow.setObjectName("ThirdWindow")
        ThirdWindow.showMaximized()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Facultate/Licenta/dot-crossed_icon-icons.com_68558.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        ThirdWindow.setWindowIcon(icon)

        with open('ThirdWindow.qss', 'r') as f:
            style = f.read()
            ThirdWindow.setStyleSheet(style)

        # user defined attributes
        self.color1 = None
        self.color2 = None
        self.X_class0 = None
        self.X_class1 = None
        self.y_class0 = None
        self.y_class1 = None
        self.X_both_classes = None
        self.y_both_classes = None
        self.X3 = None
        self.firstLabel = None
        self.secondLabel = None
        self.feature1 = None
        self.feature2 = None
        self.file_name = None
        self.trainingSize = None
        self.C_value = None
        self.Gamma_value = None
        self.degree_value = None
        self.rbf_checked = None
        self.poly_checked = None
        self.linear_checked = None
        self.sigmoid_checked = None
        self.kernel = None
        self.clfResult = None
        self.y_test = None
        self.y_pred = None

        self.loaded = False
        self.coef = None
        self.vectors = None
        self.indices = None
        self.b = None
        self.w = None
        self.correction = None
        self.randomGenerated = False
        self.classificationReport = None
        self.completeClassReport = None

        self.randomX = None
        self.randomy = None

        self.centralwidget = QtWidgets.QWidget(ThirdWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bodtFrame = QtWidgets.QFrame(self.centralwidget)
        self.bodtFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bodtFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bodtFrame.setObjectName("bodtFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.bodtFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleFrame = QtWidgets.QFrame(self.bodtFrame)
        self.titleFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.titleFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.titleLabel = QtWidgets.QLabel(self.titleFrame)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.titleFrame)
        self.mainFrame = QtWidgets.QFrame(self.bodtFrame)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftFrame = QtWidgets.QFrame(self.mainFrame)
        self.leftFrame.setMaximumSize(QtCore.QSize(550, 16777215))
        self.leftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftFrame.setObjectName("leftFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.leftTopFrame = QtWidgets.QFrame(self.leftFrame)
        self.leftTopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftTopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftTopFrame.setObjectName("leftTopFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftTopFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.kernelTypeFrame = QtWidgets.QFrame(self.leftTopFrame)
        self.kernelTypeFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.kernelTypeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.kernelTypeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.kernelTypeFrame.setObjectName("kernelTypeFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.kernelTypeFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.kernelTypeLabel = QtWidgets.QLabel(self.kernelTypeFrame)
        self.kernelTypeLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.kernelTypeLabel.setObjectName("kernelTypeLabel")
        self.verticalLayout_5.addWidget(self.kernelTypeLabel)
        self.verticalLayout_3.addWidget(self.kernelTypeFrame)
        self.kernelButtonsFrame = QtWidgets.QFrame(self.leftTopFrame)
        self.kernelButtonsFrame.setMinimumSize(QtCore.QSize(0, 120))
        self.kernelButtonsFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.kernelButtonsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.kernelButtonsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.kernelButtonsFrame.setObjectName("kernelButtonsFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.kernelButtonsFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sigmoidRB = QtWidgets.QRadioButton(self.kernelButtonsFrame, clicked=lambda: self.disableDegree())
        self.sigmoidRB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sigmoidRB.setObjectName("sigmoidRB")
        self.gridLayout_2.addWidget(self.sigmoidRB, 1, 1, 1, 1)
        self.linearRB = QtWidgets.QRadioButton(self.kernelButtonsFrame, clicked=lambda: self.disableDegree())
        self.linearRB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.linearRB.setObjectName("linearRB")
        self.gridLayout_2.addWidget(self.linearRB, 0, 0, 1, 1)
        self.rbfRB = QtWidgets.QRadioButton(self.kernelButtonsFrame, clicked=lambda: self.disableDegree())
        self.rbfRB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rbfRB.setObjectName("rbfRB")
        self.gridLayout_2.addWidget(self.rbfRB, 0, 1, 1, 1)
        self.polynomialRB = QtWidgets.QRadioButton(self.kernelButtonsFrame, clicked=lambda: self.changeDegreeLabel())
        self.polynomialRB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.polynomialRB.setObjectName("polynomialRB")
        self.gridLayout_2.addWidget(self.polynomialRB, 1, 0, 1, 1)
        self.displayAllButton = QtWidgets.QPushButton(self.kernelButtonsFrame, clicked=lambda: self.displayAll())
        self.displayAllButton.setMinimumSize(QtCore.QSize(0, 0))
        self.displayAllButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.displayAllButton.setObjectName("displayAllButton")
        self.gridLayout_2.addWidget(self.displayAllButton, 2, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.kernelButtonsFrame)
        self.adjustFrame = QtWidgets.QFrame(self.leftTopFrame)
        self.adjustFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.adjustFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.adjustFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.adjustFrame.setObjectName("adjustFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.adjustFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.adjustLabel = QtWidgets.QLabel(self.adjustFrame)
        self.adjustLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.adjustLabel.setObjectName("adjustLabel")
        self.verticalLayout_6.addWidget(self.adjustLabel)
        self.verticalLayout_3.addWidget(self.adjustFrame)
        self.frame = QtWidgets.QFrame(self.leftTopFrame)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cLabel = QtWidgets.QLabel(self.frame)
        self.cLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cLabel.setObjectName("cLabel")
        self.gridLayout_3.addWidget(self.cLabel, 0, 0, 1, 1)
        self.cValueLineEdit = QtWidgets.QLineEdit(self.frame)
        self.cValueLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cValueLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.cValueLineEdit.setObjectName("cValueLineEdit")
        self.gridLayout_3.addWidget(self.cValueLineEdit, 0, 2, 1, 1)
        self.gammaLabel = QtWidgets.QLabel(self.frame)
        self.gammaLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.gammaLabel.setObjectName("gammaLabel")
        self.gridLayout_3.addWidget(self.gammaLabel, 1, 0, 1, 2)
        self.gammaValueLineEdit = QtWidgets.QLineEdit(self.frame)
        self.gammaValueLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.gammaValueLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.gammaValueLineEdit.setObjectName("gammaValueLineEdit")
        self.gridLayout_3.addWidget(self.gammaValueLineEdit, 1, 2, 1, 1)
        self.degreeValueLineEdit = QtWidgets.QLineEdit(self.frame)
        self.degreeValueLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.degreeValueLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.degreeValueLineEdit.setObjectName("degreeValueLineEdit")
        self.degreeValueLineEdit.setEnabled(False)
        self.gridLayout_3.addWidget(self.degreeValueLineEdit, 2, 2, 1, 1)

        self.degreeLabel = QtWidgets.QLabel(self.frame)
        self.degreeLabel.setObjectName("degreeLabel")
        self.gridLayout_3.addWidget(self.degreeLabel, 2, 0, 1, 1)
        # ---
        self.infoCButton = QtWidgets.QPushButton(self.frame, clicked=lambda: self.openInfoC())
        self.infoCButton.setObjectName("infoCLabel")
        self.infoCButton.setMaximumSize(QtCore.QSize(30, 30))
        self.infoCButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_3.addWidget(self.infoCButton, 0, 3, 1, 1)
        self.infoGammaButton = QtWidgets.QPushButton(self.frame, clicked=lambda: self.openInfoGamma())
        self.infoGammaButton.setObjectName("infoGammaLabel")
        self.infoGammaButton.setMaximumSize(QtCore.QSize(30, 30))
        self.infoGammaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_3.addWidget(self.infoGammaButton, 1, 3, 1, 1)
        self.infoDegreeButton = QtWidgets.QPushButton(self.frame, clicked=lambda: self.openInfoDegree())
        self.infoDegreeButton.setObjectName("infoDegreeLabel")
        self.infoDegreeButton.setMaximumSize(QtCore.QSize(30, 30))
        self.infoDegreeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_3.addWidget(self.infoDegreeButton, 2, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.frame)
        self.trainingSampleFrame = QtWidgets.QFrame(self.leftTopFrame)
        self.trainingSampleFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.trainingSampleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trainingSampleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trainingSampleFrame.setObjectName("trainingSampleFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.trainingSampleFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.trainingSampleLabel = QtWidgets.QLabel(self.trainingSampleFrame)
        self.trainingSampleLabel.setObjectName("trainingSampleLabel")
        self.horizontalLayout_4.addWidget(self.trainingSampleLabel)
        self.trainingSampleValueLabel = QtWidgets.QLabel(self.trainingSampleFrame)
        self.trainingSampleValueLabel.setObjectName("trainingSampleValueLabel")
        self.horizontalLayout_4.addWidget(self.trainingSampleValueLabel)
        self.trainingSampleSlider = QtWidgets.QSlider(self.trainingSampleFrame, valueChanged=lambda: self.slide())
        self.trainingSampleSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.trainingSampleSlider.setMaximum(98)
        self.trainingSampleSlider.setMinimum(2)
        self.trainingSampleSlider.setSliderPosition(70)
        self.trainingSampleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.trainingSampleSlider.setInvertedControls(False)
        self.trainingSampleSlider.setObjectName("trainingSampleSlider")
        self.horizontalLayout_4.addWidget(self.trainingSampleSlider)
        self.verticalLayout_3.addWidget(self.trainingSampleFrame)
        self.loadDataButton = QtWidgets.QPushButton(self.leftTopFrame, clicked=lambda: self.loadData2())
        self.loadDataButton.setMaximumSize(QtCore.QSize(16777215, 70))
        self.loadDataButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loadDataButton.setObjectName("loadDataButton")
        self.verticalLayout_3.addWidget(self.loadDataButton)
        self.verticalLayout_2.addWidget(self.leftTopFrame)
        self.leftBottomFrame = QtWidgets.QFrame(self.leftFrame)
        self.leftBottomFrame.setMaximumSize(QtCore.QSize(16777215, 160))
        self.leftBottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftBottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftBottomFrame.setObjectName("leftBottomFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.leftBottomFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.reportButton = QtWidgets.QPushButton(self.leftBottomFrame, clicked=lambda: self.openClassificationReport())
        self.reportButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reportButton.setObjectName("reportButton")
        self.gridLayout_4.addWidget(self.reportButton, 0, 0, 1, 1)
        self.resultsButton = QtWidgets.QPushButton(self.leftBottomFrame, clicked=lambda: self.openCheckResults())
        self.resultsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resultsButton.setObjectName("resultsButton")
        self.gridLayout_4.addWidget(self.resultsButton, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.leftBottomFrame)
        self.accuracyFrame = QtWidgets.QFrame(self.leftFrame)
        self.accuracyFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.accuracyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accuracyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accuracyFrame.setObjectName("accuracyFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.accuracyFrame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.accuracyLabel = QtWidgets.QLabel(self.accuracyFrame)
        self.accuracyLabel.setObjectName("accuracyLabel")
        self.gridLayout_5.addWidget(self.accuracyLabel, 0, 0, 1, 1)
        self.accuracyValueLabel = QtWidgets.QLabel(self.accuracyFrame)
        self.accuracyValueLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.accuracyValueLabel.setObjectName("accuracyValueLabel")
        self.gridLayout_5.addWidget(self.accuracyValueLabel, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.accuracyFrame)
        self.horizontalLayout_2.addWidget(self.leftFrame)
        self.rightFrame = QtWidgets.QFrame(self.mainFrame)
        self.rightFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightFrame.setObjectName("rightFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.rightFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rightTopFrame = QtWidgets.QFrame(self.rightFrame)
        self.rightTopFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.rightTopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightTopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightTopFrame.setObjectName("rightTopFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.rightTopFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.view3DButton = QtWidgets.QPushButton(self.rightTopFrame, clicked=lambda: self.show3D_KernelFunctions())
        self.view3DButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.view3DButton.setObjectName("view3DButton")
        self.horizontalLayout_3.addWidget(self.view3DButton)
        self.confusionMatrixButton = QtWidgets.QPushButton(self.rightTopFrame,
                                                           clicked=lambda: self.showConfusionMatrix())
        self.confusionMatrixButton.setMinimumSize(QtCore.QSize(0, 0))
        self.confusionMatrixButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.confusionMatrixButton.setObjectName("confusionMatrixButton")
        self.horizontalLayout_3.addWidget(self.confusionMatrixButton)
        self.saveImage = QtWidgets.QPushButton(self.rightTopFrame, clicked=lambda: self.saveImageJPG())
        self.saveImage.setCursor((QtGui.QCursor(QtCore.Qt.PointingHandCursor)))
        self.saveImage.setObjectName("saveImageButton")
        self.horizontalLayout_3.addWidget(self.saveImage)
        self.verticalLayout_4.addWidget(self.rightTopFrame)
        self.rightBottomFrame = QtWidgets.QFrame(self.rightFrame)
        self.rightBottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightBottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightBottomFrame.setObjectName("rightBottomFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.rightBottomFrame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        ##Canvas here
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        ##end of Canvas
        self.horizontalLayout_5.addWidget(self.canvas)
        ##end of horizontal layout
        self.verticalLayout_4.addWidget(self.rightBottomFrame)
        self.horizontalLayout_2.addWidget(self.rightFrame)
        self.verticalLayout.addWidget(self.mainFrame)
        self.horizontalLayout.addWidget(self.bodtFrame)
        ThirdWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ThirdWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow)

    def retranslateUi(self, ThirdWindow):
        _translate = QtCore.QCoreApplication.translate
        ThirdWindow.setWindowTitle(_translate("ThirdWindow", "SVM Visualizer"))
        self.bodtFrame.setAccessibleName(_translate("ThirdWindow", "bodyFrame"))
        self.titleFrame.setAccessibleName(_translate("ThirdWindow", "titleFrame"))
        self.titleLabel.setAccessibleName(_translate("ThirdWindow", "titleLabel"))
        self.titleLabel.setText(_translate("ThirdWindow", "SVM Visualizer"))
        self.mainFrame.setAccessibleName(_translate("ThirdWindow", "mainFrame"))
        self.leftFrame.setAccessibleName(_translate("ThirdWindow", "leftFrame"))
        self.leftTopFrame.setAccessibleName(_translate("ThirdWindow", "leftTopFrame"))
        self.kernelTypeFrame.setAccessibleName(_translate("ThirdWindow", "kernelTypeFrame"))
        self.kernelTypeLabel.setAccessibleName(_translate("ThirdWindow", "kernelTypeLabel"))
        self.kernelTypeLabel.setText(_translate("ThirdWindow", "Kernel type:"))
        self.kernelButtonsFrame.setAccessibleName(_translate("ThirdWindow", "kernelButtonsFrame"))
        self.sigmoidRB.setText(_translate("ThirdWindow", "Sigmoid"))
        self.linearRB.setText(_translate("ThirdWindow", "Linear"))
        self.rbfRB.setText(_translate("ThirdWindow", "RBF"))
        self.polynomialRB.setText(_translate("ThirdWindow", "Polynomial"))
        self.displayAllButton.setAccessibleName(_translate("ThirdWindow", "displayAllButton"))
        self.displayAllButton.setText(_translate("ThirdWindow", "Display All"))
        self.adjustFrame.setAccessibleName(_translate("ThirdWindow", "adjustFrame"))
        self.adjustLabel.setAccessibleName(_translate("ThirdWindow", "adjustLabel"))
        self.adjustLabel.setText(_translate("ThirdWindow", "Adjust the hyperparameters:"))
        self.cLabel.setAccessibleName(_translate("ThirdWindow", "cLabel"))
        self.cLabel.setText(_translate("ThirdWindow", "C:"))
        self.cValueLineEdit.setAccessibleName(_translate("ThirdWindow", "cValueLineEdit"))
        self.gammaLabel.setAccessibleName(_translate("ThirdWindow", "gammaLabel"))
        self.gammaLabel.setText(_translate("ThirdWindow", "Gamma:"))
        self.gammaValueLineEdit.setAccessibleName(_translate("ThirdWindow", "gammaValueLineEdit"))
        self.degreeValueLineEdit.setAccessibleName(_translate("ThirdWindow", "degreeValueLineEdit"))
        self.degreeLabel.setAccessibleName(_translate("ThirdWindow", "degreeLabel"))
        self.degreeLabel.setText(_translate("ThirdWindow", "Degree:"))
        self.infoCButton.setAccessibleName(_translate("ThirdWindow", "infoCButton"))
        self.infoCButton.setText(_translate("ThirdWindow", "i"))
        self.infoGammaButton.setAccessibleName(_translate("ThirdWindow", "infoGammaButton"))
        self.infoGammaButton.setText(_translate("ThirdWindow", "i"))
        self.infoDegreeButton.setAccessibleName(_translate("ThirdWindow", "infoDegreeButton"))
        self.infoDegreeButton.setText(_translate("ThirdWindow", "i"))
        self.trainingSampleFrame.setAccessibleName(_translate("ThirdWindow", "trainingSampleFrame"))
        self.trainingSampleLabel.setAccessibleName(_translate("ThirdWindow", "trainingSampleLabel"))
        self.trainingSampleLabel.setText(_translate("ThirdWindow", "Training Sample:"))
        self.trainingSampleValueLabel.setAccessibleName(_translate("ThirdWindow", "trainingSampleValueLabel"))
        self.trainingSampleValueLabel.setText(_translate("ThirdWindow", "70%"))
        self.trainingSampleSlider.setAccessibleName(_translate("ThirdWindow", "trainingSampleSlider"))
        self.loadDataButton.setAccessibleName(_translate("ThirdWindow", "loadDataButton"))
        self.loadDataButton.setText(_translate("ThirdWindow", "Load Data"))
        self.leftBottomFrame.setAccessibleName(_translate("ThirdWindow", "leftBottomFrame"))
        self.reportButton.setAccessibleName(_translate("ThirdWindow", "reportButton"))
        self.reportButton.setText(_translate("ThirdWindow", "Classification Report"))
        self.resultsButton.setAccessibleName(_translate("ThirdWindow", "resultsButton"))
        self.resultsButton.setText(_translate("ThirdWindow", "Check Results"))
        self.accuracyFrame.setAccessibleName(_translate("ThirdWindow", "accuracyFrame"))
        self.accuracyLabel.setAccessibleName(_translate("ThirdWindow", "accuracyLabel"))
        self.accuracyLabel.setText(_translate("ThirdWindow", "Accuracy:"))
        self.accuracyValueLabel.setAccessibleName(_translate("ThirdWindow", "accuracyValueLabel"))
        self.accuracyValueLabel.setText(_translate("ThirdWindow", "0%"))
        self.rightFrame.setAccessibleName(_translate("ThirdWindow", "rightFrame"))
        self.rightTopFrame.setAccessibleName(_translate("ThirdWindow", "rightTopFrame"))
        self.view3DButton.setAccessibleName(_translate("ThirdWindow", "view3DButton"))
        self.view3DButton.setText(_translate("ThirdWindow", "View Data in 3D"))
        self.confusionMatrixButton.setAccessibleName(_translate("ThirdWindow", "confusionMatrixButton"))
        self.confusionMatrixButton.setText(_translate("ThirdWindow", "Confusion Matrix"))
        self.saveImage.setAccessibleName(_translate("ThirdWindow", "saveImageButton"))
        self.saveImage.setText(_translate("ThirdWindow", "Save Image"))
        self.rightBottomFrame.setAccessibleName(_translate("ThirdWindow", "rightBottomFrame"))

    def loadData2(self):
        self.loaded = True

        self.trainingSize = self.trainingSampleSlider.value() / 100
        self.get_hyperparameters_values()

        # Train the model
        # --> By default: 70% training and 30% test
        X_train, X_test, y_train, y_test = train_test_split(self.X_both_classes, self.y_both_classes,
                                                            test_size=1 - self.trainingSize)
        self.X_test = X_test
        self.y_test = y_test
        # fit the model
        clf = svm.SVC(kernel=self.kernel,
                      C=self.C_value,
                      gamma=self.Gamma_value,
                      degree=self.degree_value)
        clf.fit(X_train, y_train)

        plt.clf()

        plt.scatter(self.X_class0[:, 0], self.X_class0[:, 1], color=self.color1,
                    zorder=2)  # plot the elements of the first class
        plt.scatter(self.X_class1[:, 0], self.X_class1[:, 1], color=self.color2,
                    zorder=2)  # plot the elements of the second class
        # print(clf.support_vectors_)

        # Circle out the test data
        plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80, facecolors='none', zorder=10,
                    edgecolor='k')  # s -> radius of the contour circle
        plt.axis('tight')

        x_min = self.X_both_classes[:, 0].min()  # minimum x coordinate
        x_max = self.X_both_classes[:, 0].max()  # maximum x coordinate
        y_min = self.X_both_classes[:, 1].min()  # minimum y coordinate
        y_max = self.X_both_classes[:, 1].max()  # maximum y coordinate

        XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]  # create a meshgrid
        Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])  # get the data calculated by the decision function
        # Put the result into a color plot
        Z = Z.reshape(XX.shape)
        # Draw the separating hyperplanes
        plt.pcolormesh(XX, YY, Z > 0, cmap=ListedColormap(["#fec7a0", "#a3ced5"]), shading='auto')
        # Draw the decision line
        plt.contour(XX, YY, Z, colors=['k', 'k', 'k'],
                    linestyles=['--', '-', '--'], levels=[-.5, 0, .5])
        if self.randomGenerated:
            plt.title('Randomly generated data (200 samples)')
        else:
            plt.title(f'Data from the {self.file_name} file')  # set tht title
        plt.xlabel(f'{self.feature1}')  # x axis label
        plt.ylabel(f'{self.feature2}')  # y axis label
        plt.legend([self.firstLabel, self.secondLabel])  # add the legend to the plot

        self.canvas.draw()  # refresh the canvas with the resulted plot

        self.clfResult = clf

        self.createCheckResults()

        y_pred = clf.predict(X_test)  # make a prediction based on the test data
        # Get the accuracy score
        accuracyScore = metrics.accuracy_score(y_test, y_pred) * 100
        # Set the accuracy score in the interface
        self.accuracyValueLabel.setText(str(round(accuracyScore)) + '%')
        # --------------------------------------------------------
        self.y_pred = y_pred
        x = classification_report(self.y_test, self.y_pred, target_names=[self.firstLabel, self.secondLabel])
        self.completeClassReport = x
        self.classificationReport = x.split()

    def slide(self):
        self.trainingSampleValueLabel.setText(str(self.trainingSampleSlider.value()) + str('%'))

    def get_hyperparameters_values(self):
        if self.rbfRB.isChecked():
            self.kernel = 'rbf'
        elif self.linearRB.isChecked():
            self.kernel = 'linear'
        elif self.polynomialRB.isChecked():
            self.kernel = 'poly'
        elif self.sigmoidRB.isChecked():
            self.kernel = 'sigmoid'
        else:
            self.linearRB.setChecked(True)
            self.kernel = 'linear'

        self.C_value = self.cValueLineEdit.text()
        if self.C_value == '':
            self.C_value = 1.0
            self.cValueLineEdit.setText(str(self.C_value))
        else:
            self.C_value = float(self.cValueLineEdit.text())

        self.Gamma_value = self.gammaValueLineEdit.text()
        if self.Gamma_value == '':
            self.Gamma_value = 0.8
            self.gammaValueLineEdit.setText(str(self.Gamma_value))
        else:
            self.Gamma_value = float(self.gammaValueLineEdit.text())

        self.degree_value = self.degreeValueLineEdit.text()
        if self.degree_value == '':
            self.degree_value = 2
            self.degreeValueLineEdit.setText(str(self.degree_value))
        else:
            self.degree_value = float(self.degreeValueLineEdit.text())

    def changeDegreeLabel(self):
        self.degreeValueLineEdit.setEnabled(True)
        self.degreeValueLineEdit.setStyleSheet("background-color:white;")
        self.degreeLabel.setStyleSheet('color:rgb(0, 51, 69)')

    def disableDegree(self):
        self.degreeValueLineEdit.setEnabled(False)
        self.degreeValueLineEdit.setStyleSheet("background-color:#e0e0e0;")
        self.degreeLabel.setStyleSheet("font-size:20px;\nfont-weight:bold;\ncolor:#7e7e7e;")

    def displayAll(self):
        self.loaded = True
        self.trainingSize = self.trainingSampleSlider.value() / 100
        self.get_hyperparameters_values()
        self.figure.clear()

        X_train, X_test, y_train, y_test = train_test_split(self.X_both_classes, self.y_both_classes,
                                                            test_size=1 - self.trainingSize)  # 70% training and 30% test
        i = 1
        for kernel in ('linear', 'poly', 'rbf', 'sigmoid'):
            # fit the model
            clf = svm.SVC(kernel=kernel, C=self.C_value, gamma=self.Gamma_value, degree=self.degree_value)
            clf.fit(X_train, y_train)
            plt.subplot(2, 2, i)
            plt.subplots_adjust(wspace=0.4, hspace=0.4)
            i = i + 1
            plt.scatter(self.X_class0[:, 0], self.X_class0[:, 1], color=self.color1,
                        zorder=2)  # plot the elements of the first class
            plt.scatter(self.X_class1[:, 0], self.X_class1[:, 1], color=self.color2,
                        zorder=2)  # plot the elements of the second class
            # print(clf.support_vectors_)

            # Circle out the test data
            plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80, facecolors='none', zorder=10,
                        edgecolor='k')  # s -> radius of the contour circle
            plt.axis('tight')

            x_min = self.X_both_classes[:, 0].min()
            x_max = self.X_both_classes[:, 0].max()
            y_min = self.X_both_classes[:, 1].min()
            y_max = self.X_both_classes[:, 1].max()

            XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
            Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
            # Put the result into a color plot
            Z = Z.reshape(XX.shape)
            plt.pcolormesh(XX, YY, Z > 0, cmap=ListedColormap(["#fec7a0", "#a3ced5"]), shading='auto')
            plt.contour(XX, YY, Z, colors=['k', 'k', 'k'],
                        linestyles=['--', '-', '--'], levels=[-.5, 0, .5])
            if self.randomGenerated == True:
                plt.title('Randomly generated data (200 samples)')
            else:
                plt.title(f'Data from the {self.file_name} file - {kernel}')
            plt.xlabel(f'{self.feature1}')
            plt.ylabel(f'{self.feature2}')
            plt.legend([self.firstLabel, self.secondLabel])
            y_pred = clf.predict(X_test)
            accuracyScore = metrics.accuracy_score(y_test, y_pred) * 100
            self.accuracyValueLabel.setText(str(round(accuracyScore)) + '%')

        self.canvas.draw()

    def createCheckResults(self):
        if self.kernel == 'linear':
            self.w = 'w = ' + str(self.clfResult.coef_)
        else:
            self.w = 'Available only for Linear Kernel'
        self.b = 'b = ' + str(self.clfResult.intercept_)
        self.indices = str(self.clfResult.support_)
        self.vectors = str(self.clfResult.support_vectors_)
        self.noSV = str(self.clfResult.n_support_)
        self.coef = str(np.abs(self.clfResult.dual_coef_))

    def showConfusionMatrix(self):
        if self.loaded is False:
            self.loadDataAlert()
        else:
            self.figure.clear()
            cf_matrix = confusion_matrix(self.y_test, self.y_pred)
            ax = seaborn.heatmap(cf_matrix, annot=True, cmap=ListedColormap(["#fec7a0", "#a3ced5"]))
            ax.set_title(f'Confusion Matrix based on {self.file_name} data')
            ax.set_xlabel('\nPredicted Values')
            ax.set_ylabel('Actual Values')
            ax.xaxis.set_ticklabels([self.firstLabel, self.secondLabel])
            ax.yaxis.set_ticklabels([self.firstLabel, self.secondLabel])
            self.canvas.draw()
            plt.close(self.figure)

    def show3D_data(self):
        if self.loaded is False:
            self.loadDataAlert()
        else:
            X = np.column_stack((self.X_both_classes, self.X3))
            data_class0 = X[self.y_both_classes == 0, 2]
            data_class1 = X[self.y_both_classes == 1, 2]

            model = svm.SVC(kernel='linear')
            clf = model.fit(X, self.y_both_classes)

            # # The equation of the separating plane is given by all x so that np.dot(svc.coef_[0], x) + b = 0.
            # # Solve for w3 (z)
            z = lambda x, y: (-clf.intercept_[0] - clf.coef_[0][0] * x - clf.coef_[0][1] * y) / clf.coef_[0][2]
            #
            # tmp = np.linspace(5, 5, 5)
            # x, y = np.meshgrid(tmp, tmp)
            x_min = self.X_both_classes[:, 0].min()  # minimum x coordinate
            x_max = self.X_both_classes[:, 0].max()  # maximum x coordintae
            y_min = self.X_both_classes[:, 1].min()  # minimum y coordinate
            y_max = self.X_both_classes[:, 1].max()  # maximum y coordinate
            x, y = np.mgrid[x_min:x_max:10j, y_min:y_max:10j]
            plt.tight_layout()
            fig = plt.figure(figsize=(12, 12))
            ax = fig.add_subplot(projection='3d')
            ax.plot3D(self.X_class0[:, 0], self.X_class0[:, 1], data_class0, 'o', zorder=1, c='#ec6302')
            Z = z(x, y) / self.correction
            ax.plot_surface(x, y, Z, zorder=2, color='#c0c0c0', alpha=0.7)
            ax.plot3D(self.X_class1[:, 0], self.X_class1[:, 1], data_class1, 'o', zorder=3, c='#1b8697')
            ax.view_init(30, 60)
            ax.can_zoom()
            ax.can_pan()
            ax.set_title('3D Visualization of the Kernel trick')
            ax.set_xlabel(str(self.feature1))
            ax.set_ylabel(str(self.feature2))
            ax.set_zlabel('Calculated Z')
            fig.show()

    def show3D_KernelFunctions(self):
        self.correction = 1
        if self.kernel == 'poly':
            self.X3 = (self.Gamma_value + self.X_both_classes[:, 0] * self.X_both_classes[:, 1]) ** self.degree_value
            self.correction = 2
        elif self.kernel == 'rbf':
            self.X3 = np.exp(-self.Gamma_value * abs(self.X_both_classes[:, 0] - self.X_both_classes[:, 1]) ** 2)
            self.correction = 1
        elif self.kernel == 'linear':
            self.X3 = self.X_both_classes[:, 0] * self.X_both_classes[:, 1]
            self.correction = 1
        elif self.kernel == 'sigmoid':
            self.X3 = np.tanh(self.Gamma_value * self.X_both_classes[:, 0] * self.X_both_classes[:, 1] + self.C_value)
            self.correction = 5
        self.show3D_data()

    def openInfoGamma(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_infoAboutGammaWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openInfoC(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InfoAboutCWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openInfoDegree(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_infoAboutDegreeWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def loadDataAlert(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("Load the data first!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def openClassificationReport(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ClassificationReportWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.classificationReport = self.classificationReport
        self.ui.completeClassReport = self.completeClassReport

    def saveImageJPG(self):
        if self.loaded is False:
            self.loadDataAlert()
        else:
            if self.randomGenerated:
                plt.savefig(f'Figure-random-{self.kernel}-{datetime.now().strftime("%d-%m-%Y-%h-%M-%S")}.jpg')
            else:
                plt.savefig(f'Figure-{self.file_name}-{self.kernel}-{datetime.now().strftime("%d-%m-%Y-%h-%M-%S")}.jpg')
            msg = QMessageBox()
            msg.setWindowTitle("Saved")
            msg.setText("Image saved")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ThirdWindow = QtWidgets.QMainWindow()
    ui = Ui_ThirdWindow()
    ui.setupUi(ThirdWindow)
    ThirdWindow.show()
    sys.exit(app.exec_())
