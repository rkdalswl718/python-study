import time
import random

word_list = ["안녕하십니까", "저는 윤석열입니다", "나는 지금 잠이 옵니다", "집가고 싶다"]
random.shuffle(word_list)

correct_count = 0  # 정확하게 입력한 횟수
total_characters = 0  # 총 입력한 문자 수
typo_count = 0 

for word in word_list:
    start = time.time()
    print(word)
    user = input().strip()
    end = time.time() - start
    
    total_characters += len(word)
    
    if user == word:
        correct_count += 1
    else:
        typo_count += sum(1 for i, j in zip(user, word) if i != j)

typing_speed = total_characters / (end * len(word_list))  # 타수 계산
accuracy = (correct_count / len(word_list)) * 100  # 정확도 계산
typo_rate = (typo_count / total_characters) * 100  # 오타율 계산

print(f"타수: {typing_speed:.2f} 정확도: {accuracy:.2f}% 오타율: {typo_rate:.2f}%")
