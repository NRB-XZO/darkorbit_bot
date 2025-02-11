import cv2
import numpy as np
import pydirectinput
import keyboard
import time
import threading

# 📌 Ekran görüntüsü alıp OpenCV ile işleyerek hızlı nesne algılama yapar
def find_image(target, threshold=0.8, region=None):
    screen = np.array(pydirectinput.screenshot(region=region)) if region else np.array(pydirectinput.screenshot())
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
    template = cv2.imread(target, 0)
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    if len(loc[0]) > 0:
        return loc[1][0] + (region[0] if region else 0), loc[0][0] + (region[1] if region else 0)
    return None

# 📌 Çok hızlı tıklama için DirectInput kullanıyoruz
def fast_click(x, y, delay=0.1):
    pydirectinput.moveTo(x, y)
    pydirectinput.click()
    time.sleep(delay)

# 📌 Düşmanları tarayan ve ateş eden bot fonksiyonu
def enemy_hunter():
    while True:
        if keyboard.is_pressed('q'):
            print("[+] Bot Durduruldu")
            break

        enemies = ["saimon.PNG", "kristallin.PNG", "plagued_kristallin.PNG"]
        for enemy in enemies:
            pos = find_image(enemy, region=(300, 300, 800, 600))  # 🔥 Bölgesel tarama
            if pos:
                fast_click(pos[0], pos[1])
                pydirectinput.press("ctrl")  # Ateş etme tuşu
                time.sleep(0.1)

# 📌 Loot toplamak için bot fonksiyonu
def loot_collector():
    while True:
        if keyboard.is_pressed('q'):
            print("[+] Loot Bot Durduruldu")
            break

        loot_items = ["kutu1.PNG", "cubikon.PNG"]
        for item in loot_items:
            pos = find_image(item, region=(300, 300, 800, 600))
            if pos:
                fast_click(pos[0], pos[1])
                time.sleep(0.1)

# 📌 Çoklu işlem başlatma
def start_bot():
    thread_enemy = threading.Thread(target=enemy_hunter)
    thread_loot = threading.Thread(target=loot_collector)

    thread_enemy.daemon = True
    thread_loot.daemon = True

    thread_enemy.start()
    thread_loot.start()

    thread_enemy.join()
    thread_loot.join()

if __name__ == "__main__":
    start_bot()
