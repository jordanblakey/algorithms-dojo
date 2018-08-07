#!/bin/python
# Print all files on the current users desktop

import os
import glob

home = os.path.expanduser("~")

os.chdir("{}/Desktop".format(home))
for file in glob.glob("*"):
  print(file)


# #!/bin/python
# import os
# import glob
# home = os.path.expanduser("~")

# os.chdir("{}/Desktop".format(home))
# for file in glob.glob("*"):
#   print(file)
