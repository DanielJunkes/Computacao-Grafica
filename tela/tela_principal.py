import customtkinter as ctk
from entrada_de_dados import EntradaDados

app = ctk.CTk()
app.title("Radares - Sistema de Gestão de Radares")
app.geometry("1080x720")
app.columnconfigure((0,1,2,3,4,5,6,7), weight=1)
app.rowconfigure((0,1,2,3,4,5,6), weight=1)

#entrada de dados
label_entrada = ctk.CTkLabel(app, text="Entrada de Dados")
label_entrada.grid(row=0, column=0, columnspan=2, padx=10)
entrada_dados = EntradaDados(app)
entrada_dados.criar_tela()

app.mainloop()