from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLACK = "#222222"
WHITE = "#ffffff"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    global reps, timer
    if timer:
        window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(timer_label, text="Timer", fill=WHITE)
    canvas.itemconfig(check_marks, text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        canvas.itemconfig(timer_label, text="Break", fill=RED)
        countdown(long_break_seconds)
    elif reps % 2 == 0:
        canvas.itemconfig(timer_label, text="Break", fill=PINK)
        countdown(short_break_seconds)
    else:
        canvas.itemconfig(timer_label, text="Work", fill=GREEN)
        countdown(work_seconds)

def countdown(count):
    global timer
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        completed_sessions = reps // 2
        canvas.itemconfig(check_marks, text="✔" * completed_sessions)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=0, pady=0)

# Canvas sized exactly to the image (175x175) — no extra space around it
canvas = Canvas(width=175, height=175, highlightthickness=0)
pomo_img = PhotoImage(file="pomodoro.png")
canvas.create_image(0, 0, image=pomo_img, anchor="nw")

# Timer label text (drawn on the canvas, not a separate widget)
timer_label = canvas.create_text(
    87, 25,
    text="Timer",
    fill=WHITE,
    font=(FONT_NAME, 14, "bold")
)

# Timer countdown text
timer_text = canvas.create_text(
    87, 87,
    text="00:00",
    fill=WHITE,
    font=(FONT_NAME, 20, "bold")
)

# Checkmarks text
check_marks = canvas.create_text(
    87, 115,
    text="",
    fill=GREEN,
    font=(FONT_NAME, 10, "bold")
)

# Start Button — embedded inside the canvas via create_window
start_button = Button(
    text="Start",
    command=start_timer,
    bg=BLACK,
    fg=WHITE,
    activebackground=BLACK,
    activeforeground=WHITE,
    font=(FONT_NAME, 8, "bold"),
    relief="flat",
    borderwidth=0,
    cursor="hand2"
)
canvas.create_window(35, 150, window=start_button)

# Reset Button — embedded inside the canvas via create_window
reset_button = Button(
    text="Reset",
    command=reset_timer,
    bg=BLACK,
    fg=WHITE,
    activebackground=BLACK,
    activeforeground=WHITE,
    font=(FONT_NAME, 8, "bold"),
    relief="flat",
    borderwidth=0,
    cursor="hand2"
)
canvas.create_window(140, 150, window=reset_button)

canvas.pack()

window.mainloop()