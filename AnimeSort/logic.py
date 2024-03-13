# date of create 12.03.24

import os


def process_folder(folder_path):
    print(f"Обработка папки: {folder_path}")
        for root, dirs, filenames in os.walk(folder_path):
        print(f"root: {root}")
        print(f"dirs: {dirs}")
        print(f"filenames: {filenames}")
    # for root, dirs, files in os.walk(folder_path):
    #     print(root, dirs, files)
    #     for file in files:
    #         file_path = os.path.join(root, file)
    #         print(file_path)
