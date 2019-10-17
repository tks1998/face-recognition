import os
path = "C://Users//DELL//Desktop//**"
for dirname in os.listdir(path):
    path2 = os.path.join(path,dirname)
    filename, file_extension = os.path.splitext(path2)
    if file_extension == ".jpg":
        os.remove(path2)
