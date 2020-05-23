"""
File: Final.py
----------------
"""

from tkinter import *


def choose_mode():
    chosen_mode = []
    intro_root = Tk()
    intro_root.title("Rules")
    intro_root.geometry("+200+100")
    intro_root.resizable(0, 0)
    intro_root.bind("<Escape>", lambda event: exit())
    rules = Label(text="\n1. Turn over any two cards.\n"
                       "2. If the two cards match, they remain face up.\n"
                       "3. If not, they are flipped face down.\n"
                       "4. The game is over when all the cards have been matched.\n"
                       "5. A new game starts automatically.\n"
                       "6. Press ENTER to change mode.\n"
                       "7. Press ESC to exit.\n",
                  width="48",
                  bg="misty rose")
    rules.pack(side=TOP)
    colored_mode = Button(text="COLORED MODE", width="23", height="5", bg="rosy brown",
                          command=lambda mode=1, route='images/pic':
                          clicked(mode, route, intro_root, chosen_mode))
    colored_mode.pack(side=LEFT)
    colorblind_mode = Button(text="COLORBLIND MODE", width="23", height="5", bg="rosy brown",
                             command=lambda mode=2, route='images/RustyLake/pic':
                             clicked(mode, route, intro_root, chosen_mode))
    colorblind_mode.pack(side=LEFT)
    intro_root.mainloop()
    return chosen_mode


def clicked(first_value, second_value, root, info_list):
    info_list.append(first_value)
    info_list.append(second_value)
    root.destroy()


def choose_level():
    chosen_level = []
    level_root = Tk()
    level_root.title("Level")
    level_root.geometry("+200+100")
    level_root.resizable(0, 0)
    level_root.bind("<Escape>", lambda event: exit())
    lvl1 = Button(text="EASY", width="15", height="5", bg="alice blue",
                  command=lambda rows=3, cols=4: clicked(rows, cols, level_root, chosen_level))
    lvl1.pack(side=LEFT)
    lvl2 = Button(text="MEDIUM", width="15", height="5", bg="lavender blush",
                  command=lambda rows=4, cols=6: clicked(rows, cols, level_root, chosen_level))
    lvl2.pack(side=LEFT)
    lvl3 = Button(text="HARD", width="15", height="5", bg="lavender",
                  command=lambda rows=5, cols=8: clicked(rows, cols, level_root, chosen_level))
    lvl3.pack(side=LEFT)
    level_root.mainloop()
    return chosen_level
