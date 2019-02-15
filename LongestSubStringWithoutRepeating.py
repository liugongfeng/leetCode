






"""
@:param s, a string.
"""
def lengthOfLongestSubstringSet(s):
    if len(s) == 0 :
        return
    reset = set()
    length = 0
    j = 0
    for i in range(len(s)):
        if s[i] in reset:
            reset.remove(s[j])
            j += 1
        else:
            reset.add(s[i])
            length = max(len(reset), length)
    return length


if __name__ == "__main__":
    ss = "pwwkew"
    result = lengthOfLongestSubstringSet(ss)
    print(result)

