/// Integration style test for main script.
use two_sum::TwoSum;

#[test]
fn test_two_sum_case_one() {
    let nums1 = vec![2, 7, 11, 15];
    let target1: i32 = 9;
    let mut result1: Vec<i32> = TwoSum::run_two_sum(nums1, target1);
    result1.sort();
    assert_eq!(result1, vec![0, 1])
}

#[test]
fn test_two_sum_case_two() {
    let nums2 = vec![3, 2, 4];
    let target2: i32 = 6;
    let mut result2: Vec<i32> = TwoSum::run_two_sum(nums2, target2);
    result2.sort();
    assert_eq!(result2, vec![1, 2])
}

#[test]
fn test_two_sum_case_three() {
    let nums3 = vec![3, 3];
    let target3: i32 = 6;
    let mut result3: Vec<i32> = TwoSum::run_two_sum(nums3, target3);
    result3.sort();
    assert_eq!(result3, vec![0, 1])
}
