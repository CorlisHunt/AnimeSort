# date create: 9.03.2024

import tkinter as tk
from tkinter import filedialog

# Переменные
COLOR_BG = "#C9A9FF"
COLOR_FG = "red"
IN_DEVELOPING = "Пока в разработке!!!"
VERSION = "1.0"

selected_folder_path = None


# Функция для кнопки события
def select_folder():
    global selected_folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        print(f"Выбрана папка: {folder_path}")
        selected_folder_path = folder_path
        # TODO: root.event_generate("<<FolderSelected>>") Не удалять!!! Связано с событиями
    else:
        print("Папка не выбрана")


# Создание root(Главного окна)
root = tk.Tk()
root.title("AnimeSort")
root.geometry("640x480+775+300")
root.resizable(False, False)

# Иконка root
image_root = tk.PhotoImage(file="assets/logo.png")
root.iconphoto(False, image_root)

# Цвет фона root
root.config(bg=COLOR_BG)

# Приветствие
lbl_welcome = tk.Label(root, text="Welcome to AnimeSort",
                       font=("Arial", 25),
                       bg=COLOR_BG,
                       )

lbl_welcome.pack(pady=30)

# Справка текст
lbl_text = tk.Label(root, text=f'''Укажите путь к папку для сортировки
Для настройки сортировки воспользуйтесь блокнотом!
{IN_DEVELOPING}''',
                    font=("Arial", 14),
                    bg=COLOR_BG,
                    fg=COLOR_FG
                    )

lbl_text.pack()

# Кнопку для выбора папки
btn = tk.Button(root, cursor="hand2",
                text="Select folder",
                font=("Arial", 15),
                bg="white",
                activebackground="#DE71F9",
                command=select_folder
                )

btn.pack(expand=True, anchor="center")

# Кнопку выхода из приложения
btn_exit = tk.Button(root, cursor="hand2",
                     text="Exit",
                     font=("Arial", 15),
                     bg="#FF6969",
                     activebackground="#FF0000",
                     command=exit,
                     padx=10
                     )

btn_exit.pack(side="right", padx=20, pady=20)

# Версия приложения
lbl_version = tk.Label(root, text=f"version {VERSION}",
                       font=("Arial", 11),
                       bg=COLOR_BG,
                       )

lbl_version.pack(side="left", padx=20)

root.mainloop()
