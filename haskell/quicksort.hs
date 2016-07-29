-- Implementation of the quick sort algorithm in Haskell
-- Author : Thomas Minier

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:tx) =
  let leftSorted = quicksort (filter (<= x) tx)
      rightSorted = quicksort (filter (> x) tx)
  in leftSorted ++ [x] ++ rightSorted
