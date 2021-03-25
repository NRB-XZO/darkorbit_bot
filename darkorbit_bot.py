#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NRB SECURITY
from python_imagesearch.imagesearch import imagesearch
from pyautogui import leftClick
from time import sleep
from random import randint
from os import system
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
                    sleep(1)
                elif imagesearch(image="kutu1.PNG")[0] != -1:
                    leftClick(imagesearch(image="kutu1.PNG"))
                    sleep(3)
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
        leftClick(608,396)
        continue

    finally:
        leftClick(608,396)
        system("python3 darkorbit_bot.py")
        continue