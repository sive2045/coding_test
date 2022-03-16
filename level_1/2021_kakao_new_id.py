"""
신규 아이디 추천
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/72410
정규표현식 지식이 필요함 : https://buyandpray.tistory.com/49
"""
import re

def solution(new_id):
    # step 1 & 2
    answer = re.sub('[^0-9a-z_.\-]+','',new_id.lower())

    # step 3
    answer = re.sub('\.*\.+','.', answer)
    
    # step 4
    answer = answer.strip('.')

    # step 5
    if answer == '':
        answer = 'a'

    # step 6
    answer = answer[:15].rstrip('.')

    # step 7
    answer += answer[-1] * (3-len(answer))

    return answer

################################################################################
new_id = "...!@BaT#*..y.abcdefghijklm"	
################################################################################

print(solution(new_id))