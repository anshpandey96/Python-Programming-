import os
directory_path = '/New folder'

#list all files and directories in the specified path 
contents= os.listdir(directory_path)

# print each file and directory name 
for item in contents:
    print(item)