# 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
# 3의 배수인 경우는 출력하지 않도록 만들어보자.

# 예를 들면,
# 1 2 4 5 7 8 10 11 13 14 ...
# 와 같이 출력하는 것이다.

a = int(input())

for i in range(1, a + 1):
    if i % 3 != 0:
        print(i, end=' ')



n=int(input())

for i in range(1, n+1) : 
  if i%3==0 : 
    continue            #다음 반복 단계로 넘어간다.
  print(i, end=' ')    #i가 짝수가 아닐 때만 실행된다.