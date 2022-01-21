# 소프트웨어프로젝트1 학기말 프로젝트
## '맘 속의 수 맞추기'게임

+ Game.py
+ game.conf
+ picknumber.py
+ wsgi.py

### 서버 내부 설계 (picknumber.py)
1. 핵심 논리 모듈 개발
2. 메서드의 구현
    def __init__(self) : 비밀숫자, 비밀숫자의 자리수, 시도횟수 모두 0으로 초기화
    def newGame(self,amount) : 시도횟수=0으로 초기화 & 1부터 사용자의 입력값까지를 범위로 하여 랜덤한 수 추출
    def guess(self, userGuess) : 한 번 숫자를 입력해 문제를 풀때마다 시도횟수 +1 & 비밀숫자와 추론한 숫자가 같은지 판단
    def getGuessCount(self) : 지금까지 맞추기를 시도한 횟수 반환
3. 게임 구현 테스트
4. 게임 실행

5. API 구현
6. 게임 드라이버의 구현
7. Apache 서버의 WSGI 설정
8. 서버 테스트
9. 터미널에서 curl 이용해 기본 동작 테스트
10. 게임 클라이언트 개발 - App inventor -> 미완성
