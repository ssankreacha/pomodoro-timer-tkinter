from tkinter import *   # Call classes from the tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)  # Cancels timer
    canvas.itemconfig(timer_text, text="00:00") # canvas
    timer_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)   # Alternatively, call the same label but use the config method
        long_break_time = Label(text="Break", bg=YELLOW, fg=RED, highlightthickness=0, font=(FONT_NAME, 30, "bold"))
        long_break_time.grid(column=1, row=0)
    elif reps % 2 == 0:
        countdown(short_break)
        short_break_time = Label(text="Break", bg=YELLOW, fg=PINK, highlightthickness=0, font=(FONT_NAME, 30, "bold"))
        short_break_time.grid(column=1, row=0)

    else:
        countdown(work)
        work = Label(text="Work", bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 30, "bold"))
        work.grid(column=1, row=0)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    # To change a piece of text in a canvas: particular canvas then itemconfig

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")   # contains attributes of text, from count number
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# window.after(1000, )  # after a certain time (ms), executes the function

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 25, "bold"))
timer_label.grid(column=1, row=0)

checkmarks = Label(bg=YELLOW, highlightthickness=0, fg=GREEN, font=0)
checkmarks.grid(column=1, row=3)

canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # find the file of the tomato, save to variable
canvas.create_image(100, 112, image=tomato_img)     # x, y, cor and variable for image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
