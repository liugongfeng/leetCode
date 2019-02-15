import java.util.HashMap;
import java.util.Map;

/** Given an array of integers, return indices of the two numbers
 *  such that they added up to a specific target.
 * Example:
 *  Given nums = [2, 7, 11, 15], target = 9
 *
 *  Because num[0] + num[1] = 9
 *  return [0, 1]
 *
 * */
public class twoSum {

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] x = new int[]{0, 0};
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            int other = target - nums[i];
            if (map.containsKey(other)) {
                int pos = map.get(other);
                if (pos == i)  continue;
                x[0] = i;
                x[i] = pos;
                return x;
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }

}
