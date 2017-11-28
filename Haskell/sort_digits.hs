module Codewars.Kata.Supersize where
import Data.List
-- Given an integer, arrange the digits in the largest possible value.

superSize :: Integer -> Integer
superSize n = read $ reverse $ sort $ show n
