# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

'''
3
5
49679
5
08271
10
7797946543
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
  N = int(input())
  cards = input()

  answer = [0] * 10
  for i in range(len(cards)):
    answer[int(cards[i])] += 1
  
  result = 0
  for j in range(1, len(answer)):
    if answer[result] <= answer[j]:
      result = j
  
  print(f'#{test_case} {result} {max(answer)}')

'''
#1 9 2
#2 8 1
#3 7 3
'''