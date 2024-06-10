# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

'''
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
  N, M = map(int, input().split())
  numbers = list(map(int, input().split()))

  result = []
  for i in range(N-M+1):
      answer = 0
      for j in range(i, i+M):
          answer += numbers[j]
      result.append(answer)
  print(f'#{test_case} {max(result) - min(result)}')

'''
#1 21
#2 11088
#3 1090
'''