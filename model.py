class TemperatureModel:
    """
    Model: Holds application data and performs business logic.
    No dependency on Qt or PySide6 — pure Python.
    """

    def __init__(self):
        self._celsius = 0.0

    def set_celsius(self, value: float):
        """Store the current Celsius value."""
        self._celsius = value

    def get_celsius(self) -> float:
        return self._celsius

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9 / 5) + 32

    def validate_input(self, text: str) -> tuple[bool, float]:
        """
        Validate and parse a string as a float.
        Returns (is_valid, parsed_value).
        """
        try:
            value = float(text.strip())
            return True, value
        except ValueError:
            return False, 0.0
