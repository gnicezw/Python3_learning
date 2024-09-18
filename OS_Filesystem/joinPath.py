import os
#specify 2 paths
directory = "Output"
parent_dir = "C:\\Users\\nazgu\Documents\\Python3_learning\\OS_Filesystem\\"
print(parent_dir)
#join the paths in a path object
path = os.path.join(parent_dir, directory)
#make a dir from the path object
os.mkdir(path)
#tell the user their directory is created
print("Hey doofus, {} has been created!".format(directory))