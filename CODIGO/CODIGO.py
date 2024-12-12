import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

def select_image():
    global input_image_path
    input_image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if input_image_path:
        messagebox.showinfo("Selecionado", f"Imagem selecionada: {input_image_path}")
    else:
        messagebox.showwarning("Aviso", "Nenhuma imagem selecionada!")

def save_image():
    if not input_image_path:
        messagebox.showwarning("Aviso", "Por favor, selecione uma imagem primeiro!")
        return

    output_image_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if output_image_path:
        try:
            image = Image.open(input_image_path)
            draw = ImageDraw.Draw(image)

            new_text = text_entry.get()
            text_color = text_color_var.get()
            background_color = bg_color_var.get()
            font_size = int(font_size_var.get())
            position = position_var.get()

            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except IOError:
                font = ImageFont.load_default()

            text_width, text_height = draw.textbbox((0, 0), new_text, font=font)[2:]

            if position == "Top":
                text_x, text_y = (image.width - text_width) // 2, 10
            elif position == "Center":
                text_x, text_y = (image.width - text_width) // 2, (image.height - text_height) // 2
            else:  
                text_x, text_y = (image.width - text_width) // 2, image.height - text_height - 10

            draw.rectangle(
                [
                    text_x - 10,
                    text_y - 10,
                    text_x + text_width + 10,
                    text_y + text_height + 10,
                ],
                fill=background_color,
            )
            draw.text((text_x, text_y), new_text, font=font, fill=text_color)

            image.save(output_image_path)
            messagebox.showinfo("Sucesso", f"Imagem salva em: {output_image_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar imagem: {str(e)}")
    else:
        messagebox.showwarning("Aviso", "Nenhum local de salvamento selecionado!")

app = ctk.CTk()
app.geometry("800x600")
app.title("CUSTOMTKINTER IMAGE EDITOR")
app.state("zoomed")  

ctk.CTkButton(app, text="SELECIONAR", command=select_image).pack(pady=20)

text_frame = ctk.CTkFrame(app)
text_frame.pack(pady=10, padx=10, fill="x")
ctk.CTkLabel(text_frame, text="DIGITE O TEXTO:").pack(side="left", padx=5)
text_entry = ctk.CTkEntry(text_frame, width=300)
text_entry.pack(side="left", padx=5)
text_entry.insert(0, "CUSTOMTKINTER")

text_color_var = ctk.StringVar(value="white")
text_color_frame = ctk.CTkFrame(app)
text_color_frame.pack(pady=10, padx=10, fill="x")
ctk.CTkLabel(text_color_frame, text="COR DO TEXTO:").pack(side="left", padx=5)
for color in ["white", "red", "green", "blue"]:
    ctk.CTkRadioButton(
        text_color_frame, text=color.capitalize(), variable=text_color_var, value=color
    ).pack(side="left", padx=5)

bg_color_var = ctk.StringVar(value="red")
bg_color_frame = ctk.CTkFrame(app)
bg_color_frame.pack(pady=10, padx=10, fill="x")
ctk.CTkLabel(bg_color_frame, text="COR DO FUNDO:").pack(side="left", padx=5)
for color in ["white", "red", "green", "blue"]:
    ctk.CTkRadioButton(
        bg_color_frame, text=color.capitalize(), variable=bg_color_var, value=color
    ).pack(side="left", padx=5)

font_size_var = ctk.StringVar(value="40")
font_size_frame = ctk.CTkFrame(app)
font_size_frame.pack(pady=10, padx=10, fill="x")
ctk.CTkLabel(font_size_frame, text="TAMANHO DA FONTE:").pack(side="left", padx=5)
for size in ["20", "40", "60", "80", "100", "150", "200"]:
    ctk.CTkRadioButton(
        font_size_frame, text=f"{size}px", variable=font_size_var, value=size
    ).pack(side="left", padx=5)

position_var = ctk.StringVar(value="Center")
position_frame = ctk.CTkFrame(app)
position_frame.pack(pady=10, padx=10, fill="x")
ctk.CTkLabel(position_frame, text="POSIÇÃO DO TEXTO:").pack(side="left", padx=5)
for pos in ["Top", "Center", "Bottom"]:
    ctk.CTkRadioButton(
        position_frame, text=pos, variable=position_var, value=pos
    ).pack(side="left", padx=5)

ctk.CTkButton(app, text="SALVAR", command=save_image).pack(pady=20)

app.mainloop()
