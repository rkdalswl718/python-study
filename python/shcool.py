def menu(friendName):
    print(f"1. {friendName} 사랑한다 말하기")
    print(f"2. {friendName} 때리기")
    print(f"3. {friendName} 덕담해주기")
    print(f"4. {friendName} 욕설하기")
    print(f"5. {friendName} 맛있는 거 사주기")
    print("6. 종료")

def get_user_choice():
    choice = input("친구에게 할 행동을 선택하세요! : ")
    return choice

def answer(friendName, myName):
    while True:
        menu(friendName)
        user_choice = get_user_choice()
        if user_choice == '1':
            print(f"{friendName}: 갑자기 뭐야 ^^ {myName}, 나도 사랑해~~")
        elif user_choice == '2':
            print(f"{friendName}: 뭐야? 왜 때려? 학교폭력 멈춰!!!!!!!!!!!!!")
        elif user_choice == '3':
            print(f"{friendName}: 좋은말 고마워*^^*")
        elif user_choice == '4':
            print(f"{friendName}: 너 왜 나한테 욕하니? 언어폭력도 학교폭력이야.")
        elif user_choice == '5':
            print(f"{friendName}: 헉! 잘 먹을게~~ {myName}, 고마워! 담엔 내가 쏜다!")
        elif user_choice == '6':
            print("프로그램을 종료합니다. 이용해 주셔서 감사합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

user_myName = input("자신의 이름을 입력하세요: ")
user_friendName = input("친구의 이름을 입력하세요: ")

answer(user_friendName, user_myName)
