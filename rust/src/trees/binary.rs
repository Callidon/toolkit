// Binary search tree implemented in Rust
// Author : Thomas Minier
use std::fmt;
use std::cmp;

// Binary Search tree implementation using a struct.
pub struct Node<T> where T: fmt::Display + cmp::PartialOrd {
    value : T,
    left : Option<Box<Node<T>>>,
    right : Option<Box<Node<T>>>
}

impl<T> Node<T> where T: fmt::Display + cmp::PartialOrd {
    // Allocates a new Node.
    pub fn new(v : T) -> Node<T> {
        Node::<T> { value : v, left: None, right : None }
    }

    // Insert a value in the tree.
    pub fn insert(&mut self, v : T) {
        let target = if self.value >= v {
            &mut self.left
        } else {
            &mut self.right
        };
        match target {
            &mut Some(ref mut x) => x.insert(v),
            &mut None => *target = Some(Box::new(Node::<T>::new(v)))
        }
    }

    // Search the node correspondig to a value in the tree.
    pub fn search(&self, v : T) -> Option<&Node<T>> {
        if self.value == v {
            return Some(self)
        }
        let target = if self.value >= v {
            &self.left
        } else {
            &self.right
        };
        match target {
            &Some(ref x) => x.search(v),
            &None => None
        }
    }

    // Verify the integrity of the tree.
    // Returns true if the tree is a Binary Search Tree, false otherwise.
    pub fn check(&self) -> bool {
        match self {
            &Node::<T> { value : ref v, left : Some(ref x), right : None } => (v >= &x.value) && x.check(),
            &Node::<T> { value : ref v, left : None, right : Some(ref x) } => (v < &x.value) && x.check(),
            &Node::<T> { value : ref v, left : Some(ref x), right : Some(ref y) } => (v >= &x.value) && (v < &y.value) && x.check() && y.check(),
            _ => true
        }
    }

    // Serialize the tree into string format.
    pub fn to_string(&self) -> String {
        match self {
            &Node::<T> { value : ref v, left : Some(ref x), right : None } => format!("Node({}, {}, _)", v, x.to_string()),
            &Node::<T> { value : ref v, left : None, right : Some(ref x) } => format!("Node({}, _, {})", v, x.to_string()),
            &Node::<T> { value : ref v, left : Some(ref x), right : Some(ref y) } => format!("Node({}, {}, {})", v, x.to_string(), y.to_string()),
            _ => format!("Node({}, _, _)", self.value)
        }
    }
}

impl<T> fmt::Debug for Node<T> where T: fmt::Display + cmp::PartialOrd {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.to_string())
    }
}

// Binary Search Tree implementation using a enum instead of a struct,
// in a more functionnal style.
#[derive(PartialEq, Eq, Debug, Clone)]
pub enum BST<T> where T: Ord + PartialEq + Eq + Clone + fmt::Display {
    Leaf(T),
    Branch(T, Box<BST<T>>, Box<BST<T>>),
    Nil
}

impl<T> BST<T> where T: Ord + PartialEq + Eq + Clone + fmt::Display {
    // Allocates a new Node.
    pub fn new() -> BST<T> {
        BST::Nil
    }

    // Insert a value in the tree and returns the new tree.
    pub fn insert(&self, v : T) -> BST<T> {
        match self {
            &BST::Nil => BST::Leaf(v),
            &BST::Branch(ref value, ref left, ref right) => {
                match v.cmp(&value) {
                    cmp::Ordering::Less => BST::Branch(value.clone(), Box::new(left.insert(v)), right.clone()),
                    _ => BST::Branch(value.clone(), left.clone(), Box::new(right.insert(v)))
                }
            },
            &BST::Leaf(ref value) => {
                match v.cmp(&value) {
                    cmp::Ordering::Less => BST::Branch(value.clone(), Box::new(BST::Leaf(v)), Box::new(BST::Nil)),
                    _ => BST::Branch(value.clone(), Box::new(BST::Nil), Box::new(BST::Leaf(v)))
                }
            },
        }
    }

    // Delete a value in the tree and returns the new tree.
    // WARNING : doesn't compile yet, need more work with borrow checker :/
    pub fn delete(&self, v : T) -> BST<T> {
        match self {
            &BST::Nil => self.clone(),
            &BST::Leaf(ref value) => {
                match v.cmp(value) {
                        cmp::Ordering::Equal => BST::Nil,
                        _ => self.clone()
                }
            },
            &BST::Branch(ref value, ref left, ref right) => {
                match v.cmp(&value) {
                    cmp::Ordering::Equal => {
                        match (left, right) {
                            (_, BST::Nil) =>  left
                        }
                    },
                    cmp::Ordering::Less => BST::Branch(value.clone(), Box::new(left.delete(v)), right.clone()),
                    cmp::Ordering::Greater => BST::Branch(value.clone(), left.clone(), Box::new(right.delete(v)))
                }
            }
        }
    }

    // Search the node correspondig to a value in the tree.
    pub fn search(&self, v : T) -> Option<T> {
        match self {
            &BST::Leaf(ref x) if &v == x => Some(v),
            &BST::Branch(ref x, ref left, ref right) => {
                match v.cmp(x) {
                    cmp::Ordering::Equal => Some(v),
                    cmp::Ordering::Less => left.search(v),
                    cmp::Ordering::Greater => right.search(v)
                }
            },
            _ => None
        }
    }
}

#[test]
fn test_bst_insert() {
    let root = BST::new().insert(4).insert(5).insert(1).insert(2).insert(6);
    let expected = BST::Branch(4, Box::new(BST::Branch(1, Box::new(BST::Nil), Box::new(BST::Leaf(2)))), Box::new(BST::Branch(5, Box::new(BST::Nil), Box::new(BST::Leaf(6)))));
    assert_eq!(root, expected);
}

#[test]
fn test_bgt_search() {
    let root = BST::new().insert(4).insert(5).insert(1).insert(2).insert(6);
    let s = match root.search(6) {
        Some(x) => x,
        _ => -1
    };
    assert_eq!(s, 6);
}
