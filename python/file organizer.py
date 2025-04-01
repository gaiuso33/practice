import os
import shutil

folders = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Scripts": [".py", ".js", ".html"]
}

for file in os.listdir():
    file_ext = os.path.splitext(file)[1]
    for folder, extensions in folders.items():
        if file_ext in extensions:
            if not os.path.exists(folder):
                os.mkdir(folder)
            shutil.move(file, folder)
