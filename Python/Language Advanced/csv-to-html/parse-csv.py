import csv

html_output = ''
names = []

with open('names.csv', 'r') as data_file:  # open the file
  csv_data = csv.DictReader(data_file)  # Create the csv.reader generator

  # Preints the reader object(generator)
  # print(csv_data)

  # creates a list of lists from generator
  # print(list(csv_data))

  next(csv_data)  # Step over the header row

  # print(dir(csv_data))

  for line in csv_data:
    if csv_data.line_num <= 26:
      # print(line)  # print line as list
      names.append(f"{line['id']} {line['first_name']} {line['last_name']}")
    else:
      break

  # for name in names:
  #   print(name)

  html_output += f'''
<p>There are currently {len(names)} public contributors.</p>'''

  html_output += '\n<ul>'

  for name in names:
    html_output += f'\n  <li>{name}</li>'

  html_output += '\n</ul>'

  print(html_output)
