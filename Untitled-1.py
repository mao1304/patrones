
from abc import ABC, abstractmethod

# Abstract Product A

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

# Abstract Product B

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# Concrete Product A1

class MacOSButton(Button):
    def paint(self):
        return "tu has creado  MacOSButton."

# Concrete Product A2

class WindowsButton(Button):
    def paint(self):
        return "tu has creado  WindowsButton."

# Concrete Product B1

class MacOSCheckbox(Checkbox):
    def paint(self):
        return "tu has creado  MacOSCheckbox."

# Concrete Product B2

class WindowsCheckbox(Checkbox):
    def paint(self):
        return "tu has creado  WindowsCheckbox."

# Abstract Factory

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete Factory 1

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()

# Concrete Factory 2

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

# Cliente

class Application:
    def __init__(self, factory):
        self.factory = factory

    def create_ui(self):
        button = self.factory.create_button()
        checkbox = self.factory.create_checkbox()
        return f"{button.paint()} {checkbox.paint()}"

# Test code
if __name__ == "__main__":
    app = Application(MacOSFactory())
    print(app.create_ui())

    app = Application(WindowsFactory())
    print(app.create_ui())

    # Este ejemplo implementa una fábrica abstracta para la creación de elementos de interfaz de usuario (botones y casillas de verificación).
    # La clase Application utiliza la fábrica para crear elementos de interfaz de usuario concretos (por ejemplo, MacOSButton y MacOSCheckbox).
    # Al cambiar la fábrica utilizada por Application, se pueden crear elementos de interfaz de usuario de diferentes sistemas operativos sin cambiar
    # el código de la aplicación.





