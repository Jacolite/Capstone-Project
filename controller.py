from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

from model import TemperatureModel
from view import Ui_MainWindow


class TemperatureController(QMainWindow):
    """
    Controller: Acts as the 'glue' between View and Model.
    - Loads the UI (View)
    - Connects signals (button clicks) to slots
    - Calls Model methods for logic
    - Updates View widgets with results
    """

    def __init__(self):
        super().__init__()

        # Set up the View (generated from view.ui via pyside6-uic)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Instantiate the Model
        self.model = TemperatureModel()

        # Connect signals to slots
        self.ui.convertButton.clicked.connect(self.handle_convert)
        self.ui.clearButton.clicked.connect(self.handle_clear)

        # Allow pressing Enter in the input field to trigger conversion
        self.ui.celsiusInput.returnPressed.connect(self.handle_convert)

    # Slots 

    def handle_convert(self):
        """Read input, validate via Model, compute result, update View."""
        raw_text = self.ui.celsiusInput.text()

        is_valid, celsius_value = self.model.validate_input(raw_text)

        if not is_valid:
            self.ui.errorLabel.setText("⚠ Please enter a valid number.")
            self.ui.resultLabel.setText("Result will appear here")
            return

        # Clear any previous error
        self.ui.errorLabel.setText("")

        # Ask Model to perform the conversion
        self.model.set_celsius(celsius_value)
        fahrenheit = self.model.celsius_to_fahrenheit(celsius_value)

        # Update the View with the result
        self.ui.resultLabel.setText(
            f"{celsius_value:.2f} °C  =  {fahrenheit:.2f} °F"
        )

    def handle_clear(self):
        """Reset all View widgets and Model state."""
        self.ui.celsiusInput.clear()
        self.ui.resultLabel.setText("Result will appear here")
        self.ui.errorLabel.setText("")
        self.model.set_celsius(0.0)
        self.ui.celsiusInput.setFocus()
