import pyautogui, time, keyboard
def click(): 
    #time.sleep(0.25)  
    pyautogui.click()
def main():
    while True:
     click()
     pyautogui.moveRel(0,-40)
     click()
     pyautogui.moveRel(0,40)
while True:
 main()
 if keyboard.read_key() == "esc":
    break