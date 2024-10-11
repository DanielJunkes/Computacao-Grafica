import customtkinter as ctk

class FuncaoTransformacao:
    def __init__(self, app: ctk.CTk) -> None:
        self.frame = ctk.CTkFrame(app)
        self.frame.grid(row=1, column=0, columnspan=2, padx=10, pady=0, sticky='nsew')
        self.frame.columnconfigure((0,1,2,3), weight=1)
        self.frame.rowconfigure((0,1,2,3,4), weight=1) 
        
        #Titulo da sub tela
        self.label_titulo = ctk.CTkLabel(self.frame, text="Funções de Tranformações")
        
        #Labels
        self.label_opcao_X = ctk.CTkLabel(self.frame, text="X")
        self.label_opcao_Y = ctk.CTkLabel(self.frame, text="Y")
        
        #Caixa translandar
        #Entrada de valores
        self.text_translandar_x = ctk.CTkEntry(self.frame_entrada)     
        self.text_translandar_Y = ctk.CTkEntry(self.frame_entrada)
        #Botão Translandar
        self.btn_inserir = ctk.CTkButton(self.frame, text="Translandar")
    
    def criar_tela(self) -> None:
        #Titulo da sub tela
        self.label_titulo.grid(row=0, column=0, columnspan=4)
        
        
        