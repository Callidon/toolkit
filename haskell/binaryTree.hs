-- Implementation of a Binary Search Tree in Haskell
-- author : Thomas Minier

data BST a = EmptyTree | Node a (BST a) (BST a) deriving (Show, Read, Eq)

-- Insert a value in a Binary Search Tree
insert :: (Ord a) => a -> BST a -> BST a
insert x EmptyTree = Node x EmptyTree EmptyTree
insert x (Node y left right)
  | x == y = Node x left right
  | x < y = Node y (insert x left) right
  | x > y = Node y left (insert x right)

-- Test if a Binary search Tree contains a specific value,
contains :: (Ord a) => a -> BST a -> Bool
contains x EmptyTree = False
contains x (Node y left right)
    | x == y = True
    | x < y  = contains x left
    | x > y  = contains x right

-- Remove a value from a Binary Search Tree
delete :: (Ord a) => a -> BST a -> BST a
delete _ EmptyTree = EmptyTree
delete x (Node y left right)
  | x < y = Node y (delete x left) right
  | x > y = Node y left (delete x right)
  | x == y = case (left, right) of
    (EmptyTree, _)  -> right
    (_, EmptyTree)  -> left
    (Node _ _ _, _) -> Node y' left' right where (y', left') = deleteMax left

-- Remove the max value of a non-empty Binary Search BST and returns both this value and the new tree
deleteMax :: (Ord a) => BST a -> (a, BST a)
deleteMax EmptyTree = error "Cannot delete the maximum of a empty tree"
deleteMax (Node x left EmptyTree) = (x, left)
deleteMax (Node x left right) = (x', Node x left' right) where (x', left') = deleteMax left

-- Test if a Binary Search Tree is correctly build
validTree :: (Ord a) => BST a -> Bool
validTree EmptyTree = True
validTree (Node _ EmptyTree EmptyTree) = True
validTree (Node _ left EmptyTree) = validTree left
validTree (Node _ EmptyTree right) = validTree right
validTree (Node x left@(Node y _ _) right@(Node z _ _))
  | (x < y) && (x > z) = validTree left && validTree right
  | otherwise = False

-- Find the minimum value of a Binary Search Tree
minTree :: (Ord a) => BST a -> a
minTree (Node x EmptyTree _) = x
minTree (Node _ left _) = minTree left

-- Find the maximum value of a Binary search Tree
maxTree :: (Ord a) => BST a -> a
maxTree (Node x _ EmptyTree) = x
maxTree (Node _ _ right) = maxTree right

-- Construct a Binary Search Tree from a list of values
fromList :: (Ord a) => [a] => BST a
fromList x = foldr insert EmptyTree x

-- Construct a list from a Binary Search Tree
toList :: (Ord a) => BST a -> [a]
toList EmptyTree = []
toList (Node x left right) = (toList left) ++ [x] ++ (toList right)
