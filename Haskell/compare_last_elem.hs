module Codewars.IsThisMyTail where

-- Given a string and a single character, return true if the character matches the last char in the string.
correctTail :: String -> Char -> Bool
correctTail b t = last b == t 
