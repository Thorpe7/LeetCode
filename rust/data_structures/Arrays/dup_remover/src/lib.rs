/**
 * 26. Remove Duplicates from Sorted Array Rust implementation
 *
 */
pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
    let vec_length = nums.len();

    if vec_length == 0 {
        0;
    }

    let mut insert_at_index = 1;
    for idx in 1..nums.len() {
        if nums[idx] != nums[idx - 1] {
            nums[insert_at_index] = nums[idx];
            insert_at_index += 1;
        }
    }

    insert_at_index as i32
}
