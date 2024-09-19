import time
import pyautogui
from autoaccepter.template_matcher import load_templates, find_accept_button

template_paths = [
    'templates/accept_button_1.png', 
    'templates/accept_button_2.png',
    'templates/accept_button_3.png'
]

templates = load_templates(template_paths)

thresholds = [0.84, 0.81, 0.84]  

def main():
    print("Starting Dota2 Accept Button Finder...")

    while True:
        match = find_accept_button(templates, thresholds)

        if match:
            print("Button found, accepting game")
            pyautogui.press('enter')
        else:
            print("No match found.")
        
        print("### Dota2-Autoaccepter ###")
        print(" ")
        time.sleep(3)


if __name__ == '__main__':
    main()

