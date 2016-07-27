// Binary search tree implemented in Rust
// Author : Thomas Minier
use std::fmt;

pub struct Node<T> where T: fmt::Display {
    value : T,
    left : Option<Box<Node<T>>>,
    right : Option<Box<Node<T>>>
}

impl<T> Node<T> where T: fmt::Display {
    pub fn new(v : T) -> Node<T> {
        Node::<T> { value : v, left: None, right : None }
    }

    pub fn insert(&self, v : T) {

    }

    pub fn to_string(&self) -> String {
        match (&self.left, &self.right) {
            (&Some(ref x), &None) => format!("Node({}, {}, _)", self.value, x.to_string()),
            (&None, &Some(ref x)) => format!("Node({}, _, {})", self.value, x.to_string()),
            (&Some(ref x), &Some(ref y)) => format!("Node({}, {}, {})", self.value, x.to_string(), y.to_string()),
            _ => format!("Node({}, _, _)", self.value)
        }
    }
}

impl<T> fmt::Debug for Node<T> where T: fmt::Display {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.to_string())
    }
}
