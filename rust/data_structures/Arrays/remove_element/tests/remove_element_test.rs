use remove_element::remove_element;

#[test]
fn test_element_remover_case_one() {
    let mut nums1 = vec![3, 2, 2, 3];
    let val1: i32 = 3;
    let result1 = remove_element(&mut nums1, val1);
    assert_eq!(result1, 2)
}

#[test]
fn test_element_remover_case_two() {
    let mut nums2 = vec![0, 1, 2, 2, 3, 0, 4, 2];
    let val2: i32 = 2;
    let result2 = remove_element(&mut nums2, val2);
    assert_eq!(result2, 5)
}
