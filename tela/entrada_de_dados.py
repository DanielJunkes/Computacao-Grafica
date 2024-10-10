import customtkinter as ctk

class EntradaDados:
    
    def __init__(self, app: ctk.CTk) -> None:
        self.frame_entrada = ctk.CTkFrame(app)
        self.frame_entrada.columnconfigure((0,1), weight=1)
        self.frame_entrada.rowconfigure((0,1,2,3), weight=1)       
        
        #entrda de dados X e Y
        self.label_X = ctk.CTkLabel(self.frame_entrada, text="X:")       
        self.text_X = ctk.CTkEntry(self.frame_entrada)        
        self.label_Y = ctk.CTkLabel(self.frame_entrada, text="Y:")        
        self.text_Y = ctk.CTkEntry(self.frame_entrada)        

        #entrada angulo e raio
        self.label_A = ctk.CTkLabel(self.frame_entrada, text="Angulo:")        
        self.text_A = ctk.CTkEntry(self.frame_entrada)        
        self.label_R = ctk.CTkLabel(self.frame_entrada, text="Raio:")       
        self.text_R = ctk.CTkEntry(self.frame_entrada)       

        #entrada velocidade e direção
        self.label_D = ctk.CTkLabel(self.frame_entrada, text="Direção:")        
        self.text_D = ctk.CTkEntry(self.frame_entrada)       
        self.label_V = ctk.CTkLabel(self.frame_entrada, text="Velocidade:")
        self.text_V = ctk.CTkEntry(self.frame_entrada)        

        #botao de inserir
        self.btn_inserir = ctk.CTkButton(self.frame_entrada, text="Inserir")
        
        
    def criar_tela(self) -> None:
        self.frame_entrada.grid(row=0, column=0, columnspan=2, padx=10, pady=40, sticky='nsew')
        
        self.label_X.grid(row=0, column=0, sticky='w', padx=(10,0))
        self.text_X.grid(row=0, column=0)
        
        self.label_Y.grid(row=0, column=1, sticky='w', padx=(10,0))
        self.text_Y.grid(row=0, column=1)
        
        self.label_A.grid(row=1, column=0, sticky='w', padx=(10,0))
        self.text_A.grid(row=1, column=0, padx=(10,0))
        self.label_R.grid(row=1, column=1, sticky='w', padx=(10,0))
        self.text_R.grid(row=1, column=1)
        
        self.label_D.grid(row=2, column=0, sticky='w', padx=(10,0))
        self.text_D.grid(row=2, column=0, padx=(15,0))
        self.label_V.grid(row=2, column=1, sticky='w', padx=(10,0))
        self.text_V.grid(row=2, column=1, padx=(35,0))
        
        self.btn_inserir.grid(row=3, column=0, columnspan=2, pady=(0,10), sticky='nsew', padx=10)