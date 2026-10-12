class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) {
            return "";
        }

        int start = 0;
        int maxLen = 0;

        for (int i = 0; i < s.length(); i++) {
            // Case 1: Odd-length palindromes (center at i)
            int len1 = expandAroundCenter(s, i, i);
            // Case 2: Even-length palindromes (center between i and i + 1)
            int len2 = expandAroundCenter(s, i, i + 1);

            int currentLen = Math.max(len1, len2);
            if (currentLen > maxLen) {
                maxLen = currentLen;
                // Calculate the start index based on current center i and length
                start = i - (currentLen - 1) / 2;
            }
        }

        return s.substring(start, start + maxLen);
    }

    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        // When the loop ends, left and right have gone 1 step too far.
        // Length = (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1;
    }
}