-- Experiments using Haskell, from "Learn you a Haskell for Great Good"
-- Author : Thomas Minier

-- Very basic stuff
doubleMe x = x * 2
doubleUs x y = x*2 + y*2
doubleSmallNum x = if x > 100 then x else x*2
doubleSmallNum' x = (doubleSmallNum x) - 1

removeNonUppercase :: [Char] -> [Char]
removeNonUppercase str = [ c | c <- str, elem c ['A'..'Z']]

rightTriangle :: Int -> [ (Int, Int, Int)]
rightTriangle n = [ (a,b,c) | c <- [1..n], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2, a+b+c == 24]

-- pattern matching
lucky :: (Integral a) => a -> String
lucky 7 = "Lucky number"
lucky x = "out of luck"

factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- higher-order functions
zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (x:tx) (y:ty) = f x y : zipWith' f tx ty
