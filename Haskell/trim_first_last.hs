module Haskell.Codewars.RemoveChar where
-- Given a string, remove its first and last characters.
removeChar :: String -> String
removeChar str = init (drop 1 str)
