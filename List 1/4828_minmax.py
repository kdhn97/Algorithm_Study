# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
  N = int(input())
  numbers = list(map(int, input().split()))

  max_number = 0
  min_number = float('inf')

  for n in range(len(numbers)):
    if numbers[n] > max_number:
      max_number = numbers[n]
    if numbers[n] < min_number:
      min_number = numbers[n]

  print(f'#{test_case} {max_number-min_number}')

'''
#1 630739
#2 740510
#3 838110
'''