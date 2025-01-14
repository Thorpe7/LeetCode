use search_insert_position::search_insert;

#[test]
fn test_search_insert_case_one() {
    let nums1 = vec![1, 3, 5, 6];
    let target: i32 = 2;
    let result1 = search_insert(&nums1, target);
    assert_eq!(result1, 1)
}

#[test]
fn test_search_insert_case_two() {
    let nums2 = vec![1, 3, 5, 6];
    let target2: i32 = 7;
    let result2 = search_insert(&nums2, target2);
    assert_eq!(result2, 4)
}
