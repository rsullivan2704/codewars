def longest_palindrome(s):
    if not s:
        return 0
    max_length = 0
    for i in range(len(s), 0, -1):
        for j in range(len(s)):
            if s[j:i] == s[j:i][::-1]:
                if len(s[j:i]) > max_length:
                    max_length = len(s[j:i])
    return max_length

def longest_palindrome_comp(s):
    if not s:
        return 0
    palindromes = [palindrome for palindrome in [sub[j:i] for sub in [s] for i in range(len(sub), 0, -1) for j in range(len(sub)) if sub[j:i] and sub[j:i] == sub[j:i][::-1]]]
    return len(max(palindromes, key=len))

print(longest_palindrome("aab"))
print(longest_palindrome("baablkj12345432133d"))


print(longest_palindrome_comp("baablkj12345432133d"))
