import os
from datetime import datetime

# Recon for objects, classes, modules
vars(os)  # Get all properties of module
dir(os)  # Get all methods of object, class, or module

# File tree navigation ########################################################
os.listdir()  # return array with cwd contents
os.getcwd()  # get current working directory
os.chdir('/root/Desktop')  # Change directories. Takes an absolute path.
os.walk()  # Generator that yields a tuple (path, dirs, files)

# Traverse the file tree downward
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
  print('Current Path:', dirpath)
  print('Directories:', dirnames)
  print('Files:', filenames)
  print()


# Making and removing directories #############################################
os.mkdir('os-demo-2/sub-dir-1')  # will only create the last dir
os.makedirs('os-demo-2/sub-dir-1')  # Will make parent dirs

os.rmdir('os-demo-2/sub-dir-1')  # delete only the last dir
os.removedirs('os-demo-2/sub-dir-1')  # deletes all dirs in the path (!!)

os.rename('test.txt', 'demo.txt')  # rename existing file

os.stat('test.txt')  # return info on file
os.stat('test.txt').st_size  # get filesize in bytes
mod_time = os.stat('test.txt').st_mtime  # modified time
print(datetime.fromtimestamp(mod_time))


# Environment Variables #######################################################
os.environ()
os.environ.get('HOME')

# Error prone pathing
# file_path =  os.environ.get('HOME') + 'test.txt'
# print(file_path)

# FILE CREATION ###############################################################

# create a file in the HOME folder
with open(os.path.join(os.environ.get('HOME'), 'test.txt'), 'w') as f:
  f.write('Hello world')

# simpler
with open('new2.txt', 'w') as f:
  f.write('New file text.')

# ABSOLUTE PATHS ##############################################################
# Get basename
os.path.basename()
os.path.basename(os.path.join(os.getcwd(), 'test.txt'))  # test.txt
os.path.basename('/root/Desktop/python/src/test.txt')  # test.txt

# /root/Desktop/python/src
os.path.dirname('/root/Desktop/python/src/test.txt')

# SPLIT: ('/root/Desktop/python/src', 'test.txt')
path_name = os.path.split('/root/Desktop/python/src/test.txt')

# JOIN: # join removes or adds slashes
os.path.join(path_name[0], path_name[1])
os.path.join(os.environ.get('HOME'), 'test.txt')

# CHECKING EXISTENCE AND TYPE #################################################
os.path.exists('/tmp/test.txt')  # False
os.path.exists('/tmp')  # True
os.path.isdir('/tmp')  # True
os.path.isfile('/tmp')  # False

os.path.splitext('/tmp/test.txt')  # ('/tmp/test', '.txt')

print(dir(os.path()))  # See all methods of os.path
