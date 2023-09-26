# Importando a biblioteca tkinter
import tkinter as tk
from tkinter import ttk


# Variável para armazenar a expressão de cálculo
calculation = ''


# Função para adicionar símbolos à expressão de cálculo
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)


# Função para calcular o resultado da expressão
def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ''
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, 'Error')


# Função para limpar o campo de cálculo
def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')


# Criando uma janela principal usando tkinter
root = tk.Tk()
root.geometry('355x340')
root.title('Calc. PEMDAS')

style = ttk.Style()
style.configure('TButton', font=('Arial', 16), padding=10, relief='raised', borderwidth=2)



# Criando um campo de texto para exibir a expressão e o resultado
text_result = tk.Text(root, height=2, width=19, font=('Arial', 24))
text_result.grid(columnspan=5)


# Criando botões para números, operadores, igual e limpar

btn_1 = ttk.Button(root, text='1', command=lambda: add_to_calculation(
    '1'), width=5)
btn_1.grid(row=2, column=1)

btn_2 = ttk.Button(root, text='2', command=lambda: add_to_calculation(
    '2'), width=5)
btn_2.grid(row=2, column=2)

btn_3 = ttk.Button(root, text='3', command=lambda: add_to_calculation(
    '3'), width=5)
btn_3.grid(row=2, column=3)

btn_4 = ttk.Button(root, text='4', command=lambda: add_to_calculation(
    '4'), width=5)
btn_4.grid(row=3, column=1)

btn_5 = ttk.Button(root, text='5', command=lambda: add_to_calculation(
    '5'), width=5)
btn_5.grid(row=3, column=2)

btn_6 = ttk.Button(root, text='6', command=lambda: add_to_calculation(
    '6'), width=5)
btn_6.grid(row=3, column=3)

btn_7 = ttk.Button(root, text='7', command=lambda: add_to_calculation(
    '7'), width=5)
btn_7.grid(row=4, column=1)

btn_8 = ttk.Button(root, text='8', command=lambda: add_to_calculation(
    '8'), width=5)
btn_8.grid(row=4, column=2)

btn_9 = ttk.Button(root, text='9', command=lambda: add_to_calculation(
    '9'), width=5)
btn_9.grid(row=4, column=3)

btn_0 = ttk.Button(root, text='0', command=lambda: add_to_calculation(
    '0'), width=5)
btn_0.grid(row=5, column=2)

btn_plus = ttk.Button(root, text='+', command=lambda: add_to_calculation(
    '+'), width=5)
btn_plus.grid(row=2, column=4)

btn_minus = ttk.Button(root, text='-', command=lambda: add_to_calculation(
    '-'), width=5)
btn_minus.grid(row=3, column=4)

btn_mult = ttk.Button(root, text='*', command=lambda: add_to_calculation(
    '*'), width=5)
btn_mult.grid(row=4, column=4)

btn_divi = ttk.Button(root, text='/', command=lambda: add_to_calculation(
    '/'), width=5)
btn_divi.grid(row=5, column=4)

btn_open = ttk.Button(root, text='(', command=lambda: add_to_calculation(
    '('), width=5)
btn_open.grid(row=5, column=1)

btn_close = ttk.Button(root, text=')', command=lambda: add_to_calculation(
    ')'), width=5)
btn_close.grid(row=5, column=3)

btn_equal = ttk.Button(
    root, text='=', command=evaluate_calculation, width=11)
btn_equal.grid(row=6, column=3, columnspan=2)

btn_clear = ttk.Button(root, text='C', command=clear_field,
                      width=11)
btn_clear.grid(row=6, column=1, columnspan=2)

root.mainloop()