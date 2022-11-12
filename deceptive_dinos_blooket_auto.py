import pyautogui, time, keyboard
def click(): 
    time.sleep(0.25)  
    pyautogui.click()
def main():
    while True:
     click()
     pyautogui.moveRel(-30,0)
     click()
     pyautogui.moveRel(30,0)
     click()
     click()
while True:
 main()
 if keyboard.read_key() == "esc":
    break