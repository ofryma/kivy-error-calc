import kivy
kivy.require('2.1.0') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#
# def callback(instance,value):
#
def on_enter(instance):
    print(f'value is {instance.text}')

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.username.bind(on_text_validate = on_enter)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.password.bind(on_text_validate = on_enter)
        self.add_widget(self.password)

        self.submit = Button(text='Submit', font_size = 14)
        self.submit.bind(state=self.submit_button)
        self.add_widget(self.submit)

    def submit_button(self,instance,value):

        if value == 'normal':
            print(f'Button {instance.text} button is {value}')
            print(f'Username: {self.username.text}')
            print(f'Password: {self.password.text}')




class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()