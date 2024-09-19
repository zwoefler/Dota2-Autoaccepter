import unittest
from unittest.mock import patch
import cv2
from autoaccepter.template_matcher import load_templates, find_accept_button

class FunctionalTestAutoAccepter(unittest.TestCase):
    """
    Test if the script finds the accept button.
    """

    @classmethod
    def setUpClass(cls):
        """
        Load templates once for all tests
        """

        template_paths = [
            'templates/accept_button_1.png', 
            'templates/accept_button_2.png', 
            'templates/accept_button_3.png'
        ]
        cls.templates = load_templates(template_paths)
        cls.thresholds = [0.84, 0.81, 0.84]

    def test_accept_button_found(self):
        """
        DotA Accept screen
        """

        screenshot = cv2.imread('resources/test_match_found.png')
        self.assertTrue(find_accept_button(self.templates, self.thresholds, screenshot))


    def test_accept_button_found_dota_plus(self):
        """
        DotA-Plus Accept screen
        """

        screenshot = cv2.imread('resources/test_match_found_dota_plus.png')
        self.assertTrue(find_accept_button(self.templates, self.thresholds, screenshot))


    def test_accept_button_found_dota_plus_hover_accept_button(self):
        """
        DotA-Plus Accept screen when mouse is hovering accept button
        """
        screenshot = cv2.imread('resources/test_match_found_dota_plus_hovering_button.png')
        self.assertTrue(find_accept_button(self.templates, self.thresholds, screenshot))


    def test_no_accept_button_in_international_24_main_menu(self):
        """
        Main Menu International 2024
        """
        screenshot = cv2.imread('resources/test_dota2_main_menu_international_2024.png')
        self.assertFalse(find_accept_button(self.templates, self.thresholds, screenshot))

    def test_ready_check_found(self):
        pass


if __name__ == '__main__':
    unittest.main()