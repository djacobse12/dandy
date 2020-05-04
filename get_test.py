# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:07:31 2019

@author: djaco
"""

import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, name = None, age = None):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.name = tk.Entry(self)
        self.age = tk.Entry(self)
        self.button = tk.Button(self, text="Get", command=self.on_button)
        self.button.pack()
        self.entry.pack()
        self.name.pack()
        self.age.pack()

    def on_button(self):
        print(self.entry.get())
        print(self.name.get())
        print(self.age.get())

app = SampleApp(name = 'hello',age = 3)
app.mainloop()