import pyautogui, time, keyboard
def click(): 
    while True:
    #time.sleep(0.25)  
     pyautogui.click()
     pyautogui.click()
def main():
    while True:
     click()
while True:
 main()
 if keyboard.read_key() == "esc":
    break