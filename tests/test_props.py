"""
Unit test for Props class.
"""

import unittest
from unittest.mock import MagicMock
from props import Props  # type: ignore


class TestProps(unittest.TestCase):
    """
    Test Props class.
    """
    def setUp(self):
        """
        Initialize the Props class.
        """
        self.app = MagicMock()
        self.props = Props(self.app)
        self.assertIsInstance(self.props, Props)

    def test_default_values(self):
        """
        Test default values of the Props class.
        """
        self.assertEqual(self.props.WIDTH,
                         int(self.app.winfo_screenwidth() * 0.21))
        self.assertEqual(self.props.HEIGHT,
                         int(self.app.winfo_screenheight() * 0.6))
        self.assertEqual(self.props.BACKGROUND_DARK, '#014F86')
        self.assertEqual(self.props.BACKGROUND_LIGHT, '#89C2D9')
        self.assertEqual(self.props.BUTTON_COLOR, '#A9D6E5')
        self.assertEqual(self.props.APP_NAME, 'Solace')
        self.assertEqual(self.props.GRADIENT, 'NightTrain.json')
        self.assertEqual(self.props.THEME, 'dark')
        self.assertEqual(self.props.SLIDERBUTTON, '#012A4A')
