import java.util.HashMap;

public class LeetCode003 {

    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0)
            return 0;

        int start = -1;
        int result = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i)) && map.get(s.charAt(i)) > start) {
                start = map.get(s.charAt(i));
                map.put(s.charAt(i), i);
            } else {
                map.put(s.charAt(i), i);
                if (i - start > result) {
                    result = i - start;
                }
            }
        }

        return result;
    }

}