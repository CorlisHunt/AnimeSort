# date create: 09.03.2024

# TODO: Не забыть почитать про зоны видимости в Python, более подробно разобрать импорты модулей и почитать об ОПП!

# IMPORTANT!!! Не удалять Связано с событиями
# import tkinter as tk
#
# # Мои модули
# import interface
# import logic
#
#
# def on_folder_selection(event):
#     if interface.select_folder():
#         logic.process_folder(interface.select_folder)
#     else:
#         print("Папка не выбрана, обработка не может быть выполнена.")
#
#
# root = tk.Tk()
# root.bind("<<FolderSelected>>", on_folder_selection)
# root.mainloop()

import interface
import logic


def main():
    interface.root.mainloop()  # Запускаем главный цикл интерфейса только после импорта всех модулей

    # Теперь, после закрытия интерфейса, программа переходит к логике
    if interface.selected_folder_path:
        logic.process_folder(interface.selected_folder_path)
    else:
        print("Папка не выбрана, обработка не может быть выполнена.")


if __name__ == '__main__':
    main()
