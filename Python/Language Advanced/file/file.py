# open for reading, writing, appending

# FILE MODES ##################################################################
# f = open('test.txt')  # read
# f = open('test.txt', 'r')  # read
# f = open('test.txt', 'w')  # write
# f = open('test.txt', 'a')  # append
# f = open('test.txt', 'r+')  # read & write


# BASIC METHODS ###############################################################
# open('test.txt', 'w')  # open the file for writing
# f = open('test.txt', 'r')  # open the file for reading
# print(f.name)  # print the filename
# print(f.mode)  # r/w/a/r+
# print(f.read())  # read file contents
# f.close()  # close the file
# f.closed  # Boolean indicating whether the file is closed


# CONTEXT MANAGER: with #######################################################
# automatically closes after the code block &
# Also closes file on exceptions. Best practice.
# with open('test.txt', 'r') as f:
#   f_contents = f.read()
#   print(f_contents, end='')  # end arg used to suppress newline

# with open('test.txt', 'r') as f:
#   f_contentlist = f.readlines()
#   print(f_contentlist)

# with open('test.txt', 'r') as f:
#   print(f.readline(), end='')
#   print(f.readline(), end='')
#   print(f.readline(), end='')

# print(f.mode) # Still reads 'r'
# print(f.closed) # But f.closed = True


# LOOPING OVER LINES ##########################################################
# Will read entire file without storing the whole file in memory
# with open('test.txt', 'r') as f:
#   for line in f:
#     print(line, end='')


# READ BY BLOCK ###############################################################
# Will read x characters without storing the whole file in memory
# with open('test.txt', 'r') as f:
#   size_to_read = 10
#   f_contents = f.read(size_to_read)  # Read 100 characters (bytes) at a time
#   while len(f_contents) > 0:
#     print(f_contents, end='*')
#     f_contents = f.read(size_to_read)  # Advance the reader


# MANIPULATE FILE POSITION ####################################################
# with open('test.txt', 'r') as f:
#   print(f.tell())  # 0

#   size_to_read = 10
#   f_contents = f.read(size_to_read)
#   print(f_contents, end='')
#   print(f.tell())  # 10

#   f.seek(0)
#   print(f.tell())  # 0

#   f_contents = f.read(size_to_read)
#   print(f_contents)
#   print(f.tell())  # 10


# MODE ERRORS #################################################################
# with open('test.txt', 'r') as f:
#   f.write('Test')  # io.UnsupportedOperation: not writable

# READ, WRITE, SEEK ###########################################################
# with open('test2.txt', 'r+') as f:  # Creates the file. Will overwrite
#   f.write('Test')  # "Test"
#   print(f.tell())  # 4
#   f.seek(0)
#   print(f.read())  # "Test"
#   f.seek(0)
#   print(f.tell())  # 0
#   f.write('R')  # Overwrites existing characters => "Rest"


# WORKING WITH IMAGES #########################################################

# Copy an image file (by line)
with open('test.gif', 'rb') as rf:  # rb = read binary
  with open('test_copy.gif', 'wb') as wf:  # wb = write binary
    for line in rf:
      wf.write(line)

# Copy an image file (by chunck size)
with open('test.gif', 'rb') as rf:  # rb = read binary
  with open('test_copy_chunk.gif', 'wb') as wf:  # wb = write binary
    chunk_size = 4096
    rf_chunk = rf.read(chunk_size)
    while len(rf_chunk) > 0:
      wf.write(rf_chunk)
      rf_chunk = rf.read(chunk_size)
