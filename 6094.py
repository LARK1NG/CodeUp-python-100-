# 정보 선생님은 오늘도 이상한 출석을 부른다.

# 영일이는 오늘도 다른 생각을 해보았다.
# 출석 번호를 다 부르지는 않은 것 같은데... 가장 빠른 번호가 뭐였지?

# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

# 단, 
# 첫 번째 번호와 마지막 번호가 몇 번인지는 아무도 모른다.
# 음수(-) 번호, 0번 번호도 있을 수 있다.

n = int(input())
a = map(int, input().split())

b = min(a)
print(b)



n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

min = a[0]
for i in range(0, n) :
  if a[i] < min :
    min = a[i]

print(min)