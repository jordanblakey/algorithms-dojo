# Javascript Object Notation
import json

# WORKING WITH STRINGS: json.loads ######################
# people_string = '''
# {
#   "people": [
#     {
#       "name": "John Smith",
#       "phone": "123-123-1234",
#       "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
#       "has_license": false
#     },
#     {
#       "name": "Jane Doe",
#       "phone": "123-123-1234",
#       "emails": null,
#       "has_license": true
#     }
#   ]
# }
# '''

# data = json.loads(people_string)
# print(type(data))  # dict
# # print(data)
# print(type(data['people']))  # list

# for person in data['people']:
#   # print(person['name'])
#   del person['phone']
#   # print(person)

# data = json.dumps(data, indent=2, sort_keys=True)

# print(data)
# # print(new_string)


#############################################################
# WORKING WITH FILES: json.load
#############################################################

with open('states.json', 'r') as f:
  data = json.load(f)

for state in data['states']:
  del state['area_codes']
  # print(state['name'], state['abbreviation'])

with open('states-new.json', 'w') as f:  # open file write context
  json.dump(data, f, indent=2)  # dump indented json to file


#############################################################
# WORKING WITH APIS: urllib.request
#############################################################
from urllib.request import urlopen
url = 'https://jsonplaceholder.typicode.com/todos'
with urlopen(str(url)) as response:
  source = response.read()

data = json.loads(source)
# print(json.dumps(data, indent=2))

for item in data:
  # print(item)
  title = item['title']
  status = 'Complete' if item['completed'] == True else 'Incomplete'
  print(title + ', ' + str(status))

print('Response Item Count: ' + str(len(data)))
