import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para adicionar uma nova tarefa ao banco de dados
def add_task():
    description = task_entry.get()
    if description:
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute("INSERT INTO tasks (description, status) VALUES (?, ?)", (description, 'Pending'))
        conn.commit()
        conn.close()
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Digite uma descrição para a tarefa!")

# Função para listar todas as tarefas
def update_task_list():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    task_listbox.delete(0, tk.END)
    for row in rows:
        task_listbox.insert(tk.END, f"{row[0]} - {row[1]} ({row[2]})")
    conn.close()

# Função para remover uma tarefa selecionada
def remove_task():
    try:
        index = task_listbox.curselection()[0]
        task_id = int(task_listbox.get(index).split('-')[0].strip())
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        conn.close()
        update_task_list()
    except:
        messagebox.showwarning("Warning", "Selecione uma tarefa para remover!")

# Configuração da janela principal
root = tk.Tk()
root.title("Gerenciador de Tarefas")

# Entrada para adicionar nova tarefa
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=5, pady=5)

# Botão para adicionar tarefa
add_button = tk.Button(root, text="Adicionar Tarefa", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

# Lista de tarefas
task_listbox = tk.Listbox(root, width=80)
task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Botão para remover tarefa selecionada
remove_button = tk.Button(root, text="Remover Tarefa", command=remove_task)
remove_button.grid(row=2, column=0, padx=5, pady=5, sticky='w')

# Atualizar lista de tarefas
update_task_list()

# Loop principal da interface gráfica
root.mainloop()
