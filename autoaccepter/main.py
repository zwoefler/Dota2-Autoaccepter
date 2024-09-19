import argparse
import time
import pyautogui
from pynput import keyboard
from autoaccepter.template_matcher import load_templates, find_accept_button

VERSION = "1.0.0"
is_active = True

def show_license():
    """
    Prints the license information.
    """
    license_text = """
    MIT License

    © 2023 Your Name

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """
    print(license_text)


def toggle_autoaccept(key=None):
    """
    Toggle Autoaccept on and off when F11 is pressed.
    """

    global is_active
    if key == keyboard.Key.f11:
        is_active = not is_active
    status = "active" if is_active else "paused"
    print(f"DotA2-Autoaccepter is {status} (Press F11 to toggle)")


template_paths = [
    'templates/accept_button_1.png', 
    'templates/accept_button_2.png',
    'templates/accept_button_3.png'
]

def main():
    """
    Main function for DotA2-Autoaccepter.
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="DotA2-Autoaccepter. Automatically accept games when found."
    )

    parser.add_argument(
        "--version", action="store_true", help="Print the version of DotA2-Autoaccepter"
    )
    parser.add_argument(
        "--license", action="store_true", help="Print the license information"
    )

    args = parser.parse_args()

    if args.version:
        print(f"DotA2-Autoaccepter version: {VERSION}")
        return

    if args.license:
        show_license()
        return

    listener = keyboard.Listener(on_press=toggle_autoaccept)
    listener.start()

    print("Starting DotA2-Autoaccepter...")
    templates = load_templates(template_paths)
    thresholds = [0.84, 0.81, 0.84]  

    while True:
        if is_active:
            match = find_accept_button(templates, thresholds)
            if match:
                print("Button found, accepting game")
                pyautogui.press('enter')
            else:
                print("No match found.")
            print("### DotA2-Autoaccepter ###")
            print(" ")
        else:
            print("DotA2-Autoaccepter is paused. Press F11 to activate.")
        time.sleep(3)


if __name__ == '__main__':
    main()

