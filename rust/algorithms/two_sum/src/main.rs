use two_sum::TwoSum;

fn main() {
    let nums = vec![2, 7, 11, 15];
    let target = 9;

    let result = TwoSum::run_two_sum(nums, target);

    if !result.is_empty() {
        println!("Indices: {:?}", result);
    } else {
        println!("No solution found.");
    }
}
