from tkinter import *
from prompts import Prompt

BACKGROUND_COLOR = "#ff7171"
TIMER_COLOR = "white"
BUTTON_COLOR = "#ffd3b4"
count = 5
rounds = 0
spaces = 0

#--------------Prompts-----------------#

prompt = Prompt()
new_prompt = prompt.NewPrompt()[0][0]

#--------------Timer-----------------#

def timer ():
    global count
    global rounds
    global spaces
    canvas.itemconfig(timer_text, text=f"{count} seconds")
    count -=1
    if count == 0:
        rounds += 1
        count = 5
        if spaces == 0:
            text.delete("1.0", END)
            text.insert(1.0, f"Prompt: {new_prompt}")
            count = 5
        canvas.after(1000, timer)
        spaces = 0
    elif rounds == 12:
        text.insert(END, "\n\nYou did it! Now it's time to save your work.")
    else:
        canvas.after(1000, timer)

def activity(event=None):
    global spaces
    spaces +=1

def save ():
    global rounds
    global count
    global spaces
    with open("masterpiece.txt", "a") as file:
        file.write(text.get("1.0", END))
    canvas.itemconfig(timer_text, text="Masterpiece Saved!")
    text.delete("1.0", END)
    text.insert(1.0, f"Prompt: {prompt.NewPrompt()[0][0]}")
    rounds = 0
    count = 5
    spaces = 0

#--------------UI-----------------#

# Set up Window
window = Tk()
window.title ("Most Dangerous Writing App")
window.minsize(width = 850, height = 590)
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)


# Set up Canvas for Timer
canvas = Canvas(width=800, height = 50, highlightthickness=0, bg =BACKGROUND_COLOR)
timer_text = canvas.create_text(400,30, text="00:00", fill = TIMER_COLOR, font = ("Didot", 35, "bold"))
canvas.grid(column=1, row=4)

# Labels
label_title = Label(text = "The Most Dangerous Writing App", font = ("Didot", 56), foreground = "white", background = BACKGROUND_COLOR, pady=5)
label_title.grid(column=1, row = 1)

label_directions = Label(text = "Using the prompt, start writing!\nYou have 1 minute. If you pause for more than 5 seconds, your text will disappear, so keep going!", font = ("Didot", 24), foreground = "black", background = BACKGROUND_COLOR, pady=30)
label_directions.grid(column=1, row = 2)

# Buttons
start_button = Button(text = "Start", font = ('didot', 24), relief = "raised", highlightthickness = 0, activebackground = BUTTON_COLOR, command = timer)
start_button.grid(column=1, row = 3)

save_button = Button(text = "Save & Reset", font = ('didot', 24), relief = "raised", highlightthickness = 0, activebackground = BUTTON_COLOR, command = save)
save_button.grid(column=1, row = 6, pady=(10,0))

# Typing Text Field
text = Text(height=15, width= 40, font=("courier",20))
text.insert(1.0, f"Prompt: {new_prompt}")
text.focus()
text.config(wrap=WORD)
text.grid(column=1, row=5, pady=(10,0))

# Gameplay
window.bind("<space>", activity)
window.mainloop()
