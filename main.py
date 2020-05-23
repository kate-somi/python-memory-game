"""
File: Final.py
----------------
"""

import os
import random
import sys
import tkinter
import time

from PIL import ImageTk
from tkinter import messagebox

from intro import choose_level
from intro import choose_mode

MODE = choose_mode()
LEVEL = choose_level()
COL_SIZE = LEVEL[0]
ROW_SIZE = LEVEL[1]
ROUTE = MODE[1]


def main():
    root = tkinter.Tk()
    root.title("Pairs")
    root.geometry("+200+100")
    root.resizable(0, 0)
    root.bind("<Escape>", lambda event: exit())
    root.bind("<Return>", lambda event: restart(root))
    draw_board(root)
    root.mainloop()


def restart(root):
    root.destroy()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def draw_board(root):
    start_time = time.time()
    answers = make_answers(root)
    default_image = ImageTk.PhotoImage(master=root, file="images/default.png")
    buttons = []
    for row in range(COL_SIZE):
        for col in range(ROW_SIZE):
            button = tkinter.Button(root, image=default_image,
                                    command=lambda row=row, column=col:
                                    change_label(buttons, row, column, answers, root, default_image, start_time))
            buttons.append(button)
            button.grid(column=col, row=row)
    buttons = set_on_board(buttons)
    return buttons


def set_on_board(raw_list):
    set_list = []
    for i in range(0, len(raw_list), ROW_SIZE):
        set_list.append(raw_list[i:i + ROW_SIZE])
    return set_list


def make_answers(root):
    cards_total = ROW_SIZE * COL_SIZE // 2
    answers = []
    for i in range(cards_total):
        route = ROUTE + str(i) + '.png'
        image = ImageTk.PhotoImage(master=root, file=route)
        answers.append(image)
        answers.append(image)
    random.shuffle(answers)
    answers = set_on_board(answers)
    return answers


def change_label(buttons, row, col, answers, root, default_image, start_time):
    buttons[row][col].config(image=answers[row][col], bg="gray99")
    if not is_first(buttons):
        first_card_coords = find_first(buttons, row, col)
        x = first_card_coords[0]
        y = first_card_coords[1]
        if answers[row][col] == answers[x][y]:
            buttons[row][col].config(state=tkinter.DISABLED, bg="white")
            buttons[x][y].config(state=tkinter.DISABLED, bg="white")
            if is_over(buttons):
                time_passed = int(time.time() - start_time)
                messagebox.showinfo(title="Success!", message="Time: " + str(time_passed) + " sec")
                buttons[row][col].after(1000, draw_board, root)
        else:
            buttons[row][col].after(800, hide_buttons, buttons, row, col, x, y, default_image)


def is_first(buttons):
    counter = 0
    for row in range(COL_SIZE):
        for col in range(ROW_SIZE):
            button = buttons[row][col]
            if button["bg"] == "gray99":
                counter += 1
    return counter % 2 == 1


def find_first(buttons, row, col):
    coords = []
    for i in range(COL_SIZE):
        for j in range(ROW_SIZE):
            button = buttons[i][j]
            if button["bg"] == "gray99" and buttons[row][col] != buttons[i][j]:
                coords.append(i)
                coords.append(j)
    return coords


def hide_buttons(buttons, row, col, x, y, default_image):
    buttons[row][col].config(image=default_image, bg="white")
    buttons[x][y].config(image=default_image, bg="white")


def is_over(buttons):
    counter = 0
    for row in range(COL_SIZE):
        for col in range(ROW_SIZE):
            button = buttons[row][col]
            if button["state"] != tkinter.DISABLED:
                counter += 1
    return counter == 0


if __name__ == "__main__":
    main()
