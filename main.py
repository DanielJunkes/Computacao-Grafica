import customtkinter as ctk
import pygame as pyG
from PIL import Image

pyG.init()

app = ctk.CTk()
app.geometry("1000x650")
app.title("Avioes")

tab_view = ctk.CTkTabview(app)
tab_view.add("Radar")
tab_view.add("Mapa")
tab_view.pack(expand=True, fill="both")

frame_radar = ctk.CTkFrame(tab_view.tab("Radar"), width=980, height=500)
frame_radar.grid(row=0, column=0, padx=10, pady=10)

btn_add_aviao = ctk.CTkButton(tab_view.tab("Radar"), text="Adicionar Avião", command=lambda: print("Button clicked"))
btn_add_aviao.grid(row=6, column=0, padx=10, pady=10)

# Create a Pygame surface
pygame_surface = pyG.Surface((980, 500))
pygame_surface.fill((255, 255, 255))

pyG.draw.rect(pygame_surface, (255, 0, 0), (100, 100, 50, 50))
pygame_image = pyG.image.tostring(pygame_surface, 'RGB')
tkinter_image = ctk.CTkImage(Image.frombytes('RGB', (980, 500), pygame_image), size=(980, 500))

# Create a Tkinter label to display the Pygame surface
label = ctk.CTkLabel(frame_radar, image=tkinter_image, text="")
label.grid(row=0, column=0)

def game_loop():
    # Handle Pygame events
    for event in pyG.event.get():
        if event.type == pyG.QUIT:
            app.quit()

    # Add more drawing commands here

    # Update the Tkinter window
    # You'll need to convert the Pygame surface to a format Tkinter can display
    pygame_image = pyG.image.tostring(pygame_surface, 'RGB')
    tkinter_image.configure(data=pygame_image)
    app.after(16, game_loop)  # Call the game loop again after 16ms (approx. 60 FPS)

game_loop()  # Start the game loop

app.mainloop()
