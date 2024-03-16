from tkinter import *
import tkinter.messagebox as tsmg


def re_turns(event):
    global turn, temp
    wid = event.widget
    if  not(wid["text"] == " "):
        turn = temp
    wid["text"] = " "

def turns(event):
    global turn, temp, play_again
    wid = event.widget
    if wid["text"] == " ":
        if turn == "X":
            wid["text"] = "X"
            temp = turn
            turn = "O"
        else:
            wid["text"] = "O"
            temp = turn
            turn = "X"
    # Horizontal
    if  not(button1['text'] == button2['text'] == button3['text'] == " ") and (button1['text'] == button2['text'] == button3['text']):
        button1['bg'] = button2['bg'] = button3['bg'] = "red"
        button1['fg'] = button2['fg'] = button3['fg'] = "white"
        play_again = tsmg.askyesno("Win!", f"{button1['text']} wins the game!\nWant to try again?")
    elif not (button4['text'] == button5['text'] == button6['text'] == " ") and (button4['text'] == button5['text'] == button6['text']):
        button4['bg'] = button5['bg'] = button6['bg'] = "red"
        button4['fg'] = button5['fg'] = button6['fg'] = "white"
        play_again = tsmg.askyesno("Win!", f"{button4['text']} wins the game!\nWant to try again?")
    elif not(button7['text'] == button8['text'] == button9['text'] == " ") and (button7['text'] == button8['text'] == button9['text']):
        button7['bg'] = button8['bg'] = button9['bg'] = "red"
        button7['fg'] = button8['fg'] = button9['fg'] = "white"
        play_again = tsmg.askyesno("Win!", f"{button7['text']} wins the game!\nWant to try again?")

    # Vertical
    elif not (button1['text'] == button4['text'] == button7['text'] == " ") and (button1['text'] == button4['text'] == button7['text']):
        button1['bg'] = button4['bg'] = button7['bg'] = "red"
        button1['fg'] = button4['fg'] = button7['fg'] = "white"
        play_again = tsmg.askyesno("Win!", f"{button1['text']} wins the game!\nWant to try again?")
    elif not (button2['text'] == button5['text'] == button8['text'] == " ") and (button2['text'] == button5['text'] == button8['text']):
        button2['bg'] = button5['bg'] = button8['bg'] = "red"
        button2['fg'] = button5['fg'] = button8['fg'] = "white"
        play_again = tsmg.askyesno("Win!", f"{button2['text']} wins the game!\nWant to try again?")
    elif not (button3['text'] == button6['text'] == button9['text'] == " ") and (button3['text'] == button6['text'] == button9['text']):
        button3['bg'] = button6['bg'] = button9['bg'] = "red"
        button3['fg'] = button6['fg'] = button9['fg'] = "white"
        play_again = tsmg.askyesno("Win!", f"{button3['text']} wins the game!\nWant to try again?")

    # Cross Line
    elif not (button1['text'] == button5['text'] == button9['text'] == " ") and (button1['text'] == button5['text'] == button9['text']):
        button1['bg'] = button5['bg'] = button9['bg'] = "red"
        button1['fg'] = button5['fg'] = button9['fg'] = "white"
        play_again = tsmg.askyesno("Win!", f"{button1['text']} wins the game!\nWant to try again?")
    elif not (button3['text'] == button5['text'] == button7['text'] == " ") and (button3['text'] == button5['text'] == button7['text']):
        button3['bg'] = button5['bg'] = button7['bg'] = "red"
        button3['fg'] = button5['fg'] = button7['fg'] = "white"
        play_again = tsmg.askyesno("Win!", f"{button3['text']} wins the game!\nWant to try again?")
    
    # Draw
    elif button1["text"] in ["X", "O"] and button2["text"] in ["X", "O"] and button3["text"] in ["X", "O"] and button4["text"] in ["X", "O"] and button5["text"] in ["X", "O"] and button6["text"] in ["X", "O"] and button7["text"] in ["X", "O"] and button8["text"] in ["X", "O"] and button9["text"] in ["X", "O"]:
        play_again = tsmg.askyesno("Draw", "It's a draw game!\nWant to try again?")
    
    if play_again is True:
        button1['text'] = button2['text'] = button3['text'] = button4['text'] = button5['text'] = button6['text'] = button7['text'] = button8['text'] = button9['text'] = " "
        button1['bg'] = button2['bg'] = button3['bg'] = button4['bg'] = button5['bg'] = button6['bg'] = button7['bg'] = button8['bg'] = button9['bg'] = "yellow"
        button1['fg'] = button2['fg'] = button3['fg'] = button4['fg'] = button5['fg'] = button6['fg'] = button7['fg'] = button8['fg'] = button9['fg'] = "black"
    elif play_again is False:
        root.destroy()


# Tkinter Initialization
root = Tk()
root.title("Tic Tac Toe")
root.geometry("500x500")
root.resizable(False, False)
root.config(bg="tan")


# Variables
font = "Arial 50"
turn = "X"
temp = " "
play_again = None


# Title Frame
title_frame = Frame(root, bg="tan")
Label(title_frame, text="Tic Tac Toe", font=font, bg="tan").pack(fill="x", side="top", padx=5)
title_frame.pack()


# Buttons Frame
main_frame = Frame(root)

# Buttons
button1 = Button(main_frame, text=" ", font=font, width=3, height=1, relief="raised", bg="yellow", activebackground="coral")
button1.bind("<Button-1>", turns)
button1.bind("<Button-3>", re_turns)
button1.grid(row=1, column=1)

button2 = Button(main_frame, text=" ", font=font, width=3, height=1, relief="raised", bg="yellow", activebackground="coral")
button2.bind("<Button-1>", turns)
button2.bind("<Button-3>", re_turns)
button2.grid(row=1, column=2)

button3 = Button(main_frame, text=" ", font=font, width=3, height=1, relief="raised", bg="yellow", activebackground="coral")
button3.bind("<Button-1>", turns)
button3.bind("<Button-3>", re_turns)
button3.grid(row=1, column=3)

button4 = Button(main_frame, text=" ", font=font, width=3, height=1, relief="raised", bg="yellow", activebackground="coral")
button4.bind("<Button-1>", turns)
button4.bind("<Button-3>", re_turns)
button4.grid(row=2, column=1)

button5 = Button(main_frame, text=" ", font=font, width=3, height=1, relief="raised", bg="yellow", activebackground="coral")
button5.bind("<Button-1>", turns)
button5.bind("<Button-3>", re_turns)
button5.grid(row=2, column=2)

button6 = Button(main_frame, text=" ", font=font, width=3, height=1, relief="raised", bg="yellow", activebackground="coral")
button6.bind("<Button-1>", turns)
button6.bind("<Button-3>", re_turns)
button6.grid(row=2, column=3)

button7 = Button(main_frame, text=" ", font=font, width=3, height=1, relief="raised", bg="yellow", activebackground="coral")
button7.bind("<Button-1>", turns)
button7.bind("<Button-3>", re_turns)
button7.grid(row=3, column=1)

button8 = Button(main_frame, text=" ", font=font, width=3, height=1, relief="raised", bg="yellow", activebackground="coral")
button8.bind("<Button-1>", turns)
button8.bind("<Button-3>", re_turns)
button8.grid(row=3, column=2)

button9 = Button(main_frame, text=" ", font=font, width=3, height=1, relief="raised", bg="yellow", activebackground="coral")
button9.bind("<Button-1>", turns)
button9.bind("<Button-3>", re_turns)
button9.grid(row=3, column=3)

main_frame.pack()


root.mainloop()
