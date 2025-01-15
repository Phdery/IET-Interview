def numDecodings(s: str, memo=None) -> int:

    # Memoization for some big number
    if memo is None:
        memo = {}
    if not s:
        return 1
    if s[0] == '0':
        return 0

    result = 0

    # daq 1
    result += numDecodings(s[1:], memo)

    # 2
    if len(s) >= 2 and 10 <= int(s[:2]) <= 26:
        result += numDecodings(s[2:], memo)
    memo[s] = result
    
    return result


s1 = "226"
decode = numDecodings(s1)
print("The final result should be: 3")
print("The final result: ", decode)