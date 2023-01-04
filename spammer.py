import pyautogui
import time
from termcolor import colored

def spam():
    text = input(colored('Enter text for send!\n   ', 'green'))
    count = input(colored('Enter count!\n   ', 'green'))
    print(colored('Click on \'Write a message...\'', 'red'))
    print(colored('    For it you have 5 seconds', 'red'))
    time.sleep(5)
    print(colored('If all is right, spam started ;)', 'green'))
    try:
        for i in range(int(count)):
            pyautogui.typewrite(text)
            pyautogui.press('enter')
    except:
        print(colored('    Input error:(', 'red'))
        
spam()
