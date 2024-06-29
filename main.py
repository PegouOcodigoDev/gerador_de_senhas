import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Gerador de Senhas")

tk.Label(root, text="Comprimento da Senha:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "12")

generate_button = tk.Button(root, text="Gerar Senha", command=generate_password)
generate_button.pack(pady=5)

password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=5)

root.mainloop()