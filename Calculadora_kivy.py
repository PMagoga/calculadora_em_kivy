from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operadores = ["+", "-", "*", "/"]
        self.ultimo_operador_usado = None
        self.ultimo_botao = None
        main_layout = BoxLayout(orientation="vertical")
        self.solucao = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solucao)
        buttons = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            [".", "0", "C", "/"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        botao_igual = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        botao_igual.bind(on_press=self.on_solution)
        main_layout.add_widget(botao_igual)

        return main_layout

    def on_button_press(self, instance):
        resposta = self.solucao.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.solucao.text = ""
        else:
            if resposta and (
                    self.ultimo_operador_usado and button_text in self.operadores):
                # Don't add two operators right after each other
                return
            elif resposta == "" and button_text in self.operadores:
                # First character cannot be an operator
                return
            else:
                new_text = resposta + button_text
                self.solucao.text = new_text
        self.ultimo_botao = button_text
        self.ultimo_operador_usado = self.ultimo_botao in self.operadores

    def on_solution(self, instance):
        text = self.solucao.text
        if text:
            solution = str(eval(self.solucao.text))
            self.solucao.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()