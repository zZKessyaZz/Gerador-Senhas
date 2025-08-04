import tkinter as tk

#Janela
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("500x300")
janela.config(bg = "lightgray")

#Frame
botoes_frame = tk.Frame(janela, bg = "lightgray")
botoes_frame.place(relx=0.5, rely=0.35, anchor="center")


btn = tk.Button(botoes_frame, text="Gerar Senha")
btn.pack(side = "left", padx=10)
btn1 = tk.Button(botoes_frame, text="Copiar senha")
btn1.pack(side = "left", padx=10)

#Elementos
tamanho_senha = tk.Spinbox(janela)
tamanho_senha.pack()

campo_senha = tk.Entry()
campo_senha.pack()










janela.mainloop()