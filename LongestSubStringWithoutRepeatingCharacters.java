import java.util.HashMap;
import java.util.HashSet;

public class LongestSubStringWithoutRepeatingCharacters {
    /** Longest SubString Without Repeating Characters
     *  Example:
     *  "abcabcbb"  --> "abc", which length is 3
     *  "bbbbb"   --> "b", which length is 1.
     *  "pwwkew"  --> "wke", which length is 3.
     *  ATTENTION: SubString. "pwke" is sequence and not a substring.
     *
     * **/

    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0)
            return 0;
        HashMap<Character, Integer> map = new HashMap<>();
        int res = 0;
        for (int i = 0, j = 0; i < s.length(); i++){
            if (map.containsKey(s.charAt(i))) {
                j = Math.max(j, map.get(s.charAt(i)) + 1);
            }
            map.put(s.charAt(i), i);
            res = Math.max(res, i - j + 1);
        }
        return res;
    }

    public int lengthOfLongestSubstringSet(String s) {
        if (s == null || s.length() == 0)
            return 0;
        HashSet<Character> set = new HashSet<>();
        int res = 0;
        for (int i = 0, j = 0; i < s.length(); i++) {
            if (set.contains(s.charAt(i))) {
                set.remove(s.charAt(j++));
            } else  {
                set.add(s.charAt(i));
                res = Math.max(res, set.size());
            }
        }
        return res;
    }

    public static void main(String[] args) {
        LongestSubStringWithoutRepeatingCharacters ls
                = new LongestSubStringWithoutRepeatingCharacters();

        String s = "pwwkew";
        int res = 0;
//        res = ls.lengthOfLongestSubstring(s);
        res = ls.lengthOfLongestSubstringSet(s);
        System.out.println(res);

    }
}
