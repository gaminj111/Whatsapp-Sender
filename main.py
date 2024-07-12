import pyautogui
import time
import csv
import random

# Constants
image_black_1 = "search_bar.png"
image_black_2 = "search_bar_2.png"
image_white_1 = "w_search_bar.png"
image_white_2 = "w_search_bar_2.png"
database = "db.csv"


# Primul rand ii numele contactului; al doilea ii mesajul; nu trebuie stearsa prima linie

print("DURING THE PROCES DO NOT TOUCH THE MOUSE OR KEYBOARD")
def locator(image1, image2, image3, image4):
    time.sleep(1.8)
    try:
        try:
            try:
                location = pyautogui.locateCenterOnScreen(image1, confidence=0.8)
                pyautogui.click(location, interval=0.27)
            except:
                location = pyautogui.locateCenterOnScreen(image2, confidence=0.8)
                pyautogui.click(location, interval=0.27)
            print("Black theme")
        except:
            try:
                location = pyautogui.locateCenterOnScreen(image3, confidence=0.8)
                pyautogui.click(location, interval=0.27)
            except:
                location = pyautogui.locateCenterOnScreen(image4, confidence=0.8)
                pyautogui.click(location, interval=0.27)
            print("""White theme
        (The program works better with the dark theme because of higher contrast between "elements)""")
        print(location)
        messager(database)
    except:
        print("Program did not find the location of searchbar or whatsapp is not visible\nPlease restart")


def messager(dbase):
    """
    a = 0
    time.sleep(2)
    while a == 0:
        try:
            location = pyautogui.locateCenterOnScreen('search_bar.png', confidence=0.8)
            pyautogui.click(location, interval=0.27)
        except:
            location = pyautogui.locateCenterOnScreen('search_bar_2.png', confidence=0.8)
            pyautogui.click(location, interval=0.27)
        print(location)
        a += 1
        """

    time.sleep(3)
    with open(dbase, newline='') as f:
        reader = csv.reader(f, skipinitialspace=True)
        next(f)
        for row in reader:
            random_interval = random.randint(25, 55)
            random_interval = random_interval / 100
            print(random_interval)
            var_name = row[0]
            var_message = row[1]
            time.sleep(0.32 + random_interval)
            pyautogui.typewrite(var_name, interval=random_interval)
            time.sleep(0.33 + random_interval)
            pyautogui.hotkey("enter", interval=random_interval)
            time.sleep(0.34 + random_interval)
            pyautogui.typewrite(var_message, interval=random_interval)
            time.sleep(0.35 + random_interval)
            pyautogui.hotkey("enter", interval=random_interval)
            time.sleep(0.31 + random_interval)
            pyautogui.leftClick(interval=random_interval)
            time.sleep(0.30 + random_interval)

def loading_screen():
    time.sleep(1)
    print("Starting", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".")
    time.sleep(0.5)


loading_screen()
locator(image_black_1, image_black_2, image_white_1, image_white_2)
print("Finished")