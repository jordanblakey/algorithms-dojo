import csv

# with open('names.csv', 'r') as csv_file:  # Open context (read)

# # load the csv file into csv.reader module
#   csv_reader = csv.reader(csv_file)
#   # print(dir(csv_reader)) # Print all methods
#   print(csv_reader)  # csv reader object (generator)
#   print('Line number: ' + str(csv_reader.line_num))  # 0
#   next(csv_reader)  # Step over the column header
#   print('Line number: ' + str(csv_reader.line_num))  # 1

#   with open('new_names.csv', 'w') as new_file:
#     # quotes strings containing delimiter
#     csv_writer = csv.writer(new_file, delimiter='\t')

#     for line in csv_reader:
#       csv_writer.writerow(line)
#       # print(line[0])


with open('names.csv', 'r') as csv_file:
  # DictReader creates dictionaries for each row
  csv_reader = csv.DictReader(csv_file)

  # for line in csv_reader:
  #   print(line.keys())
  # print(line['email'])  # Print values by column name

  # Rrray to hold fieldnames
  fieldnames = [x for x in csv_reader.next().keys()]
  # print(fieldnames)

  with open('new_names2.csv', 'w') as new_file:
    csv_writer = csv.DictWriter(
        new_file, fieldnames=fieldnames, delimiter='\t')
    csv_writer.writeheader()
    for line in csv_reader:
      print(line['email'])
      del line['email']
      csv_writer.writerow(line)
