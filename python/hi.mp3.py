def max_score_recursive(n, s):
    if n <= 2:
        return sum(s)
    
    def helper(i):
        if i < 0:
            return 0
        if i == 0:
            return s[0]
        if i == 1:
            return s[0] + s[1]
        
        # 현재 계단을 오를 때 두 가지 옵션을 고려하여 최대값을 계산합니다.
        option1 = helper(i - 3) + s[i - 1] + s[i]
        option2 = helper(i - 2) + s[i]
        
        # 두 옵션 중에서 더 큰 값을 반환합니다.
        return max(option1, option2)
    
    return helper(n - 1)

n = int(input())  # 계단 개수
s = [int(input()) for _ in range(n)]  # 계단 리스트

result = max_score_recursive(n, s)
print(result)
