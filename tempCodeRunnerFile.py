number = int(input("정수를 입력하세요 (1~100): "))

if 1 <= number <= 100:
    even_sum = 0
    for i in range(2, number+1, 2):
        even_sum += i

    print(f"1부터 {number}까지 짝수의 합은 {even_sum}입니다.")
else:
    print("1에서 100 사이의 정수를 입력해주세요.")
