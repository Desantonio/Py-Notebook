from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        layout = GridLayout(cols=4, spacing=10, padding=20)

        # Create a Label to display the expression
        self.display_label = Label(
            text="",
            font_size=64,  # Increased font size
            size_hint=(1, None),
            height=100,   # Increased height
            halign="right",
            valign="center",
            text_size=(None, 100)
        )
        layout.add_widget(self.display_label)

        # Button labels
        button_labels = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for label in button_labels:
            button = Button(
                text=label,
                font_size=32,  # Increased font size
                background_color=(0.2, 0.6, 0.9, 1),
                background_normal='',
                on_press=self.on_button_click
            )
            layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        button_text = instance.text

        if button_text == 'C':
            self.expression = ""
            self.display_label.text = ""
        elif button_text == '=':
            try:
                self.expression = str(eval(self.expression))
                self.display_label.text = self.expression
            except Exception:
                self.display_label.text = "Error"
                self.expression = ""
        else:
            if self.expression == "0":
                self.expression = ""

            self.expression += button_text
            self.display_label.text = self.expression

if __name__ == '__main__':
    CalculatorApp().run()
