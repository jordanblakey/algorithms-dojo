def sakura_fall(v)
  # Given a constant speed, return the time to travel 400 units 
  print v
  if v <= 0 
    return 0
  end
  return 400/v.to_f
end
