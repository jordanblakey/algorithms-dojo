def update_light(current):
    #Given a string representing current color of a traffic light, return a string representing the upcoming color.
    if current == 'green': return 'yellow'
    if current == 'yellow': return 'red'
    if current == 'red': return 'green'
