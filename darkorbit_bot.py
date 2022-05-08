#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NRB SECURITY
import keyboard
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
        self.buton3 = QtWidgets.QPushButton("Tıklama botu")
        self.buton4 = QtWidgets.QPushButton("Test")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.buton2)
        v_box.addWidget(self.buton3)
        v_box.addWidget(self.buton4)
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
        self.buton4.clicked.connect(self.click4)
        self.show()

    def click(self):
        pyautogui.FAILSAFE = False
        sure1 = int(pyautogui.prompt(text='Küçük npc leri kaç sn de kessin ?', title='NRB SECURİTY' , default=''))
        npcs = ["devolarium.PNG","devolarium2.PNG","devolarium3.PNG","devolarium4.PNG","devolarium5.PNG","devolarium6.PNG","devolarium7.PNG","mordon.PNG","lordakia.PNG","streuner.PNG"]
        print("Bot ekranı taramak üzere beklemede")
        if imagesearch(image="portal.PNG")[0] != -1:
            pyautogui.alert(text="Portal tespit edildi. Gemi patlayınca x2 haritasında kesime devam edilecektir :)",title="NRB SECURİTY",button="Tamam")
        sleep(5)
        if imagesearch(image="mini_harita.PNG")[0] != -1:
            print("Mini harita bulundu")
            coordinat1 = int(imagesearch(image="mini_harita.PNG")[0])
            coordinat2 = int(imagesearch(image="mini_harita.PNG")[1])
            reel_coordinat_x1 = coordinat1 + 16
            reel_coordinat_x2 = coordinat1 + 293
            reel_coordinat_y1 = coordinat2 + 54
            reel_coordinat_y2 = coordinat2 + 218
        else:
            print("Mini harita algılanmadı")
            exit()
        while True:
            try:
                for i in range(1,40):
                    if i == 3 or 7:
                        leftClick(randint(int(reel_coordinat_x1), int(reel_coordinat_x2)),randint(int(reel_coordinat_y1), int(reel_coordinat_y2)))
                    if imagesearch(image="mordon.PNG")[0] != -1:
                        leftClick(546,468)
                        sleep(1)
                        leftClick(imagesearch(image="mordon.PNG")[0], imagesearch(image="mordon.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(sure1)
                    if imagesearch(image="tamir.PNG")[0] != -1:

                        leftClick(imagesearch(image="tamir.PNG")[0],imagesearch(image="tamir.PNG")[1])
                        sleep(10)
                        leftClick(imagesearch(image="portal.PNG")[0]+14, imagesearch(image="portal.PNG")[1]+11)
                        sleep(100)
                        pyautogui.press("j")
                    if imagesearch(image="exit.PNG")[0] != -1:
                        leftClick(imagesearch(image="exit.PNG")[0]+2,imagesearch(image="exit.PNG")[1]+6)
                    if imagesearch(image="lordakia.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch(image="lordakia.PNG")[0], imagesearch(image="lordakia.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(sure1)
                    if imagesearch(image="streuner.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch(image="streuner.PNG")[0], imagesearch(image="streuner.PNG")[1] - 10)
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(sure1)
                    if imagesearch(image="boss.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch(image="boss.PNG")[0], imagesearch(image="boss.PNG")[1] - 10)
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(3*sure1)
                    if imagesearch(image="saimon.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch(image="saimon.PNG")[0], imagesearch(image="saimon.PNG")[1] - 10)
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(1)
                    if imagesearch(image="kutu1.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(2)
                        leftClick(imagesearch(image="kutu1.PNG")[0]+25, imagesearch(image="kutu1.PNG")[1])
                        sleep(4)
                    if imagesearch(image="boss_mordon.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch(image="boss_mordon.PNG")[0], imagesearch(image="boss_mordon.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(6)
                    if imagesearch(image="devolarium_spe.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch(image="devolarium_spe.PNG")[0],
                                  imagesearch(image="devolarium_spe.PNG")[1] - 10)
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(30)
                    if imagesearch(image="kristallin.PNG")[0] != -1:
                        leftClick(546,468)
                        sleep(1)
                        leftClick(imagesearch(image="kristallin.PNG")[0], imagesearch(image="kristallin.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(5)
                    if imagesearch(image="plagued_kristallin.PNG")[0] != -1:
                        leftClick(546,468)
                        sleep(1)
                        leftClick(imagesearch(image="plagued_kristallin.PNG")[0], imagesearch(image="plagued_kristallin.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(5)
                    if imagesearch(image="boss_kristallin.PNG")[0] != -1:
                        leftClick(546,468)
                        sleep(1)
                        leftClick(imagesearch(image="boss_kristallin.PNG")[0], imagesearch(image="boss_kristallin.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(10)
                    if imagesearch(image="kristallon.PNG")[0] != -1:
                        leftClick(546,468)
                        sleep(1)
                        leftClick(imagesearch(image="kristallon.PNG")[0], imagesearch(image="kristallon.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(30)
                    if imagesearch(image="cubikon.PNG")[0] != -1:
                        leftClick(546,468)
                        sleep(1)
                        leftClick(imagesearch(image="cubikon.PNG")[0], imagesearch(image="cubikon.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(30)
                    if keyboard.is_pressed('q'):
                        print("[+] Out")
                        break
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
                if keyboard.is_pressed('ctrl'):
                    while True:
                        if imagesearch(image="cubikon.PNG")[0] != -1:
                            leftClick(imagesearch(image="cubikon.PNG")[0], imagesearch(image="cubikon.PNG")[1]-10)
                        if imagesearch(image="kristallon.PNG")[0] != -1:
                            leftClick(imagesearch(image="kristallon.PNG")[0], imagesearch(image="kristallon.PNG")[1])
                        if imagesearch(image="boss_kristallin.PNG")[0] != -1:
                            leftClick(imagesearch(image="boss_kristallin.PNG")[0], imagesearch(image="boss_kristallin.PNG")[1])
                        if imagesearch(image="plagued_kristallin.PNG")[0] != -1:
                            leftClick(imagesearch(image="plagued_kristallin.PNG")[0], imagesearch(image="plagued_kristallin.PNG")[1])
                        if imagesearch(image="kristallin.PNG")[0] != -1:
                            leftClick(imagesearch(image="kristallin.PNG")[0], imagesearch(image="kristallin.PNG")[1])
                        if imagesearch(image="mordon.PNG")[0] != -1:
                            leftClick(imagesearch(image="mordon.PNG")[0], imagesearch(image="mordon.PNG")[1])
                        if imagesearch(image="lordakia.PNG")[0] != -1:
                            leftClick(imagesearch(image="lordakia.PNG")[0], imagesearch(image="lordakia.PNG")[1])
                        if imagesearch(image="streuner.PNG")[0] != -1:
                            leftClick(imagesearch(image="streuner.PNG")[0], imagesearch(image="streuner.PNG")[1] - 10)
                        if imagesearch(image="boss.PNG")[0] != -1:
                            leftClick(imagesearch(image="boss.PNG")[0], imagesearch(image="boss.PNG")[1] - 10)
                        if imagesearch(image="saimon.PNG")[0] != -1:
                            leftClick(imagesearch(image="saimon.PNG")[0], imagesearch(image="saimon.PNG")[1] - 10)
                        if imagesearch(image="kutu1.PNG")[0] != -1:
                            leftClick(imagesearch(image="kutu1.PNG")[0], imagesearch(image="kutu1.PNG")[1])
                        if imagesearch(image="boss_mordon.PNG")[0] != -1:
                            leftClick(imagesearch(image="boss_mordon.PNG")[0], imagesearch(image="boss_mordon.PNG")[1])
                        if imagesearch(image="devolarium_spe.PNG")[0] != -1:
                            leftClick(imagesearch(image="devolarium_spe.PNG")[0],
                                      imagesearch(image="devolarium_spe.PNG")[1] - 10)
                        if keyboard.is_pressed('q'):
                            break
            except:
                pyautogui.alert("Error")
    def click4(self):
        pyautogui.alert(text="x-1 veya x-8 haritasındayım. Onaylıyor musunuz ?", title="NRB SECURİTY", button="Onaylıyorum")
        sleep(3)
        leftClick(imagesearch(image="portal.PNG")[0]+14, imagesearch(image="portal.PNG")[1]+11)
        sleep(2)
        leftClick(imagesearch(image="exit.PNG")[0]+2, imagesearch(image="exit.PNG")[1]+6)


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
