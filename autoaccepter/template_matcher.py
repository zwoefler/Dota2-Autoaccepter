import sys
import os
import cv2
import numpy as np
from PIL import ImageGrab

def load_templates(template_paths):
    """
    Load template images of Accept button

    Args:
        template_paths (list): List of template image paths.

    Returns:
        list: List of tuples containing templates and their dimensions.
    """
    templates = []
    for path in template_paths:
        try:
            # PyInstaller stores files in a temporary _MEIPASS folder
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        template_path = os.path.join(base_path, path)
        template = cv2.imread(template_path, 0)
        template_w, template_h = template.shape[::-1]
        templates.append((template, template_w, template_h))
    return templates


def match_template(screenshot_gray, template, threshold=0.8):
    """
    Matches template to grayscale screenshot and checks the threshold.

    Args:
        screenshot_gray (np.ndarray): Grayscale screenshot.
        template (np.ndarray): Grayscale template image.
        threshold (float): Match threshold.

    Returns:
        tuple: (match_value, match_location) if match is found, else (None, None).
    """
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        return max_val, max_loc
    else:
        return None, None


def get_center_of_image(image_np):
    """
    Extract the center of the image.
    where the Accept button expected to appear.

    Args:
        image_np (np.ndarray): The input image as a NumPy array.

    Returns:
        tuple: The cropped center image, x-offset, and y-offset values.
    """
    height, width, _ = image_np.shape
    x_center_start = width // 4
    x_center_end = width - width // 4
    y_center_start = height // 4
    y_center_end = height - height // 4

    return image_np[y_center_start:y_center_end, x_center_start:x_center_end], x_center_start, y_center_start


def find_accept_button(templates, thresholds, screenshot=None):
    """
    Captures the screen.
    Finds the "Accept" button using button-edge templates.

    Args:
        templates (list): List of templates loaded from file.
        thresholds (list): List of matching thresholds for each template.
        screenshot (np.ndarray, optional): Test screenshot for testing.

    Returns:
        bool: True if all templates match, otherwise False.
    """
    if screenshot is None:
        screenshot = ImageGrab.grab()
        
    screenshot = np.array(screenshot)
    center_screenshot, x_offset, y_offset = get_center_of_image(screenshot)
    screenshot_gray = cv2.cvtColor(center_screenshot, cv2.COLOR_BGR2GRAY)

    results = []
    for idx, (template, threshold) in enumerate(zip(templates, thresholds)):
        match_val, match_loc = match_template(screenshot_gray, template[0], threshold=threshold)
        if match_val:
            results.append((match_val, match_loc, template[1], template[2]))

    if len(results) == len(templates):
        return True
    return False

