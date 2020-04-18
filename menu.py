# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from os import getcwd
import cv2
import img_function as predict
import img_math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1271, 803)
        MainWindow.setStyleSheet("color: rgb(0, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(320, 40, 132, 30))
        self.label_author.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_author.setFont(font)
        self.label_author.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_author.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_author.setObjectName("label_author")
        self.label_picResult = QtWidgets.QLabel(self.centralwidget)
        self.label_picResult.setGeometry(QtCore.QRect(720, 490, 41, 41))
        self.label_picResult.setStyleSheet("border-image: url(:/newPrefix/images_test/result.png);")
        self.label_picResult.setText("")
        self.label_picResult.setObjectName("label_picResult")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(780, 320, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_result.setObjectName("label_result")
        self.label_scanResult = QtWidgets.QLabel(self.centralwidget)
        self.label_scanResult.setGeometry(QtCore.QRect(790, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label_scanResult.setFont(font)
        self.label_scanResult.setObjectName("label_scanResult")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(80, 10, 271, 30))
        self.label_title.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(22)
        font.setItalic(True)
        self.label_title.setFont(font)
        self.label_title.setAutoFillBackground(False)
        self.label_title.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_title.setObjectName("label_title")
        self.label_picTime = QtWidgets.QLabel(self.centralwidget)
        self.label_picTime.setGeometry(QtCore.QRect(730, 50, 38, 38))
        self.label_picTime.setStyleSheet("border-image: url(:/newPrefix/images_test/net_speed.png);")
        self.label_picTime.setText("")
        self.label_picTime.setObjectName("label_picTime")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(630, 250, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(860, 250, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1070, 250, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 90, 531, 381))
        self.label1.setStyleSheet("\n"
"border-image: url(:/newPrefix/images_test/green.png);")
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.label_result_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_result_2.setGeometry(QtCore.QRect(780, 400, 120, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_result_2.setFont(font)
        self.label_result_2.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_result_2.setObjectName("label_result_2")
        self.label_result_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_result_3.setGeometry(QtCore.QRect(920, 320, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_result_3.setFont(font)
        self.label_result_3.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_result_3.setObjectName("label_result_3")
        self.label_result_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_result_4.setGeometry(QtCore.QRect(920, 400, 120, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_result_4.setFont(font)
        self.label_result_4.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_result_4.setObjectName("label_result_4")
        self.label_result_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_result_5.setGeometry(QtCore.QRect(1100, 320, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_result_5.setFont(font)
        self.label_result_5.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_result_5.setObjectName("label_result_5")
        self.label_result_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_result_6.setGeometry(QtCore.QRect(1090, 410, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_result_6.setFont(font)
        self.label_result_6.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_result_6.setObjectName("label_result_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 160, 161, 61))
        self.label_5.setStyleSheet("background-image: url(:/newPrefix/images_test/green.png);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(810, 160, 161, 61))
        self.label_6.setStyleSheet("background-image: url(:/newPrefix/images_test/green.png);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1030, 160, 151, 61))
        self.label_7.setStyleSheet("background-image: url(:/newPrefix/images_test/green.png);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(560, 330, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(560, 400, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(560, 550, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(560, 640, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_scanResult_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_scanResult_2.setGeometry(QtCore.QRect(800, 490, 201, 31))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label_scanResult_2.setFont(font)
        self.label_scanResult_2.setObjectName("label_scanResult_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(720, 550, 161, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_result_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_result_7.setGeometry(QtCore.QRect(740, 650, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_result_7.setFont(font)
        self.label_result_7.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_result_7.setObjectName("label_result_7")
        self.toolButton_file = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file.setGeometry(QtCore.QRect(30, 550, 50, 40))
        self.toolButton_file.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_file.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_file.setAutoFillBackground(False)
        self.toolButton_file.setStyleSheet("background-color: transparent;")
        self.toolButton_file.setText("")
        icon = QtGui.QIcon()

        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/recovery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_file.setIcon(icon)
        self.toolButton_file.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_file.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_file.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_file.setAutoRaise(False)
        self.toolButton_file.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_file.setObjectName("toolButton_file")

        self.toolButton_camera = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_camera.setGeometry(QtCore.QRect(900, 550, 50, 45))
        self.toolButton_camera.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_camera.setMaximumSize(QtCore.QSize(50, 45))
        self.toolButton_camera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_camera.setAutoFillBackground(False)
        self.toolButton_camera.setStyleSheet("background-color: transparent;")
        self.toolButton_camera.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/g1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_camera.setIcon(icon1)
        self.toolButton_camera.setIconSize(QtCore.QSize(50, 39))
        self.toolButton_camera.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_camera.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_camera.setAutoRaise(False)
        self.toolButton_camera.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_camera.setObjectName("toolButton_camera")


        self.textEdit_pic = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic.setGeometry(QtCore.QRect(80, 560, 360, 30))
        self.textEdit_pic.setMinimumSize(QtCore.QSize(360, 30))
        self.textEdit_pic.setMaximumSize(QtCore.QSize(360, 30))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_pic.setFont(font)
        self.textEdit_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_pic.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.textEdit_pic.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_pic.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_pic.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_pic.setReadOnly(True)
        self.textEdit_pic.setObjectName("textEdit_pic")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1271, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #函数定义
        self.toolButton_file.clicked.connect(self.choose_pic)
        self.toolButton_camera.clicked.connect(self.start)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_author.setToolTip(_translate("MainWindow", "Test Result Helper 3.3.10 author：WuXian （2019.3.13）"))
        self.label_author.setText(_translate("MainWindow", "**人设计"))
        self.label_result.setText(_translate("MainWindow", "None"))
        self.label_scanResult.setText(_translate("MainWindow", "<html><head/><body><p>停车位示意图<br/></p></body></html>"))
        self.label_title.setToolTip(_translate("MainWindow", "Test Result Helper 3.3.10 author：WuXian （2019.3.13）"))
        self.label_title.setText(_translate("MainWindow", "车牌识别系统"))
        self.label2.setText(_translate("MainWindow", "  0   0   1"))
        self.label3.setText(_translate("MainWindow", "0  0   2"))
        self.label_3.setText(_translate("MainWindow", "0  0   3"))
        self.label_result_2.setText(_translate("MainWindow", "None"))
        self.label_result_3.setText(_translate("MainWindow", "None"))
        self.label_result_4.setText(_translate("MainWindow", "None"))
        self.label_result_5.setText(_translate("MainWindow", "None"))
        self.label_result_6.setText(_translate("MainWindow", "None"))
        self.label_5.setText(_translate("MainWindow", "       NULL"))
        self.label_6.setText(_translate("MainWindow", "        NULL"))
        self.label_7.setText(_translate("MainWindow", "       NULL"))
        self.label_8.setText(_translate("MainWindow", "车牌定位结果"))
        self.label_9.setText(_translate("MainWindow", "车牌识别效果"))
        self.label_10.setText(_translate("MainWindow", "反向寻车："))
        self.label_11.setText(_translate("MainWindow", "查询结果："))
        self.label_scanResult_2.setText(_translate("MainWindow", "<html><head/><body><p>查询车辆</p></body></html>"))
        self.label_result_7.setText(_translate("MainWindow", "None"))
        self.textEdit_pic.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">加载视频</p></body></html>"))
    def choose_pic(self):

        self.path = getcwd()
        self.predictor = predict.CardPredictor()
        self.predictor.train_svm()


        self.car1="你"
        self.car2="我"
        self.car3="他"



        #界面处理
        fileName_choose, filetype = QFileDialog.getOpenFileName(
                                self.centralwidget, "选取图片文件",
                                self.path,  # 起始路径
                                "视频(*.mp4)") # 文件类型      
        print(fileName_choose)
        self.textEdit_pic.setText(fileName_choose+'文件已选中')
        self.label1.setText('正在启动识别系统...\n\nleading')
        self.cap = cv2.VideoCapture(fileName_choose)
        i = 0
        while self.cap.isOpened():
            flag, im_rd = self.cap.read()

            frameClone = im_rd.copy()  # 复制画面

            self.key1 = cv2.resize(frameClone[200:800,150:650],(600,600))
            cv2.rectangle(frameClone, (150, 200), ( 650, 800), (255, 255, 0), 2)
            
            self.key2 = cv2.resize(frameClone[200:800,700:1200],(800,800))
            cv2.rectangle(frameClone, (700, 200), ( 1200, 800), (0, 255, 0), 2)
            self.key3 = cv2.resize(frameClone[200:800,1300:1800],(800,800))
            cv2.rectangle(frameClone, (1300, 200), ( 1800, 800), (255, 0, 0), 2)
            frameClone = cv2.resize(frameClone,(520,410))

                # 在Qt界面中显示人脸
            show = cv2.cvtColor(frameClone, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
            self.label1.setPixmap(QtGui.QPixmap.fromImage(showImage))
            QtWidgets.QApplication.processEvents()
            i = i+1
            if i == 400: # 50秒响应一次
                i = 0
                #print((self.key1).type)
                #cv2.imshow("ok",self.key2)
                #img_bgr = cv2.imdecode(self.key1, cv2.IMREAD_COLOR)
                #img_bgr = img_math.img_read("C:/Users/Administrator/Desktop/carddete/img_data/1586768004.jpg")
               # cv2.imshow("dsad",self.key1)
               
               



                    #第1个

                first_img2, oldimg2 = self.predictor.img_first_pre(self.key1)
                #r_color2, roi_color2, color_color2 = self.predictor.img_color_contours(first_img2, oldimg2)     #字符，定位图像，车牌颜色
                r_color2, roi_color2, color_color2 = self.predictor.img_only_color(oldimg2, oldimg2, first_img2)

                if len(r_color2) >4:
                    
                    self.label_5.setStyleSheet("background-image: url(:/newPrefix/images_test/red.png);")
                    img1= cv2.resize(roi_color2,(100,20))
                    #cv2.imshow("ok",img1)
                    showImage = QtGui.QImage(img1.data, img1.shape[1], img1.shape[0], QtGui.QImage.Format_RGB888)
                    self.label_result.setPixmap(QtGui.QPixmap.fromImage(showImage))
                    self.label_result_2.setText(r_color2)
                    self.label_5.setText(r_color2)
                    self.car1 = r_color2
                    print(str(self.car1))
                else :
                    self.label_5.setStyleSheet("background-image: url(:/newPrefix/images_test/green.png);")
                    self.label_5.setText("NULL")

                    
                    

                    



                    #第三个
                first_img, oldimg = self.predictor.img_first_pre(self.key3)
               # r_c, roi_c, color_c = self.predictor.img_color_contours(first_img, oldimg)     #字符，定位图像，车牌颜色
                r_color, roi_color, color_color = self.predictor.img_only_color(oldimg, oldimg, first_img)
               # print( "|", color_c, r_c, "|", color_color, r_color, "| ")
               # print(len(r_c))

                if len(r_color) >4:
                    
                    self.label_7.setStyleSheet("background-image: url(:/newPrefix/images_test/red.png);")
                    img1= cv2.resize(roi_color,(100,20))
                    #cv2.imshow("ok",img1)
                    showImage = QtGui.QImage(img1.data, img1.shape[1], img1.shape[0], QtGui.QImage.Format_RGB888)
                    self.label_result_5.setPixmap(QtGui.QPixmap.fromImage(showImage))
                    self.label_result_6.setText(r_color)
                    self.label_7.setText(r_color)
                    self.car3 = r_color
                    #continue
                else :
                    self.label_7.setStyleSheet("background-image: url(:/newPrefix/images_test/green.png);")
                    self.label_7.setText("NULL")
                    #self.car3 = "0"

                first_img1, oldimg1 = self.predictor.img_first_pre(self.key2)
                r_color1, roi_color1, color_color1 = self.predictor.img_only_color(oldimg1, oldimg1, first_img1)


                if len(r_color1) >4:
                    
                    self.label_6.setStyleSheet("background-image: url(:/newPrefix/images_test/red.png);")
                    img1= cv2.resize(roi_color1,(100,20))
                    #cv2.imshow("ok",img1)
                    showImage = QtGui.QImage(img1.data, img1.shape[1], img1.shape[0], QtGui.QImage.Format_RGB888)
                    self.label_result_3.setPixmap(QtGui.QPixmap.fromImage(showImage))
                    self.label_result_4.setText(r_color1)
                    self.label_6.setText(r_color1)
                    self.car2 = r_color1
                    print("ok")
                    print((self.car2))
                else :
                    self.label_6.setStyleSheet("background-image: url(:/newPrefix/images_test/green.png);")
                    self.label_6.setText("NULL")
                    #self.car1 = "0"

                

    def start(self):
        self.name = self.lineEdit.text()   #获取文本框内容
        print(self.name)
        print(self.car2)
        if  self.name == self.car1 :
            self.label_result_7.setText("车位一")           
        if self.name == self.car2 :
            self.label_result_7.setText("车位二")
        if  self.name == self.car3 :
            self.label_result_7.setText("车位三")



                











import image1_rc
