// Author : Thomas Minier
extern crate rand;

mod mergesort;
mod trees;

use trees::binary;

fn main() {

    // Binary tree
    let mut n = binary::Node::new(2);
    println!("{:?}", n);
    println!("The tree is a binary tree ? {}", n.check());
    n.insert(3);
    println!("{:?}", n);
    println!("The tree is a binary tree ? {}", n.check());
    n.insert(1);
    println!("{:?}", n);
    println!("The tree is a binary tree ? {}", n.check());
    {
        let s = n.search(3);
        println!("searching 3, found : {:?}", s);
    }
    n.insert(1);
    println!("{:?}", n);
    println!("The tree is a binary tree ? {}", n.check());
}
