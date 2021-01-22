# 프로그래머스 코딩테스트 연습문제

# 정수 배열 numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return
# numbers = [2,1,3,4,1]
# return = [2,3,4,5,6,7]
def sum_list_func(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # 중복방지
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])

    answer.sort()

    return answer


# 선행 스킬 순서 skill과 유저들이 만든 스킬트리를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return
# skill = "CBD"
# skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# return = 2
def skill_tree_func(skill, skill_trees):
    answer = 0
    index = []
    flag = False

    for skill_tree in skill_trees:
        for s in skill:
            index.append(skill_tree.find(s))

        if sum(index) == -len(index):
            flag = True
        elif len(index) == 1:
            flag = True
        else:
            for i in range(len(index) - 1):
                if index[i] < index[i + 1]:
                    if index[i] == -1:
                        flag = False
                        break
                    else:
                        flag = True
                else:
                    if index[i + 1] == -1:
                        flag = True
                    else:
                        flag = False
                        break

        if flag:
            index = list(filter(lambda a: a != -1, index))
            if sorted(index) == index:
                answer += 1

        flag = False
        index = []

    return answer


# 2016년 1월 1일은 금요일일때, 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴
# a = 5, b = 24
# return "TUE"
def get_2016_dayofweek_func(a, b):
    answer = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

    days = sum(month_days[:a]) + b

    return answer[days % 7 - 1]


# 게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때,
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return
# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves = [1,5,3,5,1,2,1,4]
# return = 4
def get_doll_play_func(board, moves):
    st = []
    length = len(board)
    answer = 0

    for move in moves:
        for i in range(length):
            doll = board[i][move - 1]

            if doll == 0:
                continue

            st.append(doll)
            board[i][move - 1] = 0
            break

        if len(st) >= 2:
            if st[-2] == st[-1]:
                del st[-2:]
                answer += 2

    return answer


# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return
# n = 45
# return = 7
def reverse_3system_func(n):
    x = n
    s = ""

    while x >= 3:
        x, y = divmod(x, 3)
        s += str(y)
    s += str(x)

    return int(s, 3)


# 단어 s의 가운데 글자를 return
# s = "abcde", return = "c"
# s = "qwer", return = "we"
def pick_center_char_func(s):
    answer = ''
    if len(s) % 2 == 1:
        answer = s[len(s) // 2]
    else:
        answer = s[len(s) // 2 - 1:len(s) // 2 + 1]
    return answer


# 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때,
# 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return
# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"
# return = "LRLLLRLLRRL"
def pushing_keypad_func(numbers, hand):
    answer = ''
    left_x, left_y = 0, 3
    right_x, right_y = 2, 3

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left_x = 0
            if num == 1:
                left_y = 0
            elif num == 4:
                left_y = 1
            elif num == 7:
                left_y = 2
        elif num in [3, 6, 9]:
            right_x = 2
            answer += 'R'
            if num == 3:
                right_y = 0
            elif num == 6:
                right_y = 1
            elif num == 9:
                right_y = 2
        elif num in [2, 5, 8, 0]:
            x, y = -1, -1
            if num == 2:
                x, y = 1, 0
            elif num == 5:
                x, y = 1, 1
            elif num == 8:
                x, y = 1, 2
            elif num == 0:
                x, y = 1, 3

            l_temp = abs(left_x - x) + abs(left_y - y)
            r_temp = abs(right_x - x) + abs(right_y - y)

            print(l_temp, r_temp)

            if l_temp < r_temp:
                answer += 'L'
                left_x = x
                left_y = y
            elif l_temp > r_temp:
                answer += 'R'
                right_x = x
                right_y = y
            else:
                if hand[0] == 'l':
                    answer += 'L'
                    left_x = x
                    left_y = y
                else:
                    answer += 'R'
                    right_x = x
                    right_y = y

        # print("num : {} -- left ({}, {}) right ({}, {})".format(num, left_x, left_y, right_x, right_y))
        # print(num)

    return answer
