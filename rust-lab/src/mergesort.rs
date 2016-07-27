// Author : Thomas Minier
// Apply Merge sort on two slices
fn merge(left : &[i32], right : &[i32]) -> Vec<i32> {
    let mut res = vec!();
    let (mut left_set, mut right_set) = (left, right);

    while (!left_set.is_empty()) && (!right_set.is_empty()) {
        let (left_head, left_tail) = left_set.split_first().unwrap();
        let (right_head, right_tail) = right_set.split_first().unwrap();
        if left_head <= right_head {
            res.push(*left_head);
            left_set = left_tail;
        } else {
            res.push(*right_head);
            right_set = right_tail;
        }
    }
    // drain collections
    for x in left_set {
        res.push(*x);
    }
    for x in right_set {
        res.push(*x);
    }
    res
}

// Sort a slice using the Merge Sort algorithm
pub fn merge_sort(list : &[i32]) -> Vec<i32> {
    if list.len() <= 1 {
        return list.to_vec();
    }
    let (left, right) = list.split_at(list.len() / 2);
    return merge(&merge_sort(left), &merge_sort(right));
}
