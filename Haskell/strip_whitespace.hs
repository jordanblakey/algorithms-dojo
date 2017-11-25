-- Strip all spaces from a string
module Kata (noSpace) where
import Data.Char

noSpace :: String -> String
noSpace str = [x | x <- str, x /= ' ']
