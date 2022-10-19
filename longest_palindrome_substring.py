def longestPalindrome( s):
    longest =" "
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            if s[i:j] == s[i:j][::-1]:
                if len(longest) < len(s[i:j]):
                    longest = s[i:j]
    return longest

print(longestPalindrome("forgeeksskeegfor"))