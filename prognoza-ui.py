# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prognoza-ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QPushButton
import requests
from datetime import datetime

def PostaviIkonicu(kod):
    if kod >= 200 and kod <= 299:
        return "ikonice/grmljavina.png"
    elif kod >= 300 and kod <= 399:
        return "ikonice/oblacno2.png"
    elif kod >= 500 and kod <= 599:
        return "ikonice/kisa.png"
    elif kod >= 600 and kod <= 699:
        return "ikonice/sneg.png"
    elif kod >= 700 and kod <= 799:
        return "ikonice/magla.png"
    elif kod == 800:
        return "ikonice/sunce.png"
    elif kod == 801:
        return "ikonice/oblacno.png"
    elif kod >= 802 and kod <= 804:
        return "ikonice/oblacno2.png"

def PostaviVreme(kod):
    if kod >= 200 and kod <= 299:
        return "Grmljavina"
    elif kod >= 300 and kod <= 399:
        return "Veoma oblačno"
    elif kod >= 500 and kod <= 599:
        return "Kiša"
    elif kod >= 600 and kod <= 699:
        return "Sneg"
    elif kod >= 700 and kod <= 799:
        return "Magla"
    elif kod == 800:
        return "Sunčano"
    elif kod == 801:
        return "Oblačno"
    elif kod >= 802 and kod <= 804:
        return "Veoma oblačno"

def Pretraga():
    gradedit = ui.lineEdit
    ui.pushButton.setEnabled(False)
    
    try:
        url = "https://api.openweathermap.org/geo/1.0/direct?q="+gradedit.text()+"&appid=3354124a888af4ac90791c1372d604e3"
        r = requests.get(url).json()
        lat = str(r[0]["lat"])
        lon = str(r[0]["lon"])
        
        url2 = "https://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&units=metric&appid=3354124a888af4ac90791c1372d604e3"
        trvreme = requests.get(url2).json()
        
        print(trvreme)
        
        #Podaci
        Vlaznost = str(trvreme["main"]["humidity"])
        Vidljivost = str(round((trvreme["visibility"]/10000*100)))
        Temp = str(round(trvreme["main"]["temp"]))
        Pritisak = str(trvreme["main"]["pressure"])
        Vlaznost = str(trvreme["main"]["humidity"])
        IzlazakSunca = str(datetime.fromtimestamp(trvreme["sys"]["sunrise"]).strftime("%H:%M"))
        ZalazakSunca = str(datetime.fromtimestamp(trvreme["sys"]["sunset"]).strftime("%H:%M"))
        Vetar = str(trvreme["wind"]["speed"])
        VremeID = trvreme["weather"][0]["id"]
        
        '''
        print("Vlažnost vazduha: "+Vlaznost)
        print("Vidljivost: "+Vidljivost)
        print("Trenutna temperatura: "+Temp)
        print("Vazdusni pritisak: "+Pritisak+" mbar")
        print("Izlazak sunca: "+IzlazakSunca)
        print("Zalazak sunca: "+ZalazakSunca)
        print("Brzina vetra: "+Vetar+" m/s")
        '''

        print(f"Vlažnost vazduha: {Vlaznost}")
        print(f"Vidljivost: {Vidljivost}")
        print(f"Trenutna temperatura: {Temp}")
        print(f"Vazdusni pritisak: {Pritisak} mbar")
        print(f"Izlazak sunca: {IzlazakSunca}")
        print(f"Zalazak sunca: {ZalazakSunca}")
        print(f"Brzina vetra: {Vetar} m/s")
        
        ui.greska.setHidden(True)
        
        ui.grad.setText(ui.lineEdit.text().capitalize())
        ui.grad.setHidden(False)
        ui.label_2.setText(PostaviVreme(VremeID))
        ui.label_2.setHidden(False)
        ui.label_3.setText(Temp+"°")
        ui.label_3.setHidden(False)
        ui.label_4.setText("Vlažnost vazduha: "+Vlaznost+"%")
        ui.label_4.setHidden(False)
        ui.label_5.setText("Vidljivost: "+Vidljivost+"%")
        ui.label_5.setHidden(False)
        ui.label_6.setText("Vazdušni pritisak: "+Pritisak+" mbar")
        ui.label_6.setHidden(False)
        ui.label_7.setText("Brzina vetra: "+Vetar+" m/s")
        ui.label_7.setHidden(False)
        ui.label_8.setText("Izlazak sunca: "+IzlazakSunca)
        ui.label_8.setHidden(False)
        ui.label_9.setText("Zalazak sunca: "+ZalazakSunca)
        ui.label_9.setHidden(False)
        ui.slika.setPixmap(QtGui.QPixmap(PostaviIkonicu(VremeID)))
        ui.slika.setHidden(False)
        
        ui.pushButton.setEnabled(True)
    
    except:
        ui.pushButton.setEnabled(True)
        ui.greska.setHidden(False)
        
        ui.grad.setHidden(True)
        ui.label_2.setHidden(True)
        ui.label_3.setHidden(True)
        ui.label_4.setHidden(True)
        ui.label_5.setHidden(True)
        ui.label_6.setHidden(True)
        ui.label_7.setHidden(True)
        ui.label_8.setHidden(True)
        ui.label_9.setHidden(True)
        ui.slika.setHidden(True)
        
        print("Greska")
    
    # Postavljanje labela
    

