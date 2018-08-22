import os
import re

# print(os.getcwd())

# cd into the videos dir
os.chdir('videos')
# print(os.getcwd())

# Print all filenames
for f in os.listdir(os.getcwd()):
  # print(f)
  f_name, f_ext = os.path.splitext(f)
  arr = [x.strip() for x in re.findall(r"[^-#]+", f_name)]
  f_title, f_course, f_num = arr  # deconstruct
  f_num = f_num.zfill(2)  # pad with zeroes
  # format the new file string
  new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
  os.rename(f, new_name)
