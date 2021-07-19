from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtGui import QImage, QPixmap
import cv2
from datetime import datetime 
from detectObject import *
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("QMainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setWindowTitle("Sketch2Code")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.player = QtWidgets.QLabel(self.centralwidget)
        self.player.setGeometry(QtCore.QRect(50, 20, 700, 960))
        self.player.setStyleSheet("border: 1px solid black;")
        self.player.setObjectName("Player")

        self.player1 = QtWidgets.QLabel(self.centralwidget)
        self.player1.setGeometry(QtCore.QRect(1150, 20, 700, 960))
        self.player1.setStyleSheet("border: 1px solid black;")
        self.player1.setObjectName("Player")

        self.SelectImage = QtWidgets.QPushButton(self.centralwidget)
        self.SelectImage.setGeometry(QtCore.QRect(180, 60, 180, 60))
        self.SelectImage.setStyleSheet("font: 75 16pt \"Times New Roman\";")
        self.SelectImage.setObjectName("Stop Camera")
        self.SelectImage.move(860, 320)

        self.GenerateHTML = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateHTML.setGeometry(QtCore.QRect(250, 60, 250, 60))
        self.GenerateHTML.setStyleSheet("font: 75 16pt \"Times New Roman\";")
        self.GenerateHTML.setObjectName("Start Camera")
        self.GenerateHTML.move(830, 420)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        return self

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.capture = False
        self.msg = QMessageBox()
        MainWindow.setWindowTitle(_translate("MainWindow", "Sketch2Code"))
        self.GenerateHTML.setText(_translate("MainWindow", "Generate HTML"))
        self.SelectImage.setText(_translate("MainWindow", "Select Image"))
        self.GenerateHTML.clicked.connect(self.generator)
        self.SelectImage.clicked.connect(self.uploadHandlerForImage)

    def onclick(self):
        if self.dropDown.currentText() != 'Web Camera' and self.dropDown.currentText() != 'Usb Camera':
            self.ips.setDisabled(False)
        else:
            self.ips.setDisabled(True)

    def uploadHandlerForImage(self):
        path = self.openDialogBoxForImage()
        image = path[0]
        self.displayImage(cv2.imread(image))

    def uploadHandlerForVideo(self):
        self.ret = True
        self.player.setEnabled(True)
        try:
            path = self.openDialogBoxForVideo()
            video = path[0]
            cap = cv2.VideoCapture(video)
            while (cap.isOpened()):
                ret, frame = cap.read()
                if frame is not None:
                    if self.ret:
                        if ret:
                            self.displayImage(frame)
                            cv2.waitKey()
                            if (self.capture == True):
                                self.imagePath = "Capture Images/"
                                self.name = "Capture_Image_" + str(int(datetime.timestamp(datetime.now())))
                                cv2.imwrite(
                                    self.imagePath + "%s.png" % (self.name), frame)
                                self.capture = False
                        else:
                            cap.release()
                            cv2.destroyAllWindows()
                            break
                    else:
                        cap.release()
                        self.player.clear()
                        cv2.destroyAllWindows()
                        break
                else:
                    self.player.clear()
                    break

            cap.release()
            cv2.destroyAllWindows()
            self.player.clear()

        except Exception as e:
            print(str(e))

    def displayImage(self, image):
        try:

            self.image = cv2.resize(image, (800, 800))

            qformat = QImage.Format_Indexed8
            if len(self.image.shape) == 3:
                if (self.image.shape[2]) == 4:
                    qformat = QImage.Format_RGB888
                else:
                    qformat = QImage.Format_RGB888

            img = QImage(self.image, self.image.shape[1], self.image.shape[0], qformat)
            img = img.rgbSwapped()
            self.player.setScaledContents(True)
            self.player.setPixmap(QPixmap.fromImage(img))

            detectedImage, self.instance = detectObject(self.image)
            qformat = QImage.Format_Indexed8
            if len(detectedImage.shape) == 3:
                if (detectedImage.shape[2]) == 4:
                    qformat = QImage.Format_RGB888
                else:
                    qformat = QImage.Format_RGB888

            img = QImage(detectedImage, detectedImage.shape[1], detectedImage.shape[0], qformat)
            img = img.rgbSwapped()
            self.player1.setScaledContents(True)
            self.player1.setPixmap(QPixmap.fromImage(img))

        except Exception as e:
            print(str(e))

    def generator(self):
        getStatus = genareteHTML(self.image, self.instance)
        self.msg.setWindowTitle('HTML Generate')
        self.msg.setText("Your HTML File is Generated!")
        self.msg.exec_()


    def openDialogBoxForImage(self):
        file = QFileDialog.getOpenFileName(self, 'Open file', '', "Image files (*.jpg *.jpeg *.png)")
        return file

    def openDialogBoxForVideo(self):
        file = QFileDialog.getOpenFileName(self, 'Open file', '', "Video files (*.mp4)")
        return file

    def startCamera(self, ip):
        self.ret = True
        self.player.setEnabled(True)
        cap = cv2.VideoCapture(int(ip))
        while (cap.isOpened()):
            ret, frame = cap.read()
            if frame is not None:
                if self.ret == True:
                    self.displayImage(frame)
                    cv2.waitKey()
                    if (self.capture == True):
                        self.name = "Capture_Image_" + str(int(datetime.timestamp(datetime.now())))
                        cv2.imwrite(
                            "Capture Images/%s.png" % (self.name), frame)
                        self.capture = False
                else:
                    cap.release()
                    cv2.destroyAllWindows()

            else:
                self.player1.clear()

        cap.release()
        cv2.destroyAllWindows()

    def configCamera(self):
        self.ip = self.dropDown.currentText()
        if self.ip == 'Web Camera':
            self.cameraIP = 0
            self.startCamera(self.cameraIP)

        elif self.ip == 'Usb Camera':
            self.cameraIP = 1
            self.startCamera(self.cameraIP)
        
        else:
            pass
            # self.ip = self.ips.toPlainText().split(",")
            # self.startCameras(self.ip)

    def startCameras(self, ips):
        ipLen = len(ips)
        for i in ips:
            if ipLen == 2:
                pass

    def stopCamera(self):
        self.ret = False
        self.player.clear()
        return self

    def pauseVideo(self):
        self.ret = False
        self.player.clear()
        return self

    def captureImage(self):
        self.capture=True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())

