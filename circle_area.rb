def circle_area(circle)
  # Given an instance of class Circle, circle, with attributes circle.radius, circle.center.x, circle.center.y, 
  # return the circle's area.
  print "Radius: ", circle.radius, "\n"
  print "Center: ", circle.center.x, ",", circle.center.y, "\n"
  return circle.radius**2 * Math::PI
end
