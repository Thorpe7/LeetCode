pub impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let words: Vec<&str> = s.trim().split_whitespace().collect();
        words.last().unwrap().len() as i32
    }
}