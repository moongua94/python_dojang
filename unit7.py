# <Unit 7. 출력 방법 알아보기>

##### 7.1 값을 여러 개 출력하기

# print(1, 2, 3)
# print('hello', 'world')

# print(1, 2, 3, sep=', ')
# print(1920, 1080, sep='x')


##### 7.2 줄바꿈 활용하기

# print(1,2,3, sep='\n')
# print('1\n2\n3')

# cf) 제어문자
# \로 시작하는 '이스케이프 시퀀스'. 화면에는 출력되지 않지만 출력 결과를 제어.
# \n, \t 등이 있다. \를 출력하려면 \\으로 해야함.

# print(1); print(2); print(3)		# 줄바꿈이 있는 상태.
# print(1, end=''); print(2, end=''); print(3)		# 기본은 end='\n'.
# print(1, end=' ' ); print(2, end=' '); print(3)


##### 7.4 연습문제

year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year, month, day, sep = '/', end = ' ')	# end를 빼먹었었음.
print(hour, minute, second, sep = ':')


##### 핵심 정리

# 숫자 계산하기
# 계산 결과를 정수, 실수로 만들기
# 괄호 사용하기
# 변수 만들기
# 변수 삭제하기
# 변수 여러 개 만들기
# 산술 연산 후 할당 연산자 사용하기
# 객체의 자료형 알아내기
# 입력 값을 변수에 저장하기
# 한 번에 여러 개 입력받기
# 값을 여러 개 출력하기
# print 함수의 출력 방식 제어하기
# 개행 문자(줄바꿈 문자)
# 산술 연산자


##### Q & A

# 변수 이름 한글 가능?: 가능하지만 영어 써라.
# 숫자를 콤마로 구분해도 됨?: 콤마로 구분하면 튜플 됨. '_'을 써서 가능.
# 변수에 값이 어떻게 저장?: 변수에 저장하는 것이 아니라, 가리키는 것임. 자세한 사항은 사이트 참고.
# 줄바꿈 \n, \r, \r\n 등은 무슨 차이?: \n 써라. 자세한 사항은 사이트 참고.
# 행렬 곱셈 연산자는 어떻게 사용?: 파이썬 3.5부터 사용할 수 있으며 numpy 모듈 설치해야. (pip install numpy)
# 파이썬 셸에서 직전의 결과를 가져올 수 있나?: '_'변수에 결과 저장됨.
