# Temperature Converter — MVC PySide6 App

## Description

A simple desktop application that converts temperatures from **Celsius to Fahrenheit**.  
The user types a Celsius value, clicks **Convert**, and the result is displayed instantly.  
Built with Python, PySide6, and Qt Designer, following the **Model–View–Controller (MVC)** pattern.

---

## MVC Overview

| Layer | File | Responsibility |
|-------|------|----------------|
| **Model** | `model.py` | Stores the current temperature value; validates input; performs the C → F calculation. Has **no** PySide6 dependency. |
| **View** | `view.ui` / `view.py` | UI layout created visually in **Qt Designer** and converted to Python via `pyside6-uic`. Contains only widgets — zero business logic. |
| **Controller** | `controller.py` | Loads the View, connects button-click signals to slots, asks the Model to process data, then updates View labels with results. |

**Flow:**
```
User clicks button
      ↓
Controller.handle_convert()   ← signal→slot connection
      ↓
Model.validate_input()
Model.celsius_to_fahrenheit()
      ↓
Controller updates resultLabel (View)
```

---

## Project Structure

```
temp_converter/
├── main.py         # Entry point — starts QApplication, shows window
├── model.py        # Business logic, no Qt dependency
├── controller.py   # Signal/slot wiring, bridges View ↔ Model
├── view.ui         # Qt Designer source file
├── view.py         # Auto-generated from view.ui via pyside6-uic
└── README.md
```

---

## How to Run

### 1. Install dependencies

```bash
pip install pyside6
```

### 2. (Optional) Regenerate `view.py` from the `.ui` file

```bash
pyside6-uic view.ui -o view.py
```

### 3. Run the application

```bash
python main.py
```

---

## Features

- Enter any Celsius temperature (decimals supported)
- Press **Convert** or hit **Enter** to see the Fahrenheit result
- Press **Clear** to reset the form
- Invalid input shows a clear error message — no crashes
