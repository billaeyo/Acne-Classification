# -- coding: utf-8 --

# Form implementation generated from reading ui file 'classification.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import matplotlib.pyplot as plt

from PyQt5 import QtCore, QtGui, QtWidgets
from tensorflow.keras.models import load_model
#from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv #open cv
import numpy as np
#import matplotlib.pyplot as plt #untuk membuat grafik
#import pandas as pd #dataframe
from skimage.feature import greycomatrix, greycoprops
#import seaborn as sns 
#import os.path
#from PyQt5 import QtCore
#from PyQt5.QtGui import QImage,QPixmap,QIcon
#from PyQt5 import QtCore, QtGui, uic
#from PyQt5.QtWidgets import *
#from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QTextEdit, QDialog
#from sklearn.model_selection import train_test_split
import pickle
#from sklearn.neighbors import KNeighborsClassifier  ##sklearn library untuk knn classifier
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.neighbors import KNeighborsClassifier



class Ui_Classification(object):
    def setupUi(self, Classification):
        Classification.setObjectName("Classification")
        Classification.resize(922, 670)
        Classification.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Classification)
        self.centralwidget.setObjectName("centralwidget")
        #Label RGB
        self.groupBoxRGB = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxRGB.setGeometry(QtCore.QRect(50, 90, 301, 191))
        #font = QtGui.QFont()
        #font.setPointSize(12)
        #self.groupBoxRGB.setFont(font)
        self.groupBoxRGB.setObjectName("groupBoxRGB")
        self.labelRGB = QtWidgets.QLabel(self.groupBoxRGB)
        self.labelRGB.setGeometry(QtCore.QRect(20, 30, 261, 141))
        self.labelRGB.setFrameShape(QtWidgets.QFrame.Box)
        self.labelRGB.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelRGB.setText("")
        self.labelRGB.setScaledContents(True)
        self.labelRGB.setObjectName("labelRGB")
        
        #Label GRAYSCALE
        self.groupBoxGrayscale = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxGrayscale.setGeometry(QtCore.QRect(380, 90, 301, 191))
        """font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBoxGrayscale.setFont(font)"""
        self.groupBoxGrayscale.setObjectName("groupBoxGrayscale")
        self.labelGrayscale = QtWidgets.QLabel(self.groupBoxGrayscale)
        self.labelGrayscale.setGeometry(QtCore.QRect(20, 30, 261, 141))
        self.labelGrayscale.setFrameShape(QtWidgets.QFrame.Box)
        self.labelGrayscale.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelGrayscale.setText("")
        self.labelGrayscale.setScaledContents(True)
        self.labelGrayscale.setObjectName("labelGrayscale")
        
         #Label Histogram

        self.groupBoxHistogram = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxHistogram.setGeometry(QtCore.QRect(50, 290, 301, 191))
        """font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBoxGrayscale.setFont(font)"""
        self.groupBoxHistogram.setObjectName("groupBoxGrafik")
        self.labelHistogram = QtWidgets.QLabel(self.groupBoxHistogram)
        self.labelHistogram.setGeometry(QtCore.QRect(20, 30, 261, 141))
        self.labelHistogram.setFrameShape(QtWidgets.QFrame.Box)
        self.labelHistogram.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelHistogram.setText("")
        self.labelHistogram.setScaledContents(True)
        self.labelHistogram.setObjectName("labelHistogram")
        
        #Label Grafik
        self.groupBoxGrafik = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxGrafik.setGeometry(QtCore.QRect(380, 290, 301, 330))
        """font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBoxGrayscale.setFont(font)"""
        self.groupBoxGrafik.setObjectName("groupBoxGrafik")
        self.labelGrafik = QtWidgets.QLabel(self.groupBoxGrafik)
        self.labelGrafik.setGeometry(QtCore.QRect(20, 30, 261, 141))
        self.labelGrafik.setFrameShape(QtWidgets.QFrame.Box)
        self.labelGrafik.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelGrafik.setText("")
        self.labelGrafik.setScaledContents(True)
        self.labelGrafik.setObjectName("labelGrafik")
        """self.labelGrafikHis = QtWidgets.QLabel(self.groupBoxGrafik)
        self.labelGrafikHis.setGeometry(QtCore.QRect(20, 180, 261, 141))
        self.labelGrafikHis.setFrameShape(QtWidgets.QFrame.Box)
        self.labelGrafikHis.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelGrafikHis.setText("")
        self.labelGrafikHis.setScaledContents(True)
        self.labelGrafikHis.setObjectName("labelGrafik")
        
        #TABLE GLCM
        self.tableWidgetGLCM = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetGLCM.setGeometry(QtCore.QRect(50, 300, 631, 171))
        self.tableWidgetGLCM.setObjectName("tableWidgetGLCM")
        self.tableWidgetGLCM.setColumnCount(6)
        self.tableWidgetGLCM.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetGLCM.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetGLCM.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetGLCM.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetGLCM.setVerticalHeaderItem(3, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetGLCM.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetGLCM.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetGLCM.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetGLCM.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetGLCM.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetGLCM.setHorizontalHeaderItem(5, item)"""
        
        #GROUPBOX RGB / INPUT CITRA
        self.InputCitra = QtWidgets.QGroupBox(self.centralwidget)
        self.InputCitra.setGeometry(QtCore.QRect(710, 90, 181, 101))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.InputCitra.setFont(font)
        self.InputCitra.setObjectName("InputCitra")
        self.ButoonOpen = QtWidgets.QPushButton(self.InputCitra)
        self.ButoonOpen.setGeometry(QtCore.QRect(20, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.ButoonOpen.setFont(font)
        self.ButoonOpen.setObjectName("ButoonOpen")
        
        """self.ButtonReset = QtWidgets.QPushButton(self.InputCitra)
        self.ButtonReset.setGeometry(QtCore.QRect(20, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.ButtonReset.setFont(font)
        self.ButtonReset.setObjectName("ButtonReset")"""
        
        #Grafik DAN CNN
        self.Classification = QtWidgets.QGroupBox(self.centralwidget)
        self.Classification.setGeometry(QtCore.QRect(710, 330, 181, 101))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Classification.setFont(font)
        self.Classification.setObjectName("Classification")
        
        self.ButtonClassification = QtWidgets.QPushButton(self.Classification)
        self.ButtonClassification.setGeometry(QtCore.QRect(20, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.ButtonClassification.setFont(font)
        self.ButtonClassification.setObjectName("ButtonClassification")
        self.ButtonGrafik = QtWidgets.QPushButton(self.Classification)
        self.ButtonGrafik.setGeometry(QtCore.QRect(20, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.ButtonGrafik.setFont(font)
        self.ButtonGrafik.setObjectName("ButtonGrafik")
        
        self.groupBoxHasil = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxHasil.setGeometry(QtCore.QRect(50, 490, 301, 101))
        #font = QtGui.QFont()
        #font.setPointSize(12)
        #self.groupBoxHasil.setFont(font)
        self.groupBoxHasil.setObjectName("groupBoxHasil")
        self.lineHasil = QtWidgets.QLineEdit(self.groupBoxHasil)
        self.lineHasil.setGeometry(QtCore.QRect(30, 30, 251, 51))
        self.lineHasil.setObjectName("lineHasil")
        
        #GROUPBOX PREPROCESSING
        self.Preprocessing = QtWidgets.QGroupBox(self.centralwidget)
        self.Preprocessing.setGeometry(QtCore.QRect(710, 210, 181, 101))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Preprocessing.setFont(font)
        self.Preprocessing.setObjectName("Preprocessing")
        self.ButtonHistogram = QtWidgets.QPushButton(self.Preprocessing)
        self.ButtonHistogram.setGeometry(QtCore.QRect(20, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.ButtonHistogram.setFont(font)
        self.ButtonHistogram.setObjectName("ButtonHistogram")
        self.ButtonGrayscale = QtWidgets.QPushButton(self.Preprocessing)
        self.ButtonGrayscale.setGeometry(QtCore.QRect(20, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.ButtonGrayscale.setFont(font)
        self.ButtonGrayscale.setObjectName("ButtonGrayscale")
        
        #LABEL JUDUL
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 581, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 40, 581, 31))
        self.label_2.setObjectName("label_2")
        Classification.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Classification)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 922, 21))
        self.menubar.setObjectName("menubar")
        Classification.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Classification)
        self.statusbar.setObjectName("statusbar")
        Classification.setStatusBar(self.statusbar)

        self.retranslateUi(Classification)
        QtCore.QMetaObject.connectSlotsByName(Classification)

    def retranslateUi(self, Classification):
        _translate = QtCore.QCoreApplication.translate
        Classification.setWindowTitle(_translate("Classification", "MainWindow"))
        self.groupBoxRGB.setTitle(_translate("Classification", "RGB"))
        self.groupBoxGrayscale.setTitle(_translate("Classification", "Citra Grayscale"))
        self.groupBoxHistogram.setTitle(_translate("Classification", "Citra Histogram"))
        self.groupBoxGrafik.setTitle(_translate("Classification", "Grafik Citra Grayscale dan Histogram"))
             
        self.InputCitra.setTitle(_translate("Classification", "Input Citra"))
        self.ButoonOpen.setText(_translate("Classification", "Pilih Gambar"))
        #self.ButtonReset.setText(_translate("Classification", "Reset"))
        self.Classification.setTitle(_translate("Classification", "Grafik And Klasifikasi"))
        self.ButtonHistogram.setText(_translate("Classification", "Histogram"))
        self.ButtonGrafik.setText(_translate("Classification", "Grafik"))
        self.ButtonClassification.setText(_translate("Classification", "Klasifikasi"))
        self.groupBoxHasil.setTitle(_translate("Classification", "Jenis Jerawat "))
        self.Preprocessing.setTitle(_translate("Classification", "Preprocessing "))
        self.ButtonGrayscale.setText(_translate("Classification", "Grayscale"))
        self.label.setText(_translate("Classification", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">KLASIFIKASI JENIS JERAWAT DENGAN MENGGUNAKAN </span></p></body></html>"))
        self.label_2.setText(_translate("Classification", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">CONVOLUTIONAL NEURAL NETWORK</span></p></body></html>"))
        
        self.ButtonGrayscale.setEnabled(False)
        self.ButtonGrafik.setEnabled(False)
        self.ButtonHistogram.setEnabled(False)
        self.ButtonClassification.setEnabled(False)
        
        #self.ButtonReset.clicked.connect(self.ResetImages)
        self.ButoonOpen.clicked.connect(self.OpenImages)
        self.ButtonGrayscale.clicked.connect(self.konversigrayscale)
        self.ButtonGrafik.clicked.connect(self.prosesGrafik)
        self.ButtonHistogram.clicked.connect(self.konversiHistogram)
        self.ButtonClassification.clicked.connect(self.prosescnn)
        
    """def ResetImages(self):
        self.labelRGB(self.clear)
        self.labelGrayscale(self.clear)
        self.tableWidgetGLCM(self.clear)"""
    
    def OpenImages(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.labelRGB.width(),self.labelRGB.height())
            self.labelRGB.setPixmap(pixmap)
            self.labelRGB.setAlignment(QtCore.Qt.AlignCenter)
            self.file = fileName
            self.ButtonGrayscale.setEnabled(True)
            
        self.image = cv.imread(self.file, cv.COLOR_BGR2GRAY)
        self.processedImage = self.image.copy()
        # resizing the gray scale into 96x96, since we need a fixed common size for all the images in the dataset
        self.previewImage = cv.resize(self.processedImage,(96,96),interpolation=cv.INTER_AREA) #(lebar,tinggi)
        print(self.previewImage.shape)
        self.displayResize()   
    #output resize
    def displayResize(self):
        qFormat = QtGui.QImage.Format_Indexed8
        if len (self.previewImage.shape) == 3:
            if (self.previewImage.shape[2]) == 4:
                qFormat = QtGui.QImage.Format_RGBA8888
            else:
               qFormat = QtGui.QImage.Format_RGB888
        img1 = QtGui.QImage(self.previewImage, self.previewImage.shape[1], self.previewImage.shape[0],self.previewImage.strides[0], qFormat)
        img1 = img1.rgbSwapped()
        
        self.labelRGB.setPixmap(QtGui.QPixmap.fromImage(img1))
        self.labelRGB.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        #self.ButtonGrayscale.setEnabled(True)
    #Grayscale    
    def konversigrayscale(self):
        # Coverting the image into gray scale
        self.gray = cv.cvtColor(self.previewImage, cv.COLOR_BGR2GRAY)
        self.previewgray= self.gray
        
        # Normalize image to between 0 and 255
        #self.data=np.array(self.gray)/255.0
        #self.data=np.reshape(self.data,(96,96,1))
        #print(self.data.shape)
        self.displayGrayscale()
    def displayGrayscale(self):
        qFormat = QtGui.QImage.Format_Indexed8
        if len (self.previewgray.shape) == 3:
            if (self.previewgray.shape[2]) == 4:
                qFormat = QtGui.QImage.Format_RGBA8888
            else:
                qFormat = QtGui.QImage.Format_RGB888
        self.img1 = QtGui.QImage(self.previewgray, self.previewgray.shape[1], self.previewgray.shape[0], self.previewgray.strides[0], qFormat)
        self.img1 = self.img1.rgbSwapped()
        self.labelGrayscale.setPixmap(QtGui.QPixmap.fromImage(self.img1))
        self.labelGrayscale.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ButtonHistogram.setEnabled(True)
        self.ButtonClassification.setEnabled(True)
        
    def konversiHistogram(self):
        clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        self.cl1 = clahe.apply(self.previewgray)

        self.displayHistogram()
    def displayHistogram(self):
        qFormat = QtGui.QImage.Format_Indexed8
        if len (self.cl1.shape) == 3:
            if (self.cl1.shape[2]) == 4:
                qFormat = QtGui.QImage.Format_RGBA8888
            else:
                qFormat = QtGui.QImage.Format_RGB888
        
        self.img1 = QtGui.QImage(self.cl1, self.cl1.shape[1], self.cl1.shape[0], self.cl1.strides[0], qFormat)
        self.img1 = self.img1.rgbSwapped()
        self.labelHistogram.setPixmap(QtGui.QPixmap.fromImage(self.img1))
        self.labelHistogram.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ButtonGrafik.setEnabled(True)
    
    def prosesGrafik(self):
        # compute a grayscale histogram
        self.hist = cv.calcHist([self.previewgray], [0], None, [256], [0, 256])
        self.hist1 = cv.calcHist([self.cl1], [0], None, [256], [0, 256])
        print(self.hist)

        plt.plot(self.hist,'b', label='Grayscale')
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        plt.xlim([0, 256])
        plt.savefig('histo gray.png')
        plt.plot(self.hist1,'r', label='Histogram Equalization')
        plt.xlim([0, 256])
        plt.savefig('histo equalization.png')

        self.labelGrafik.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.graf = cv.imread('histo equalization.png', cv.COLOR_BGR2GRAY)
        qFormat = QtGui.QImage.Format_Indexed8
        if len (self.graf.shape) == 3:
            if (self.graf.shape[2]) == 4:
                qFormat = QtGui.QImage.Format_RGBA8888
            else:
                qFormat = QtGui.QImage.Format_RGB888
        self.grafik = QtGui.QImage(self.graf, self.graf.shape[1], self.graf.shape[0], self.graf.strides[0], qFormat)
        self.grafik = self.grafik.rgbSwapped()
        self.labelGrafik.setPixmap(QtGui.QPixmap.fromImage(self.grafik))
        self.labelGrafik.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        
    def prosescnn(self): 
        model = load_model("C:\\Users\\Luthfi Salsabilla\\Documents\\program skripsi\\best_model_2.h5")
        # Normalize image to between 0 and 255
        self.data=np.array(self.cl1)/255.0
        self.data=np.reshape(self.data,(96,96,1))
        print(self.data.shape)
        #data = [self.feature]
        self.data = self.data.reshape(-1,96,96,1)

        Hasil = model.predict(self.data)
        y_pred = np.argmax(Hasil)
        print(Hasil)
        print(y_pred)
        if (y_pred == 0):
            self.lineHasil.setText("blackheads")
        if (y_pred == 1):
            self.lineHasil.setText("cystic")
        if (y_pred == 2):
            self.lineHasil.setText("Nodules")
        if (y_pred == 3):
            self.lineHasil.setText("papules")
        if (y_pred == 4):
            self.lineHasil.setText("pustules")
        if (y_pred == 5):
            self.lineHasil.setText("whiteheads")

#if _name_ == "_main_":
import sys
app = QtWidgets.QApplication(sys.argv)
Classification = QtWidgets.QMainWindow()
ui = Ui_Classification()
ui.setupUi(Classification)
Classification.show()
sys.exit(app.exec_())