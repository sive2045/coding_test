"""
신규 아이디 추천
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/72410
"""

def solution(new_id):
    # step 1
    new_id = new_id.lower()
    # step 2
    table = new_id.maketrans({
        '~': '', '!': '', '@': '', '#': '',
        '$': '', '%': '', '^': '', '&': '', 
        '*': '', '(': '', ')': '', '=': '',
        '+': '', '/': '', '?': '', ',': '',
        '<': '', '>': '', ':': '', '[': '',
        ']': '', '}': '', '{': ''
    })
    new_id = new_id.translate(table)
    # step 3
    
    return 0