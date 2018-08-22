from collections import namedtuple

Color = namedtuple('Color', ['red', 'blue', 'green'])
white = Color(255,255,255)
black = Color(0,0,0)

print('White: {}'.format(white))
print('Black: {}'.format(black))