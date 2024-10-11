import customtkinter as ctk
from entrada_de_dados import EntradaDados
from funcao_transformacao import FuncaoTransformacao

app = ctk.CTk()
app.title("Radares - Sistema de Gestão de Radares")
app.geometry("1080x720")
app.columnconfigure((0,1,2,3,4,5,6,7), weight=1)
app.rowconfigure((0,1,2,3,4,5,6), weight=1)

#entrada de dados
entrada_dados = EntradaDados(app)
entrada_dados.criar_tela()

#funcao de transformação
funcao_transformacao = FuncaoTransformacao(app)
funcao_transformacao.criar_tela()

app.mainloop()