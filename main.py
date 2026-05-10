import sys
from PySide6.QtWidgets import QApplication
from controller import TemperatureController


def main():
    """
    Entry point: initialise QApplication, create the Controller
    (which owns the View and Model), show the window, start the event loop.
    """
    app = QApplication(sys.argv)
    window = TemperatureController()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
