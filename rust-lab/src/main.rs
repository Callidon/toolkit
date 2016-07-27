// Author : Thomas Minier
extern crate rand;

mod guessing;
mod mergesort;

fn main() {
    // Guessing game
    //guessing::guessing();

    // Merge sort
    let v = vec!(5,1,4,3,2,6);
    let w = mergesort::merge_sort(&v);
    println!("{:?}", w);
}
