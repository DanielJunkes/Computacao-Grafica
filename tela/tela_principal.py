import customtkinter as ctk

app = ctk.CTk()
app.title("Radares - Sistema de Gestão de Radares")
app.geometry("1080x720")
app.columnconfigure((0,1,2,3,4,5,6,7), weight=1)
app.rowconfigure((0,1,2,3,4,5,6), weight=1)

#entrada de dados
label_entrada = ctk.CTkLabel(app, text="Entrada de Dados")
label_entrada.grid(row=0, column=0, columnspan=2, padx=10)
frame_entrada = ctk.CTkFrame(app)
frame_entrada.columnconfigure((0,1), weight=1)
frame_entrada.rowconfigure((0,1,2,3), weight=1)
frame_entrada.grid(row=1, column=0, columnspan=2, padx=10, sticky='nsew')

#entrada X e Y
label_X = ctk.CTkLabel(frame_entrada, text="X:")
label_X.grid(row=0, column=0, sticky='w', padx=(10,0))
text_X = ctk.CTkEntry(frame_entrada)
text_X.grid(row=0, column=0)
label_Y = ctk.CTkLabel(frame_entrada, text="Y:")
label_Y.grid(row=0, column=1, sticky='w', padx=(10,0))
text_Y = ctk.CTkEntry(frame_entrada)
text_Y.grid(row=0, column=1)

#entrada angulo e raio
label_A = ctk.CTkLabel(frame_entrada, text="Angulo:")
label_A.grid(row=1, column=0, sticky='w', padx=(10,0))
text_A = ctk.CTkEntry(frame_entrada)
text_A.grid(row=1, column=0, padx=(10,0))
label_R = ctk.CTkLabel(frame_entrada, text="Raio:")
label_R.grid(row=1, column=1, sticky='w', padx=(10,0))
text_R = ctk.CTkEntry(frame_entrada)
text_R.grid(row=1, column=1)

#entrada velocidade e direção
label_D = ctk.CTkLabel(frame_entrada, text="Direção:")
label_D.grid(row=2, column=0, sticky='w', padx=(10,0))
text_D = ctk.CTkEntry(frame_entrada)
text_D.grid(row=2, column=0, padx=(15,0))
label_V = ctk.CTkLabel(frame_entrada, text="Velocidade:")
label_V.grid(row=2, column=1, sticky='w', padx=(10,0))
text_V = ctk.CTkEntry(frame_entrada)
text_V.grid(row=2, column=1, padx=(35,0))

#botao de inserir
btn_inserir = ctk.CTkButton(frame_entrada, text="Inserir")
btn_inserir.grid(row=3, column=0, columnspan=2, pady=(0,10), sticky='nsew', padx=10)


app.mainloop()