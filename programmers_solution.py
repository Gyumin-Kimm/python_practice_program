# 프로그래머스 코딩테스트 연습문제

from collections import deque

import enum
import collections


# 배열의 크기 rows, columns가 주어질 때, (query[0], query[1]) -> (query[2], query[3])
# 시계방향으로 한칸씩 rotate 시키기
def print_t(table):
    for i in table:
        print(i)
    print()


def rotate_table(matrix, q):
    # 배열 index에 맞게 변경
    # print("q(org) : {}".format(q))
    q = [x - 1 for x in q]
    # print("q : {}".format(q))

    # 초기값
    pre = matrix[q[0]][q[1]]
    curr = 0
    # print("tmp : {}".format(pre))

    # (q[0], q[1]->q[3])
    for i in range(q[1] + 1, q[3] + 1):
        curr = matrix[q[0]][i]
        matrix[q[0]][i] = pre
        pre = curr

    # (q[0]->q[2], q[3])
    for i in range(q[0] + 1, q[2] + 1):
        curr = matrix[i][q[3]]
        matrix[i][q[3]] = pre
        pre = curr

    # (q[2], q[3]->q[1])
    for i in range(q[3] - 1, q[1] - 1, -1):
        curr = matrix[q[2]][i]
        matrix[q[2]][i] = pre
        pre = curr

    # (q[2]->q[0], q[1])
    for i in range(q[2] - 1, q[0] - 1, -1):
        curr = matrix[i][q[1]]
        # print("curr:{} pre:{}".format(curr, pre))
        matrix[i][q[1]] = pre
        pre = curr

    # print_t(matrix)


def solution(rows, columns, queries):
    answer = []

    matrix = []
    i = 1
    for row in range(rows):
        cols = []
        for col in range(columns):
            cols.append(i)
            i += 1

        matrix.append(cols)

    for query in queries:
        rotate_table(matrix, query)
        # print_t(matrix)
        # print("---------------")

    print_t(matrix)

    return answer


# print(solution(6, 6, [[2, 2, 5, 4]]))
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))


# 동아리 인원수 n, 동아리 학번종류 m, 전공 k 보다 큰 동아리 수 구하기
def solution(students, n, m, k):
    answer = 0
    d_num = dict()
    d_num_major = dict()
    d_major = dict()
    s_nums = set()
    dup_num = set()

    # 분류
    for student in students:
        s_num, s_major, s_com = student.split()

        # 중복체크(중복값 중 첫 번째 값은 들어감 size 비교할 때 제외예정)
        if s_num in s_nums:
            dup_num.add(s_num)
        else:
            s_nums.add(s_num)
            d_num_major[s_num] = s_major

            # 학번
            if s_com not in d_num:  # 딕셔너리값이 없으면
                d_num[s_com] = list()  # 리스트 생성
            d_num[s_com].append(s_num)

            # 학과
            if s_com not in d_major:
                d_major[s_com] = list()
            d_major[s_com].append(s_major)

    # print("d_num : ", d_num)
    # print("d_num_major : ", d_num_major)
    # print("d_major : ", d_major)
    # print("dup_num : ", dup_num)

    # 동아리 별 체크
    for key in d_num.keys():

        # 중복 값 중 1개씩은 빼줘야함
        for dn in dup_num:
            if dn in d_num[key]:
                d_num[key].remove(dn)
                d_major[key].remove(d_num_major[dn])
                # print("delete : {} / {} / {}".format(key, dn, d_num_major[dn]))

        # 학번
        num2 = set([x[:2] for x in d_num[key]])

        if len(d_num[key]) >= n and len(num2) >= m and len(d_major[key]) >= k:
            answer += 1

    return answer


print(solution(
    ["13123820 BusinessManagement AAA",
     "15047648 Economics AAA",
     "17869244 ComputerScience AAA",
     "19000000 ElectronicEngineering AAA",
     "14281264 Law AAA",
     "19000000 ElectronicEngineering BBB",
     "16188768 BusinessManagement BBB",
     "14634411 Law BBB",
     "16628760 Economics BBB",
     "14863606 BusinessManagement CCC",
     "13165700 Law CCC",
     "13165700 Law CCC",
     "13165700 Law CCC",
     "15215218 ComputerScience CCC"], 4, 3, 3))


# 1월 1일의 요일이 day, 각 월별 k 일의 요일의 주말여부 판단
# day = 6(일요일), k = 1
# return = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
def weekday_flag(day):  # 주말여부 판단
    if day >= 5:
        return 1  # 주말 = 1
    return 0  # 평일 0


