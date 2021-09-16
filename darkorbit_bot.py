#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NRB SECURITY
from python_imagesearch.imagesearch import imagesearch
from pyautogui import leftClick
import pyautogui
from time import sleep
from random import randint
from os import system
from PyQt5 import QtWidgets,QtGui
import sys
uridium = 0
username = "NRB"
password = "sokaklarr"
kullanıcı_adı = pyautogui.prompt(text='Kullanıcı adınızı girin', title='NRB SECURİTY' , default='')
sifre = pyautogui.password(text='Şifrenizi giriniz.', title='NRB SECURİTY' , mask="*")
if username==kullanıcı_adı and sifre == password:
    pyautogui.alert(text='Giriş yapıldı', title='NRB SECURİTY', button="Tamam")
else:
    pyautogui.alert(text='Hatalı giriş!!', title='NRB SECURİTY', button="Tamam")
    exit()
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazı_alanı = QtWidgets.QLabel("NRB")
        self.buton = QtWidgets.QPushButton("NPC + Kutu")
        self.buton2 = QtWidgets.QPushButton("Sadece kutu")
        self.buton3 = QtWidgets.QPushButton("Pete toplat")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.buton2)
        v_box.addWidget(self.buton3)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.buton.clicked.connect(self.click)
        self.buton2.clicked.connect(self.click2)
        self.buton3.clicked.connect(self.click3)
        self.show()

    def click(self):
        print("Start")
        while True:
            try:
                print("Kurulumlar tamamdır")
                while True:
                    print("Döngü başladı")
                    try:
                        if imagesearch(image="lordakia.PNG")[0] != -1:
                            print("Lordakia görüldü")
                            try:
                                leftClick(imagesearch(image="lordakia.PNG"))
                                print("Lordaia tıklandı")
                            except:
                                leftClick(608, 396)
                                print("Error 564")
                                continue
                            leftClick(imagesearch(image="x2.PNG"))
                            print("X2 tıklandı")
                            leftClick(608, 396)
                            print("haritaya tıklandı")
                            print("Lordakia öldürüldü.")
                            uridium =uridium + 2
                            sleep(1)
                            print("Toplam {} uridium".format(uridium))
                            print("Lordaika süreci bitti")
                        elif imagesearch(image="kutu1.PNG")[0] != -1:
                            print("Kutu görüldü")
                            try:
                                leftClick(imagesearch(image="kutu1.PNG"))
                                print("Kutuya tıklandı")
                            except:
                                leftClick(608, 396)
                                print("Error 3549655")
                                continue
                            sleep(2)
                            print("Kutu toplandı")
                            sleep(1)
                            print("Kutu tamamlandı")
                        elif imagesearch(image="streuner.PNG")[0] != -1:
                            print("Streuner görüldü")
                            try:
                                leftClick(imagesearch(image="streuner.PNG")[0],
                                          imagesearch(image="streuner.PNG")[1] - 30)
                                print("Streuner tıklandı")
                            except:
                                leftClick(608, 396)
                                print("Error 354155")
                                continue
                            leftClick(imagesearch(image="x2.PNG")[0], imagesearch(image="x2.PNG")[1])
                            print("x2 tıklandı 63")
                            leftClick(608, 396)
                            print("Haritaya tıklandı 645")
                            print("Streuner öldürüldü")
                            uridium =uridium + 1
                            print("Toplam {} uridium".format(uridium))
                            sleep(1)
                        elif imagesearch(image="pet_health.PNG")[0] != -1:
                            print("Pet yakıtı tükendi")
                            try:
                                leftClick(imagesearch(image="nuy.PNG")[0], imagesearch(image="nuy.PNG")[1])
                                print("Yakıt alındı")
                                sleep(0.5)
                            except:
                                leftClick(608, 396)
                                print("Error 355")
                                continue
                            leftClick(imagesearch(image="start.PNG")[0],imagesearch(image="start.PNG")[1])
                            sleep(2)
                            leftClick(imagesearch(image="pasif.PNG")[0],imagesearch(image="pasif.PNG")[1])
                            sleep(1)
                            leftClick(imagesearch(image="otomatik.PNG")[0],imagesearch(image="otomatik.PNG")[1])
                            print("Pet aktif edildi")
                            sleep(2)
                        else:
                            leftClick(randint(1075, 1334), randint(519, 673))
                            print("Rastgele tıklandı")
                            sleep(2)
                    except:
                        leftClick(608, 396)
                        print("Error 35")
                        continue
            except:
                print("Sorun Oluştu 500")
                leftClick(608, 396)
                continue

            finally:
                leftClick(608, 396)
                system("python3 darkorbit_bot.py")
                continue
    def click2(self):
        while True:
            try:
                print("Kurulumlar tamamdır")
                while True:

                    try:
                        if imagesearch(image="kutu1.PNG")[0] != -1:
                            try:
                                leftClick(imagesearch(image="kutu1.PNG"))
                                sleep(2)
                                print("Kutu toplandı")
                            except:
                                print("Sorun Oluştu 502")
                                leftClick(608, 396)
                                continue
                            sleep(1)
                        else:
                            leftClick(randint(1075, 1334), randint(519, 673))
                            sleep(2)
                    except:
                        leftClick(608, 396)
                        continue
            except:
                print("Sorun Oluştu 400")
                leftClick(608, 396)
                continue

            finally:
                leftClick(608, 396)
                system("python3 darkorbit_bot.py")
                continue
    def click3(self):
        while True:
            try:
                print("Kurulumlar tamamdır")
                while True:

                    try:
                        leftClick(randint(1075, 1334), randint(519, 673))
                        sleep(2)
                    except:
                        leftClick(608, 396)
                        continue
            except:
                print("Sorun Oluştu 600")
                leftClick(608, 396)
                continue

            finally:
                leftClick(608, 396)
                system("python3 darkorbit_bot.py")
                continue


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
