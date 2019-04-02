public class LeetCode005 {

    public String longestPalindrome(String s) {
        String palindrome = "";

        for (int i = 0; i < s.length(); i++) {
            String strs1 = getLongestPalindrome(s, i, i);
            if (strs1.length() > palindrome.length()) {
                palindrome = strs1;
            }

            String strs2 = getLongestPalindrome(s, i, i + 1);
            if (strs2.length() > palindrome.length()) {
                palindrome = strs2;
            }

        }

        return palindrome;
    }

    public String getLongestPalindrome(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l -= 1;
            r += 1;
        }

        return s.substring(l + 1, r);
    }

}