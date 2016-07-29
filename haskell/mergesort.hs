-- Implementation of the merge sort algorithm in Haskell
-- Author : Thomas Minier

merge :: (Ord a) => [a] -> [a] -> [a]
merge x [] = x
merge [] y = y
merge left@(x:tx) right@(y:ty) = if x <= y then x:(merge tx right) else y:(merge left ty)

halves :: (Ord a) => [a] -> ([a], [a])
halves x =
  let n = length x `div` 2
  in ((take n x), (drop n x))

mergesort :: (Ord a) => [a] -> [a]
mergesort [] = []
mergesort [x] = [x]
mergesort x =
  let (left, right) = halves x
  in merge (mergesort left) (mergesort right)
