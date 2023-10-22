import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import pyautogui
from pyautogui import leftClick
from python_imagesearch.imagesearch import imagesearch
from time import sleep, time
from threading import Thread
import keyboard
from random import randint

class LoadingAnimation(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.movie = QtGui.QMovie("loading.gif")
        self.setMovie(self.movie)
        self.movie.start()
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(0,0)

class DarkOrbitBot(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.loading_animation = LoadingAnimation()
        self.init_ui()

        self.login_status = False
        self.start_time = None
        self.darkorbit_username = None
        self.darkorbit_password = None

    def init_ui(self):
        self.setWindowTitle('DarkOrbit Bot')
        self.setGeometry(100, 100, 400, 200)

        self.username = "NRB"
        self.password = "sokaklarr"

        self.layout = QtWidgets.QVBoxLayout()

        self.login_button = QtWidgets.QPushButton('Giriş Yap')
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.hesap_bilgileri_button = QtWidgets.QPushButton('Hesap Bilgileri')
        self.hesap_bilgileri_button.clicked.connect(self.hesap_bilgileri)
        self.layout.addWidget(self.hesap_bilgileri_button)
        self.hesap_bilgileri_button.setEnabled(False)

        self.bot_buttons = QtWidgets.QWidget()
        self.bot_layout = QtWidgets.QHBoxLayout()
        self.npc_kutu_button = QtWidgets.QPushButton('Ultra')
        self.npc_kutu_button.setEnabled(False)
        self.npc_kutu_button.clicked.connect(self.ultra)
        self.bot_layout.addWidget(self.npc_kutu_button)
        self.sadece_kutu_button = QtWidgets.QPushButton('Box')
        self.sadece_kutu_button.setEnabled(False)
        self.bot_layout.addWidget(self.sadece_kutu_button)
        self.tiklama_bot_button = QtWidgets.QPushButton('Click')
        self.tiklama_bot_button.setEnabled(False)
        self.bot_layout.addWidget(self.tiklama_bot_button)
        self.test_button = QtWidgets.QPushButton('Test')
        self.test_button.setEnabled(False)
        self.bot_layout.addWidget(self.test_button)
        self.bot_buttons.setLayout(self.bot_layout)
        self.layout.addWidget(self.bot_buttons)

        self.info_label = QtWidgets.QLabel('')
        self.layout.addWidget(self.info_label)

        self.timer_label = QtWidgets.QLabel('Çalışma Süresi: 00:00:00')
        self.layout.addWidget(self.timer_label)

        self.layout.addWidget(self.loading_animation)

        self.setLayout(self.layout)

    def login(self):
        self.loading_animation.show()

        kullanıcı_adı, ok = QtWidgets.QInputDialog.getText(self, 'Giriş', 'Kullanıcı adınızı girin:')
        sifre, ok = QtWidgets.QInputDialog.getText(self, 'Giriş', 'Şifrenizi girin:', QtWidgets.QLineEdit.Password)

        if kullanıcı_adı == self.username and sifre == self.password:
            self.info_label.setText('Giriş yapıldı')
            self.login_status = True
            self.hesap_bilgileri_button.setEnabled(True)
            self.npc_kutu_button.setEnabled(True)
            self.sadece_kutu_button.setEnabled(True)
            self.tiklama_bot_button.setEnabled(True)
            self.test_button.setEnabled(True)

            self.start_time = time()
        else:
            self.info_label.setText('Hatalı giriş!!')

        self.loading_animation.hide()

    def hesap_bilgileri(self):
        kullanıcı_adı, ok = QtWidgets.QInputDialog.getText(self, 'Hesap Bilgileri', 'Kullanıcı adınızı girin:')
        sifre, ok = QtWidgets.QInputDialog.getText(self, 'Hesap Bilgileri', 'Şifrenizi girin:', QtWidgets.QLineEdit.Password)

        self.darkorbit_username = kullanıcı_adı
        self.darkorbit_password = sifre

    def ultra(self):
        pyautogui.FAILSAFE = False
        sure1 = int(pyautogui.prompt(text='Küçük npc leri kaç sn de kessin ?', title='NRB SECURİTY', default=''))
        npcs = ["devolarium.PNG", "devolarium2.PNG", "devolarium3.PNG", "devolarium4.PNG", "devolarium5.PNG",
                "devolarium6.PNG", "devolarium7.PNG", "mordon.PNG", "lordakia.PNG", "streuner.PNG"]
        print("Bot ekranı taramak üzere beklemede")
        if imagesearch("portal.PNG")[0] != -1:
            pyautogui.alert(text="Portal tespit edildi. Gemi patlayınca x2 haritasında kesime devam edilecektir :)",
                            title="NRB SECURİTY", button="Tamam")
        sleep(5)
        if imagesearch("mini_harita.PNG")[0] != -1:
            print("Mini harita bulundu")
            coordinat1 = int(imagesearch("mini_harita.PNG")[0])
            coordinat2 = int(imagesearch("mini_harita.PNG")[1])
            reel_coordinat_x1 = coordinat1 + 16
            reel_coordinat_x2 = coordinat1 + 293
            reel_coordinat_y1 = coordinat2 + 54
            reel_coordinat_y2 = coordinat2 + 218
        else:
            print("Mini harita algılanmadı")
            exit()
        while True:
            try:
                for i in range(1, 40):
                    if i in (3, 7):
                        leftClick(randint(int(reel_coordinat_x1), int(reel_coordinat_x2)),
                                  randint(int(reel_coordinat_y1), int(reel_coordinat_y2)))
                    if imagesearch("mordon.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch("mordon.PNG")[0], imagesearch("mordon.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(sure1)
                    if imagesearch("tamir.PNG")[0] != -1:
                        leftClick(imagesearch("tamir.PNG")[0], imagesearch("tamir.PNG")[1])
                        sleep(10)
                        leftClick(imagesearch("portal.PNG")[0] + 14, imagesearch("portal.PNG")[1] + 11)
                        sleep(100)
                        pyautogui.press("j")
                    if imagesearch("lordakia.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch("lordakia.PNG")[0], imagesearch("lordakia.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(sure1)
                    if imagesearch("streuner.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch("streuner.PNG")[0], imagesearch("streuner.PNG")[1] - 10)
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(sure1)
                    if imagesearch("boss.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch("boss.PNG")[0], imagesearch("boss.PNG")[1] - 10)
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(3 * sure1)
                    if imagesearch("saimon.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch("saimon.PNG")[0], imagesearch("saimon.PNG")[1] - 10)
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(1)
                    if imagesearch("kutu1.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(2)
                        leftClick(imagesearch("kutu1.PNG")[0] + 25, imagesearch("kutu1.PNG")[1])
                        sleep(4)
                    if imagesearch("kristallin.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch("kristallin.PNG")[0], imagesearch("kristallin.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(5)
                    if imagesearch("plagued_kristallin.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch("plagued_kristallin.PNG")[0], imagesearch("plagued_kristallin.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(5)
                    if imagesearch("boss_kristallin.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch("boss_kristallin.PNG")[0], imagesearch("boss_kristallin.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(10)
                    if imagesearch("kristallon.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch("kristallon.PNG")[0], imagesearch("kristallon.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(30)
                    if imagesearch("cubikon.PNG")[0] != -1:
                        leftClick(546, 468)
                        sleep(1)
                        leftClick(imagesearch("cubikon.PNG")[0], imagesearch("cubikon.PNG")[1])
                        sleep(0.5)
                        pyautogui.press("ctrl")
                        sleep(30)
                    if keyboard.is_pressed('q'):
                        print("[+] Out")
                        break
            except:
                continue

    def update_timer(self):
        while True:
            if self.start_time:
                elapsed_time = time() - self.start_time
                hours, remainder = divmod(elapsed_time, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.timer_label.setText(f'Çalışma Süresi: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}')
                sleep(1)

def main():
    app = QtWidgets.QApplication(sys.argv)
    darkorbit_bot = DarkOrbitBot()
    darkorbit_bot.show()
    timer_thread = Thread(target=darkorbit_bot.update_timer)
    timer_thread.daemon = True
    timer_thread.start()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
