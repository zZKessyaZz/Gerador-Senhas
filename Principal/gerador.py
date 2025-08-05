import tkinter as tk
from PIL import Image, ImageTk

#Janela
janela = tk.Tk()
janela.title(" ")
janela.geometry("600x400")
janela.config(bg = "lightgray")
janela.minsize(width=600, height= 400)
janela.maxsize(width=600, height=400)

#Frame principal
frame_principal = tk.Frame(janela, bg="lightgray")
frame_principal.pack(expand=True)

#Imagem
caminho_imagem = "Principal/foto.png"
imagem = Image.open(caminho_imagem)
imagem_tamanho = imagem.resize((400, 150))
foto1 = ImageTk.PhotoImage(imagem_tamanho)

label_imagem = tk.Label(frame_principal, image = foto1, bg = "lightblue")
label_imagem.pack(pady = 10)

#Frame gerar senha
frame_senha = tk.Frame(frame_principal, bg="lightgray")
frame_senha.pack(pady=10)
label_senha = tk.Label(frame_senha, text="Escolha a quantidade de dígitos da senha:",font=("Comic Sans Ms",12), bg="lightgray")
label_senha.pack(pady = 5)
tamanho_senha = tk.Spinbox(frame_senha)
tamanho_senha.pack(side = "left", padx=5)
btn = tk.Button(frame_senha, text="Gerar Senha")
btn.pack(side = "left", padx=5)

#Frame copiar senha
frame_copiar = tk.Frame(frame_principal, bg = "lightgray")
frame_copiar.pack(pady=10)
campo_senha = tk.Entry(frame_copiar)
campo_senha.pack(pady=5)
btn1 = tk.Button(frame_copiar, text="Copiar Senha")
btn1.pack(pady=5)



janela.mainloop()