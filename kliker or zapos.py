import pyautogui
import time
i=(input("введите кликер или запрос"))
if i=="кликер":
    time.sleep(1)
    pyautogui.moveTo(330,760)
    pyautogui.click(button ="left")
    pyautogui.moveTo(600,350)
    while(True):
        pyautogui.click(button = "left")
elif i=="запрос":
    i=(input("Введите что нужно найти "))
    time.sleep(1)
    pyautogui.moveTo(150,760)
    pyautogui.click(button = "left")
    time.sleep(1)
    pyautogui.moveTo(1150,10)
    pyautogui.click(button = "left")
    time.sleep(1)
    pyautogui.moveTo(700,440)
    pyautogui.click(button = "left")
    time.sleep(1)
    pyautogui.write(i, interval=0.50)
    pyautogui.press('enter')
    

