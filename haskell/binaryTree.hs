-- Implementation of a Binary Search tree in Haskell
-- author : Thomas Minier

data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show, Read, Eq)

insertTree :: Ord a => a -> Tree a -> Tree a
insertTree x EmptyTree = Node x EmptyTree EmptyTree
insertTree x (Node y left right)
  | x == y = Node x left right
  | x < y = Node y (insertTree x left) right
  | x > y = Node y left (insertTree x right)

treeElem :: (Ord a) => a -> Tree a -> Bool
treeElem x EmptyTree = False
treeElem x (Node y left right)
    | x == y = True
    | x < y  = treeElem x left
    | x > y  = treeElem x right
