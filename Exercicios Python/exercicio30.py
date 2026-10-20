import tkinter as tk
#root é a janela principal do GUI
root = tk.Tk()
root.title ("TK Example")
root.geometry("500x300")

label = tk.Label(root, text="Hello, TKintr!")
label.pack(pady=20)

button = tk.Button(root, text="Click Me!", command=lambda: label.config(text="Button Clicked!")
#button.pack serve para posicionar e exibir o botão na janela
button.pack()

#Deixa em loop a aplição
root.mainloop()