def hq9(code)
  if code == "H"
    return "Hello World!"
  end
  if code == "Q"
    return code
  end
  if code == "9"
    i = 99
    lyrics = ''
    bottles = 'bottles'
    while i > 0
      lyrics += "#{i} #{bottles} of beer on the wall, #{i} #{bottles} of beer.\n"
      i -= 1
      if i == 1
        bottles = "bottle"
      end
      if i == 0
        lyrics += "Take one down and pass it around, no more bottles of beer on the wall.\n"
      else
        lyrics += "Take one down and pass it around, #{i} #{bottles} of beer on the wall.\n"
      end
    end
    
    lyrics += "No more bottles of beer on the wall, no more bottles of beer.\n"
    lyrics += "Go to the store and buy some more, 99 bottles of beer on the wall."
    return lyrics
  end
end
