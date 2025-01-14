pub fn search_insert(nums: &Vec<i32>, target: i32) -> i32 {
    let mut left_pointer: usize = 0;
    let mut right_pointer: usize = nums.len();
    let mut middle: usize = 0;

    while left_pointer < right_pointer {
        middle = left_pointer + (right_pointer - left_pointer) / 2;

        if nums[middle] == target {
            return middle as i32;
        } else if target > nums[middle] {
            left_pointer = middle + 1;
        } else {
            right_pointer = middle;
        }
    }
    left_pointer as i32
}
