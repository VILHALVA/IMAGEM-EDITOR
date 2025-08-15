import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import os
import ctypes
from threading import Thread
import glob

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def is_oculto_ou_sistema(path):
    if os.name == "nt":
        try:
            atributos = ctypes.windll.kernel32.GetFileAttributesW(str(path))
            if atributos == -1:
                return False
            FILE_ATTRIBUTE_HIDDEN = 0x2
            FILE_ATTRIBUTE_SYSTEM = 0x4
            return bool(atributos & (FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM))
        except Exception:
            return False
    else:
        return os.path.basename(path).startswith(".")

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IMAGEM EDITOR")
        self.root.state("zoomed")  

        self.selected_directory = ""

        self.scrollable_frame = ctk.CTkScrollableFrame(root, width=800, height=700)
        self.scrollable_frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(
            self.scrollable_frame, text="EDITOR DE IMAGENS", font=("Arial", 30, "bold")
        ).pack(pady=10)

        text_frame = ctk.CTkFrame(self.scrollable_frame, border_width=2, corner_radius=10)
        text_frame.pack(pady=10, padx=10, fill="x")
        ctk.CTkLabel(text_frame, text="DIGITE O TEXTO:").pack(side="left", padx=5)
        self.text_entry = ctk.CTkEntry(text_frame)
        self.text_entry.pack(side="left", padx=5, fill="x", expand=True)
        self.text_entry.insert(0, "EDITADO")

        text_color_frame = ctk.CTkFrame(self.scrollable_frame, border_width=2, corner_radius=10)
        text_color_frame.pack(pady=10, padx=10, fill="x")
        ctk.CTkLabel(text_color_frame, text="COR DO TEXTO:").pack(side="left", padx=5)
        self.text_color_var = ctk.StringVar(value="WHITE")
        for color in ["WHITE", "RED", "GREEN", "BLUE"]:
            ctk.CTkRadioButton(
                text_color_frame, text=color, variable=self.text_color_var, value=color
            ).pack(side="left", padx=5)

        bg_color_frame = ctk.CTkFrame(self.scrollable_frame, border_width=2, corner_radius=10)
        bg_color_frame.pack(pady=10, padx=10, fill="x")
        ctk.CTkLabel(bg_color_frame, text="COR DO FUNDO:").pack(side="left", padx=5)
        self.bg_color_var = ctk.StringVar(value="RED")
        for color in ["WHITE", "RED", "GREEN", "BLUE"]:
            ctk.CTkRadioButton(
                bg_color_frame, text=color, variable=self.bg_color_var, value=color
            ).pack(side="left", padx=5)

        font_size_frame = ctk.CTkFrame(self.scrollable_frame, border_width=2, corner_radius=10)
        font_size_frame.pack(pady=10, padx=10, fill="x")
        ctk.CTkLabel(font_size_frame, text="TAMANHO DA FONTE:").pack(side="left", padx=5)
        self.font_size_var = ctk.StringVar(value="40")
        for size in ["20", "40", "60", "80", "100", "150", "200"]:
            ctk.CTkRadioButton(
                font_size_frame, text=f"{size.upper()}PX", variable=self.font_size_var, value=size
            ).pack(side="left", padx=5)

        position_frame = ctk.CTkFrame(self.scrollable_frame, border_width=2, corner_radius=10)
        position_frame.pack(pady=10, padx=10, fill="x")
        ctk.CTkLabel(position_frame, text="POSIÇÃO DO TEXTO:").pack(side="left", padx=5)
        self.position_var = ctk.StringVar(value="CENTER")
        for pos in ["TOP", "CENTER", "BOTTOM"]:
            ctk.CTkRadioButton(
                position_frame, text=pos, variable=self.position_var, value=pos
            ).pack(side="left", padx=5)

        self.button_frame = ctk.CTkFrame(self.scrollable_frame)
        self.button_frame.pack(pady=10)
        ctk.CTkButton(self.button_frame, text="DIRETÓRIO", command=self.select_directory).pack(side="left", padx=5)
        self.convert_button = ctk.CTkButton(self.button_frame, text="EDITAR", command=self.start_conversion, state="disabled")
        self.convert_button.pack(side="left", padx=5)

        self.status_textbox = ctk.CTkTextbox(self.scrollable_frame, width=500, height=165)
        self.status_textbox.pack(pady=10)
        self.status_textbox.configure(state='disabled')

        self.progress_frame = ctk.CTkFrame(self.scrollable_frame)
        self.progress_frame.pack(pady=(0, 5), fill="x", padx=10)
        self.progress_count_label = ctk.CTkLabel(self.progress_frame, text="0/0", width=50, anchor="w")
        self.progress_count_label.pack(side="left")
        self.progress_bar = ctk.CTkProgressBar(self.progress_frame)
        self.progress_bar.set(0)
        self.progress_bar.pack(side="left", expand=True, fill="x", padx=10)
        self.progress_percent_label = ctk.CTkLabel(self.progress_frame, text="0%", width=50, anchor="e")
        self.progress_percent_label.pack(side="right")

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.selected_directory = directory
            self.clear_status()
            self.append_status(f"DIRETÓRIO SELECIONADO: {directory}\n")
            self.convert_button.configure(state="normal")

    def start_conversion(self):
        self.clear_status(keep_directory=True)
        self.progress_bar.set(0)
        self.progress_count_label.configure(text="0/0")
        self.progress_percent_label.configure(text="0%")
        Thread(target=self.convert_images).start()

    def convert_images(self):
        input_dir = self.selected_directory
        output_dir = os.path.join(input_dir, "IMAGEM_EDITOR")
        os.makedirs(output_dir, exist_ok=True)

        image_extensions = ['*.jpg', '*.jpeg', '*.png']
        image_files = []
        for ext in image_extensions:
            for file in glob.glob(os.path.join(input_dir, ext)):
                if not is_oculto_ou_sistema(file):
                    image_files.append(file)

        if not image_files:
            self.append_status("NENHUMA IMAGEM ENCONTRADA!\n")
            return

        total = len(image_files)
        for idx, image_path in enumerate(image_files):
            try:
                image = Image.open(image_path)
                draw = ImageDraw.Draw(image)

                new_text = self.text_entry.get()
                text_color = self.text_color_var.get()
                background_color = self.bg_color_var.get()
                font_size = int(self.font_size_var.get())
                position = self.position_var.get()

                try:
                    font = ImageFont.truetype("arial.ttf", font_size)
                except IOError:
                    font = ImageFont.load_default()

                text_width, text_height = draw.textbbox((0, 0), new_text, font=font)[2:]

                if position == "TOP":
                    text_x, text_y = (image.width - text_width) // 2, 10
                elif position == "CENTER":
                    text_x, text_y = (image.width - text_width) // 2, (image.height - text_height) // 2
                else:
                    text_x, text_y = (image.width - text_width) // 2, image.height - text_height - 10

                draw.rectangle(
                    [text_x - 10, text_y - 10, text_x + text_width + 10, text_y + text_height + 10],
                    fill=background_color,
                )
                draw.text((text_x, text_y), new_text, font=font, fill=text_color)

                filename = os.path.basename(image_path)
                output_file = os.path.join(output_dir, filename)
                image.save(output_file)
                self.append_status(f"EDITADO: {filename}\n")

                progress_value = (idx + 1) / total
                self.progress_bar.set(progress_value)
                self.progress_count_label.configure(text=f"{idx + 1}/{total}")
                self.progress_percent_label.configure(text=f"{int(progress_value * 100)}%")

            except Exception as e:
                self.append_status(f"ERRO AO PROCESSAR {image_path}: {str(e)}\n")

        self.append_status(f"\nEDIÇÃO CONCLUÍDA!\nARQUIVOS SALVOS EM: {output_dir}\n")
        messagebox.showinfo("FINALIZADO", "TODAS AS IMAGENS FORAM EDITADAS COM SUCESSO!")

    def clear_status(self, keep_directory=False):
        text = self.status_textbox.get("1.0", "end")
        self.status_textbox.configure(state='normal')
        self.status_textbox.delete("1.0", "end")
        if keep_directory:
            for line in text.splitlines():
                if line.startswith("DIRETÓRIO SELECIONADO"):
                    self.status_textbox.insert("end", line + "\n")
        self.status_textbox.configure(state='disabled')

    def append_status(self, message):
        self.status_textbox.configure(state='normal')
        self.status_textbox.insert("end", message)
        self.status_textbox.see("end")
        self.status_textbox.configure(state='disabled')

if __name__ == "__main__":
    root = ctk.CTk()
    app = ImageEditorApp(root)
    root.mainloop()
