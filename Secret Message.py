import os

path = r"C:\Users\Rohan Garg\Desktop\Python\alphabet\Message"

def rename_files():
    os.chdir(path)
    file_list = os.listdir(path)

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
