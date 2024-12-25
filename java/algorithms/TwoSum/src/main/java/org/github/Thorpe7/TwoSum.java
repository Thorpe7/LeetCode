/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */
package org.github.Thorpe7;

/**
 *
 * @author Thorpe7
 */
import java.util.HashMap;
import java.util.Map;

class TwoSum {

    public int[] runTwoSum(int[] nums, int target) {

        // Start by creating an empty hashmap
        Map<Integer, Integer> usedNumbers = new HashMap<>();

        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            int complementNum = target - nums[i];

            // If the complement is in the map, we found the answer
            if (usedNumbers.containsKey(complementNum)) {
                // Define the answer array
                int[] twoSumSolutionIdxs = {i, usedNumbers.get(complementNum)};
                return twoSumSolutionIdxs;
            } else {
                usedNumbers.put(nums[i], i);
            }
        }
        // If no solution is found, return type in function signature is int[]
        return new int[0];
    }

    public static void main(String[] args) {
    }
}

/**
 * Explanation:
 *
 *  *- Iterating through a list costs O(n) time complexity.
 *
 *  *- Using a brute force method would cost O(n^2) time complexity.
 *
 *  *- Using a dictionary (HashMap) to store the previous numbers we come
 * across, can reduce the time complexity.
 *
 *  *--- Why does it reduce the time complexity? ---
 *
 * Because to look up a value in a dictionary takes O(1) time complexity. So
 * looking up the compliment number in the dictionary for each element in the
 * list costs 0(n*1) = O(n) time complexity since we drop constants.
 */
