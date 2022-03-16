"""
신고 결과 받기
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3
"""

def solution(id_list, report, k):
    # user set
    user_data = {}
    for i in range(len(id_list)):
        user_data[id_list[i]] = [0, 0]
    
    # delete duplicated report list
    report_set = set(report)
    duplicated_report = list(report_set)

    # update reported user
    for i in range(len(duplicated_report)):
        report_data = duplicated_report[i].split() # [0] reporter, [1] reported 
        user_data[report_data[1]][0] += 1
    # print(user_data)

    # send mail
    for i in range(len(duplicated_report)):
        report_data = duplicated_report[i].split()
        if user_data[report_data[1]][0] >= k:
            user_data[report_data[0]][1] += 1
    # print(user_data)
    
    answer = []
    for i in range(len(id_list)):
        answer.append(user_data[id_list[i]][1])

    return answer

################################################################################
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
################################################################################

print(solution(id_list, report, k))

"""
Best Solution
"""

def solution_(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
