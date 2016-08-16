-- Implementation of a Binary Search tree in Haskell
-- author : Thomas Minier

data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show, Read, Eq)

insert :: (Ord a) => a -> Tree a -> Tree a
insert x EmptyTree = Node x EmptyTree EmptyTree
insert x (Node y left right)
  | x == y = Node x left right
  | x < y = Node y (insert x left) right
  | x > y = Node y left (insert x right)

contains :: (Ord a) => a -> Tree a -> Bool
contains x EmptyTree = False
contains x (Node y left right)
    | x == y = True
    | x < y  = contains x left
    | x > y  = contains x right

delete :: (Ord a) => a -> Tree a -> Tree a
delete _ EmptyTree = EmptyTree
delete x (Node y left right)
  | x < y = delete x left
  | x > y = delete x right
  | x == y = Node (maxTree right) left right -- need to remove the Leaf with the max elt in right

validTree :: (Ord a) => Tree a -> Bool
validTree EmptyTree = True
validTree (Node _ EmptyTree EmptyTree) = True
validTree (Node _ left EmptyTree) = validTree left
validTree (Node _ EmptyTree right) = validTree right
validTree (Node x left@(Node y _ _) right@(Node z _ _))
  | (x < y) && (x > z) = validTree left && validTree right
  | otherwise = False

minTree :: (Ord a) => Tree a -> Tree a
minTree (Node x EmptyTree _) = x
minTree (Node _ left _) = minTree left

maxTree :: (Ord a) => Tree a -> a
maxTree (Node x _ EmptyTree) = x
maxTree (Node _ _ right) = maxTree right

fromList :: (Ord a) => [a] => Tree a
fromList x = foldr insert EmptyTree x

toList :: (Ord a) => Tree a -> [a]
toList EmptyTree = []
toList (Node x left right) = (toList left) ++ [x] ++ (toList right)
