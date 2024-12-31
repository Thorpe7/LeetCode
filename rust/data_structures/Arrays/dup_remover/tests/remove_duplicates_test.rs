/// Integration style test for main script.
use dup_remover::remove_duplicates;

#[test]
fn test_remove_duplicates_case_one() {
    let mut nums1 = vec![1, 1, 2];
    let result1: i32 = remove_duplicates(&mut nums1);
    assert_eq!(result1, 2)
}

#[test]
fn test_remove_duplicates_case_two() {
    let mut nums2 = vec![0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
    let result2: i32 = remove_duplicates(&mut nums2);
    assert_eq!(result2, 5)
}
