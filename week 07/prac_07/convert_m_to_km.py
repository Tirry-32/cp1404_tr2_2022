"""
CP1404 - Practical
GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder

__author__ = 'Tirivashe Ushamba'

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation (could be button press or other call), output result to label widget."""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handle up/down button press, update the text input with new value, call handle_calculate() function."""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Get valid text input from text entry widget, convert to float and return 0 if for ValueError."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
