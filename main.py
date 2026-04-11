from tkinter import *
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

def reset_timer():
    # O método .after_cancel cancela o window.after armazenado em timer, o que possibilita que
    # o cronômetro seja pausado
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Temporizador", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Se é a oitava repetição:
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Longa pausa", fg=RED, font=(FONT_NAME,50))

    elif reps % 2 == 0:
    # Se é a segunda, quarta, sexta repetição:
        count_down(short_break_sec)
        title_label.config(text="Pequena pausa", fg=PINK, font=(FONT_NAME,50))
    # Senão:
    else:
        count_down(work_sec)
        title_label.config(text="Trabalho", fg=GREEN, font=(FONT_NAME, 50))

# .after() é um método que espera um determinado tempo passado como argumento, depois desse tempo
# uma função é chamada.
def count_down(count):
    
    # math.floor retorna o maior número inteiro
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # O método canvas.itemconfig permite que se configure um objeto configurado como canvas.
    # passa como primeiro parâmetro o objeto canvas desejado a se configurar e o segundo parâmetro
    # a propriedade a ser alterada.
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Temporizador", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)
# O objeto criado usando a classe Canvas, permite que se crie uma forma gráfica.
# Depois, usando o método .create_image, se cria uma imagem posicionada em x = 100 e y = 112
# A classe PhotoImage armazena uma imagem passando o arquivo como parâmetro. 
# Depois, no argumento image de create_image é passado a variável que armazena a PhotoImage
# O método .create_text cria um texto
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Iniciar", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Recomeçar", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()