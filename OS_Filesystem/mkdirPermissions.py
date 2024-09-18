import os
#declare name and path
dir_name = "output1"
dir_path = "C:\\Users\\nazgu\\Documents\\Python3_learning\\OS_Filesystem\\"
#join the path and name
path = os.path.join(dir_path, dir_name)
#set permissions
mode = 0o755
# make the dir with path+permissions
os.mkdir(path, mode)
#Tell the user their directory is done
print("Hey doof! Your dir {} is done!".format(dir_name))