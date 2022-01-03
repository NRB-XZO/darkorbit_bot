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
pyautogui.FAILSAFE = False
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
        pyautogui.FAILSAFE = False
        npcs = ["devolarium.PNG","devolarium2.PNG","devolarium3.PNG","devolarium4.PNG","devolarium5.PNG","devolarium6.PNG","devolarium7.PNG","mordon.PNG","lordakia.PNG","streuner.PNG"]
        while True:
            try:
                if imagesearch(image="devolarium.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="devolarium.PNG")[0],imagesearch(image="devolarium.PNG")[1])
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(20)
                if imagesearch(image="devolarium2.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="devolarium.PNG")[0],imagesearch(image="devolarium.PNG")[1])
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(20)
                if imagesearch(image="devolarium3.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="devolarium.PNG")[0],imagesearch(image="devolarium.PNG")[1])
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(20)
                if imagesearch(image="devolarium4.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="devolarium.PNG")[0],imagesearch(image="devolarium.PNG")[1])
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(20)
                if imagesearch(image="devolarium5.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="devolarium.PNG")[0],imagesearch(image="devolarium.PNG")[1])
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(20)
                if imagesearch(image="devolarium6.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="devolarium.PNG")[0],imagesearch(image="devolarium.PNG")[1])
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(20)
                if imagesearch(image="devolarium7.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="devolarium.PNG")[0],imagesearch(image="devolarium.PNG")[1])
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(20)
                if imagesearch(image="mordon.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="mordon.PNG")[0],imagesearch(image="mordon.PNG")[1])
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(5)
                if imagesearch(image="lordakia.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="lordakia.PNG")[0],imagesearch(image="lordakia.PNG")[1])
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(2)
                if imagesearch(image="streuner.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="streuner.PNG")[0],imagesearch(image="streuner.PNG")[1])
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(5)
                if imagesearch(image="boss.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="boss.PNG")[0],imagesearch(image="boss.PNG")[1]-10)
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(5)
                if imagesearch(image="saimon.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="saimon.PNG")[0],imagesearch(image="saimon.PNG")[1]-10)
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(3)
                if imagesearch(image="kutu1.PNG")[0] != -1:
                    leftClick(imagesearch(image="kutu1.PNG")[0],imagesearch(image="kutu1.PNG")[1])
                    sleep(3)
                if imagesearch(image="boss_mordon.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="boss_mordon.PNG")[0],imagesearch(image="boss_mordon.PNG")[1])
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(6)
                if imagesearch(image="devolarium_spe.PNG")[0] != -1:
                    sleep(0.5)
                    leftClick(imagesearch(image="devolarium_spe.PNG")[0],imagesearch(image="devolarium_spe.PNG")[1]-10)
                    sleep(0.5)
                    leftClick(imagesearch(image="x2.PNG")[0],imagesearch(image="x2.PNG")[1])
                    sleep(9)
                else:
                    leftClick(randint(1075, 1334), randint(519, 673))
                    sleep(2)
            except:
                continue

    def click2(self):
        pyautogui.FAILSAFE = False
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
                            sleep(0.5)
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
