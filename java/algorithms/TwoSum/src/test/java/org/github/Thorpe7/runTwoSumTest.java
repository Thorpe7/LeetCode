package org.github.Thorpe7;

/**
 * JUnit test for TwoSum Solution.
 */
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;

public class runTwoSumTest {

    @Test
    public void testRunTwoSum() {
        TwoSum twoSumObj = new TwoSum();

        // Test Case 1
        int[] nums1 = {2, 7, 11, 15};
        int target1 = 9;
        int[] results1 = {0, 1};
        int[] twoSumSolutionIdx1 = twoSumObj.runTwoSum(nums1, target1);
        Arrays.sort(twoSumSolutionIdx1);
        assertArrayEquals(results1, twoSumSolutionIdx1);

        // Test Case 2
        int[] nums2 = {3, 2, 4};
        int target2 = 6;
        int[] results2 = {1, 2};
        int[] twoSumSolutionIdx2 = twoSumObj.runTwoSum(nums2, target2);
        Arrays.sort(twoSumSolutionIdx2);
        assertArrayEquals(results2, twoSumSolutionIdx2);

        // Test Case 3
        int[] nums3 = {3, 3};
        int target3 = 6;
        int[] results3 = {0, 1};
        int[] twoSumSolutionIdx3 = twoSumObj.runTwoSum(nums3, target3);
        Arrays.sort(twoSumSolutionIdx3);
        assertArrayEquals(results3, twoSumSolutionIdx3);
    }
}
