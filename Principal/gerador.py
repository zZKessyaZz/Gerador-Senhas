import tkinter as tk
from PIL import Image, ImageTk
import string
import random

#Janela
janela = tk.Tk()
janela.title(" ")
janela.geometry("600x400")
janela.config(bg = "lightyellow")
janela.minsize(width=600, height= 400)
janela.maxsize(width=600, height=400)

#Frame principal
frame_principal = tk.Frame(janela, bg="lightyellow")
frame_principal.pack(expand=True)

#Imagem
caminho_imagem = "Principal/foto_gerador.jpg"
imagem = Image.open(caminho_imagem)
imagem_tamanho = imagem.resize((450, 150))
foto1 = ImageTk.PhotoImage(imagem_tamanho)

label_imagem = tk.Label(frame_principal, image = foto1, bg = "lightyellow")
label_imagem.pack(pady = 10)


#Lógica para gerar e copiar a senha

def gerar_senha():
    tamanho = int(tamanho_senha.get())
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    campo_senha.delete(0, tk.END)
    campo_senha.insert(0, senha)

def copiar_senha():
    senha_gerada = campo_senha.get()
    if senha_gerada:
        janela.clipboard_clear()
        janela.clipboard_append(senha_gerada)
        janela.update()

        label_confirmacao = tk.Label(frame_copiar, text="Senha Copiada!",bg="lightyellow", fg="green")
        label_confirmacao.pack(pady = 5)
        janela.after(2000, label_confirmacao.destroy)
    else:
        label_confirmacao = tk.Label(frame_copiar, text="Nada pra copiar!", bg= "lightyellow", fg="red")
        label_confirmacao.pack(pady=5)
        janela.after(2000, label_confirmacao.destroy)


#Frame gerar senha
frame_senha = tk.Frame(frame_principal, bg="lightyellow")
frame_senha.pack(pady=10)
label_senha = tk.Label(frame_senha, text="Escolha a quantidade de dígitos da senha:",font=("Comic Sans Ms",12), bg="lightyellow")
label_senha.pack(pady = 5)
tamanho_senha = tk.Spinbox(frame_senha, from_= 4, to=16, justify="center", width = 15, bg= "white")
tamanho_senha.pack(side = "left", padx=5)
btn = tk.Button(frame_senha, text="Gerar Senha", command= gerar_senha, width=20, height=2, bg = "#FACFF0", activebackground = "#FACFF0", activeforeground="black")
btn.pack(side = "left", padx=5)

#Frame copiar senha
frame_copiar = tk.Frame(frame_principal, bg = "lightyellow")
frame_copiar.pack(pady=10)
campo_senha = tk.Entry(frame_copiar,justify="center", bg="white")
campo_senha.pack(pady=5)
btn1 = tk.Button(frame_copiar, text="Copiar Senha", command=copiar_senha, width=20, height = 2, bg="#FACFF0")
btn1.pack(pady=5, padx=10)

janela.mainloop()