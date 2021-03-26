#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NRB SECURITY
from python_imagesearch.imagesearch import imagesearch
from pyautogui import leftClick
from time import sleep
from random import randint
from os import system
from PyQt5 import QtWidgets,QtGui
import sys
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
        while True:
            try:
                print("Kurulumlar tamamdır")
                while True:

                    try:
                        if imagesearch(image="lordakia.PNG")[0] != -1:
                            leftClick(imagesearch(image="lordakia.PNG"))
                            leftClick(imagesearch(image="x2.PNG"))
                            leftClick(608, 396)
                            print("Lordakia öldürüldü.")
                            sleep(0.5)
                        elif imagesearch(image="kutu1.PNG")[0] != -1:
                            leftClick(imagesearch(image="kutu1.PNG"))
                            sleep(2)
                            print("Kutu toplandı")
                            sleep(1)
                        elif imagesearch(image="streuner.PNG")[0] != -1:
                            leftClick(imagesearch(image="streuner.PNG")[0], imagesearch(image="streuner.PNG")[1] - 30)
                            leftClick(imagesearch(image="x2.PNG")[0], imagesearch(image="x2.PNG")[1])
                            leftClick(608, 396)
                            print("Streuner öldürüldü")
                            sleep(1)
                        else:
                            leftClick(randint(1075, 1334), randint(519, 673))
                            sleep(2)
                    except:
                        leftClick(608, 396)
                        continue
            except:
                print("Sorun Oluştu")
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
                            leftClick(imagesearch(image="kutu1.PNG"))
                            sleep(2)
                            print("Kutu toplandı")
                            sleep(1)
                        else:
                            leftClick(randint(1075, 1334), randint(519, 673))
                            sleep(2)
                    except:
                        leftClick(608, 396)
                        continue
            except:
                print("Sorun Oluştu")
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
                print("Sorun Oluştu")
                leftClick(608, 396)
                continue

            finally:
                leftClick(608, 396)
                system("python3 darkorbit_bot.py")
                continue
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
