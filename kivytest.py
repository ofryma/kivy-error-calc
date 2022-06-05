import kivy

kivy.require('2.1.0')  # replace with your current kivy version !
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder


import sys
import os
import math
import pyperclip
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


# difine the symbols you need to use
x , y , z = symbols("x y z")
init_printing(use_unicode=True)


def diffExpr(expr,by,times=1):
    if expr == '' or by == '':
        return '-'
    if type(expr) == type(' '):
        new_expr = parse_expr(expr)
    else:
        new_expr = expr
    for _ in range(0,times):
        new_expr = diff(new_expr , by)

    return (new_expr)



class MainScreen(GridLayout):
    Window.size = (400,150)
    def __init__(self, **kargs):
        super(MainScreen, self).__init__(**kargs)

        self.cols = 1
        self.add_widget(Label(text='Formula'))
        self.formula = TextInput(multiline=False,hint_text='x**2 + 3*x + 2',write_tab=False)
        self.formula.bind(on_text_validate=self.calculate_callback)
        self.add_widget(self.formula)
        self.add_widget(Label(text='Variables'))
        self.vars = TextInput(multiline=False,hint_text='x',write_tab=False)
        self.vars.bind(on_text_validate=self.calculate_callback)
        self.add_widget(self.vars)

        self.calculate = Button(text="Calculate")
        self.calculate.bind(state=self.calculate_callback)
        self.add_widget(self.calculate)

        self.res = Label(text='-')
        self.add_widget(self.res)

        self.add_mesure = Button(text="add")
        self.add_mesure.bind(state=self.add_mesurement)
        self.add_widget(self.add_mesure)
        self.mesurments = []


    def calculate_callback(self,event,value='normal'):
        if value == 'normal':
            self.res.text = latex(diffExpr(self.formula.text,self.vars.text))
            pyperclip.copy(self.res.text)


    def add_mesurement(self,event,value):
        if value == 'normal':

            self.remove_widget(self.add_mesure)
            for element in self.mesurments:
                self.remove_widget(element)
            mesur = TextInput(multiline=False, hint_text=f'{len(self.mesurments) + 1}.', write_tab=False)
            self.mesurments.append(mesur)
            for element in self.mesurments:
                self.add_widget(element)
            self.add_widget(self.add_mesure)


class Statistic_ErrApp(App):

    def build(self):

        return MainScreen()



if __name__ == '__main__':
    Statistic_ErrApp().run()