class Ui_MainWindow(object):
    
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setFixedSize(640, 480)
        
        MainWindow.setStyleSheet("background-color:white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.slika = QtWidgets.QLabel(self.centralwidget)
        self.slika.setGeometry(QtCore.QRect(60, 250, 180, 180))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slika.sizePolicy().hasHeightForWidth())
        self.slika.setSizePolicy(sizePolicy)
        self.slika.setMinimumSize(QtCore.QSize(0, 0))
        self.slika.setMaximumSize(QtCore.QSize(180, 180))
        self.slika.setText("")
        self.slika.setPixmap(QtGui.QPixmap("ikonice/sunce.png"))
        self.slika.setScaledContents(True)
        self.slika.setAlignment(QtCore.Qt.AlignCenter)
        self.slika.setObjectName("slika")
        self.slika.setHidden(True)
        self.grad = QtWidgets.QLabel(self.centralwidget)
        self.grad.setGeometry(QtCore.QRect(70, 140, 350, 90))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.grad.setFont(font)
        self.grad.setStyleSheet("color:#263238;")
        self.grad.setObjectName("grad")
        self.grad.setHidden(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 210, 250, 24))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#263238")
        self.label_2.setObjectName("label_2")
        self.label_2.setHidden(True)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 300, 121, 81))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(52)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#263238")
        self.label_3.setObjectName("label_3")
        self.label_3.setHidden(True)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(180, 30, 331, 62))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("color:#263238;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setStyleSheet("color: #263238; border-radius:0; border: 1px solid #263238; padding:4px 15px;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("QPushButton {background-color: #2196F3; border: 1px solid  #2196F3;padding: 5px 15px;color:white;} QPushButton::hover{background-color: #263238; border: 1px solid  #263238;padding: 5px 15px;color:white;}")
        self.pushButton.setObjectName("pushButton") 
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(400, 170, 224, 151))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("color:#263238;")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_4.setHidden(True)
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#263238;")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_5.setHidden(True)
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#263238;")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.setHidden(True)
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#263238;")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_7.setHidden(True)
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#263238;")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_8.setHidden(True)
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:#263238;")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_9.setHidden(True)
        self.verticalLayout.addWidget(self.label_9)
        self.greska = QtWidgets.QLabel(self.centralwidget)
        self.greska.setGeometry(QtCore.QRect(230, 100, 251, 36))
        self.greska.setObjectName("greska")
        self.greska.setStyleSheet("color:red;")
        self.greska.setHidden(True)
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.greska.raise_()
        self.slika.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.grad.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vremenska prognoza"))
        self.grad.setText(_translate("MainWindow", "Beograd"))
        self.label_2.setText(_translate("MainWindow", "Sunčano"))
        self.label_3.setText(_translate("MainWindow", "36°"))
        self.label.setText(_translate("MainWindow", "Unesite ime grada"))
        self.pushButton.setText(_translate("MainWindow", "Pretraga"))
        self.label_4.setText(_translate("MainWindow", "Najniža dnevna: 26°"))
        self.label_5.setText(_translate("MainWindow", "Najviša dnevna: 37°"))
        self.label_6.setText(_translate("MainWindow", "Vazdušni pritisak: 1002 mbar"))
        self.label_7.setText(_translate("MainWindow", "Brzina vetra: 4 m/s"))
        self.label_8.setText(_translate("MainWindow", "Izlazak sunca: 04:51"))
        self.label_9.setText(_translate("MainWindow", "Zalazak sunca: 20:06"))
        self.greska.setText(_translate("MainWindow", "Greška prilikom pretrage grada"))
        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    
    dugme = ui.pushButton
    dugme.clicked.connect(Pretraga) # Klik na dugme
    
    
    
    MainWindow.show()
    sys.exit(app.exec_())
    
    
