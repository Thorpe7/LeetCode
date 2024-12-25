use std::collections::HashMap;

pub struct TwoSum;

impl TwoSum {
    pub fn run_two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        // Create an empty HashMap to store seen numbers
        let mut seen_nums: HashMap<i32, i32> = HashMap::new();

        for (idx, num) in nums.iter().enumerate() {
            let complement_num: i32 = target - num;

            // Check if the complementry number is in the HashMap
            if seen_nums.contains_key(&complement_num) {
                // If the complement is in the map, we have found our answer
                if let Some(&complement_idx) = seen_nums.get(&complement_num) {
                    return vec![complement_idx, idx as i32];
                }
            } else {
                // If complement not in the map, add current value w/ idx as value
                seen_nums.insert(*num, idx as i32);
            }
        }
        // If no solution found, fn signature specifies Vec<i32> return
        vec![]
    }
}

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
