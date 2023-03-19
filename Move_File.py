import os
import shutil

from_dir="C:\Users\pc\OneDrive\Desktop\white hat jr project\Project102"
to_dir="E:\Document_Files"

list_of_files=os.listdir()
#print(list_of_files)

for file_name in list_of_files:

    name,extension=os.path.splitext(file_name)

    if extension=='':
        continue
if extension in ['.gif','.png','.jpg','jpeg','.jfif']:

    path1=from_dir+'/'+file_name
    path2=to_dir+'/'+"Image_files"
    path3=to_dir+'/'+"Image_files"+'/'+file_name

    if os.path.exists(path2):
        print("Moving"+ file_name+"......")

        shutil.move(path1,path3)

    else:
        os.makedirs(path2)
        print("Moving"+file_name+".......")
        shutil.move(path1,path3)



