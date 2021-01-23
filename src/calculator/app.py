"""
Beeware calculator
com.example.calculator

adb shell am start -n "com.example.calculator/com.example.calculator.MainActivity" -a android.intent.action.MAIN -c android.intent.category.LAUNCHER

"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

UI_data = [
    [{'type': 'inputtext'}],
    [{'type': 'button', 'name': '7'}, {'type': 'button', 'name': '8'}, {'type': 'button', 'name': '9'}, {'type': 'button', 'name': '+'}],
    [{'type': 'button', 'name': '4'}, {'type': 'button', 'name': '5'}, {'type': 'button', 'name': '6'}, {'type': 'button', 'name': '-'}],
    [{'type': 'button', 'name': '1'}, {'type': 'button', 'name': '2'}, {'type': 'button', 'name': '3'}, {'type': 'button', 'name': '*'}],
    [{'type': 'button', 'name': '.'}, {'type': 'button', 'name': '0'}, {'type': 'button', 'name': 'C'}, {'type': 'button', 'name': '/'}],
    [{'type': 'button', 'name': 'Calculate'}],
]


class Calculator(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        for line in UI_data:
            box_tmp = toga.Box(style=Pack(flex=1))
            for el in line:
                if el['type'] == 'inputtext':
                    element_tmp = toga.TextInput(placeholder='enter expression here', readonly=True, style=Pack(flex=1, font_size=18))
                    self.input_text = element_tmp
                elif el['type'] == 'button':
                    element_tmp = toga.Button(el['name'], on_press=self.button_pressed, style=Pack(flex=1, padding=2, font_size=18))
                box_tmp.add(element_tmp)
            main_box.add(box_tmp)
        main_box.style.update(direction=COLUMN)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def button_pressed(self, widget):
        button_title = widget._label
        if button_title == 'C':
            self.input_text.clear()
        elif button_title != 'Calculate':
            self.input_text.value += button_title
            # print(self.input_text.__dict__)
        else:
            try:
                result = eval(self.input_text.value)
                self.input_text.value = str(result)
            except Exception as e:
                self.main_window.info_dialog("Result", f"Error in expression: {self.input_text.value}")


def main():
    return Calculator()
