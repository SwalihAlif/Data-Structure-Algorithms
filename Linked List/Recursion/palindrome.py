def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

my_str = 'swalih'
my_st = 'malayalam'
print(palindrome(my_str))
print(palindrome(my_st))