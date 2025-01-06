pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
    if nums.len() == 0 {
        0;
    }

    let mut insert_at_index = 0;
    for idx in 0..nums.len() {
        if nums[idx] != val {
            nums[insert_at_index] = nums[idx];
            insert_at_index += 1;
        }
    }
    insert_at_index as i32
}