def solution(day, k):
    answer = []
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    """
    1 / 6
    2 / (6+1) % 7 = 0
    3 / (6+2) % 7 = 1
    25 / (6+24) % 7 = 2
    """

    for i in range(1, len(days) + 1):
        answer.append(weekday_flag((day + k + sum(days[:i]) - 1) % 7))

    return answer


print(solution(6, 1))
print(solution(6, 25))


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


# 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를
# 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return
def priority_printer_func(priorities, location):
    answer = 0
    m_list = []
    b_loop = True

    for idx, val in enumerate(priorities):
        if idx == location:
            m_list.append([location, val])
        else:
            m_list.append([-1, val])

    while b_loop:
        list_len = len(m_list)
        for i in range(1, list_len):
            # print(m_list, ",", m_list[0][1], m_list[i][1])
            if m_list[0][1] < m_list[i][1]:
                m_list.append(m_list.pop(0))
                break
        else:
            answer += 1
            a, b = m_list.pop(0)
            if a != -1:
                b_loop = False

    return answer


# print(priority_printer_func([2, 1, 3, 2], 2))
# print(priority_printer_func([1, 1, 9, 1, 1, 1], 0))


# 10진법	124나라	10진법	124나라
# 1	    1	    6	    14
# 2	    2	    7	    21
# 3	    4	    8	    22
# 4	    11	    9	    24
# 5	    12	    10	    41
def change124(n):
    # q = deque()
    # x, y = divmod(n, 3)
    #
    # while True:
    #     if y == 1:
    #         q.appendleft('1')
    #     elif y == 2:
    #         q.appendleft('2')
    #     elif y == 0:
    #         q.appendleft('4')
    #
    #     if n < 4:
    #         break
    #
    #     if y == 0:
    #         x -= 1
    #
    #     if x > 3:
    #         x, y = divmod(x, 3)
    #     else:
    #         if x == 1:
    #             q.appendleft('1')
    #         elif x == 2:
    #             q.appendleft('2')
    #         elif x == 3:
    #             q.appendleft('4')
    #         else:
    #             pass
    #         break
    #
    # return ''.join(map(str, q))
    num = ['1', '2', '4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


def notinlist(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

    # used sort
    # answer = ''
    #
    # for p_name, c_name in zip(sorted(participant), sorted(completion)):
    #     # print(p_name, c_name)
    #     if p_name != c_name:
    #         answer += p_name
    #         break
    #
    # if answer == "":
    #     answer += sorted(participant).pop(-1)

    # used hash
    # answer = ''
    # temp = 0
    # dic = {}
    # for part in participant:
    #     dic[hash(part)] = part
    #     temp += int(hash(part))
    #     print(dic, temp)
    #
    # for com in completion:
    #     temp -= hash(com)
    #
    # answer = dic[temp]
    #
    # return answer


# print(notinlist(["leo", "kiki", "eden"], ["eden", "kiki"]))
# print(notinlist(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


def no_continuous_num(arr):
    answer = []

    for i in arr:
        if not answer:
            answer.append(i)
        else:
            if answer[-1] == i:
                pass
            else:
                answer.append(i)

    return answer


# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
def greedy_func(n, lost, reserve):
    # 1
    # cnt_list = [1] * (n + 2)
    # for i in reserve:
    #     cnt_list[i] += 1
    #
    # for i in lost:
    #     cnt_list[i] -= 1
    #
    # print(cnt_list)
    # for idx, i in enumerate(cnt_list):
    #     # print(idx, i)
    #     if i > 1:
    #         if cnt_list[idx - 1] == 0:
    #             cnt_list[idx - 1] += 1
    #             cnt_list[idx] -= 1
    #         elif cnt_list[idx + 1] == 0:
    #             cnt_list[idx + 1] += 1
    #             cnt_list[idx] -= 1
    #
    # print(cnt_list)
    #
    # answer = len([i for i in cnt_list[1:-1] if i > 0])

    # 2
    s = set(lost) & set(reserve)  # 교집합
    l = set(lost) - s  # 잃어버려서 수업참가 불가능한 집합
    r = set(reserve) - s  # 여분이 있는 집합

    for i in sorted(r):
        if i - 1 in l:
            l.remove(i - 1)
        elif i + 1 in l:
            l.remove(i + 1)

    answer = n - len(l)

    return answer


# print(greedy_func(5, [2, 3, 4], [1, 3, 5]))
# print(greedy_func(5, [2, 4], [3]))


# 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
def big_num_combination(numbers):
    answer = ''

    s = [str(x) for x in numbers]
    s.sort(key=lambda x: (x * 4)[:4], reverse=True)
    if s[0] == '0':
        answer = '0'
    else:
        answer = ''.join(s)

    return answer

# print(big_num_combination([6, 10, 2]))
# print(big_num_combination([3, 30, 34, 5, 9]))
