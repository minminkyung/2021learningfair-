import random

score1=0
score2=0
score3=0

def alpha():
    import random
    import time

    print('<알파벳 야구 게임을 해봅시다!>\n')
    print('실패하면 다음 게임으로 넘어갑니다. 30초 안에 입력하지 못하면 처음부터 다시 시작합니다.\n')
    print('a부터 i까지 알파벳 중 제가 생각하고 있는 알파벳 3개를 맞춰보세요.\n')
    
    secretLen =3
    alphabet = ['a','b','c','d','e','f','g','h','i']
    secretList = random.sample(alphabet,secretLen)
    secret = ''
    for i in range(secretLen):
        secret += str(secretList[i])
        

    for chance in range(10,0,-1):
        while True:
            timeStart = time.time()
            guess = input('기회는 %d번 남았어요.\n'%(chance))
            timeend = time.time()
            totaltime = timeend-timeStart
            if totaltime >=30:
                print('30초 안에 입력하지 못했네요. 다시 시작!\n')
                alpha()
            if len(guess) == secretLen and guess.isalpha():
                break

        strike = 0
        ball = 0

        for i in range(secretLen):
            if secret[i] == guess[i]:
                strike +=1
            elif secret[i] in guess:
                ball +=1

        if strike == secretLen:
            print('제가 생각한 알파벳을 모두 맞췄어요!\n')
            global score1
            score1 += 1
            break
        if strike >0:
            if ball > 0:
                print('스트라이크는 %d  볼은 %d이 나왔어요. \n'%(strike,ball))
            else:
                print('스트라이크가 %d이 나왔어요.\n '%(strike))
        else:
            if ball >0:
                print('볼이 %d가 나왔어요.\n'%(ball))
            else:
                print('전부 아웃!\n')
    else:
        print('전부 맞추지 못했어요..')
         


def typing():
    import random
    import time
    print('<타자게임을 해봅시다.10초 안에 주어지는 단어를 입력하세요. 5개의 단어가 무작위로 나옵니다.>\n')

    words=["고양이", "강아지", "여우", "원숭이", "쥐", "곰", "개구리", "뱀", "늑대"]
    number = 1
    print("[타자게임] 시작하려면 엔터")
    startTime = time.time()

    question = random.choice(words)
    while number <=5:
        print("문제", number)
        print(question)
        userinput = input()
        endTime = time.time()
        ElapsedTime = endTime-startTime
        if ElapsedTime >=10:
            print("실패! 시간초과!")
            break
        elif question == userinput:
            print("통과!점수 +1")
            global score2
            score2 = score2 +1
            number = number + 1 
            question = random.choice(words)
        elif question!= userinput:
            print("오타! 다시 도전!")
            question = random.choice(words)
    ElapsedTime = format(ElapsedTime, "2f")
    print("합격 타자시간: {}초\n".format(ElapsedTime))
    
    

def rsp():
    from random import randint

    RSP = {"주먹", "가위", "보"}

    print('<컴퓨터랑 가위바위보 해봅시다.>')

    for i in range(5):
        comRSP = randint(1,3)
        myRSP = int(input("주먹,가위,보 중 내고싶은 것을 숫자로 입력하세요.1.주먹 2.가위 3.보\n"))


        if myRSP == 1:
            if comRSP == 1:
                print("나: 주먹!, 컴퓨터: 주먹!\n")
                print("비겼다!\n")
                global score3
                score3 = score3 +1

            elif comRSP == 2:
                print("나: 주먹!, 컴퓨터: 가위!\n")
                print("이겼다!점수+1\n")
            
            else:
                print("나: 주먹!, 컴퓨: 보!\n")
                print("졌다!\n")



        if myRSP == 2:
            if comRSP == 1:
                print("나: 가위!, 컴퓨터: 주먹!\n")
                print("졌다!!\n")
            elif comRSP == 2:
                print("나: 가위!, 컴퓨터: 보!\n")
                print("이겼다!점수 +1\n")
                score3 = score3 +1
            else:
                print("나:가위!,컴퓨터: 가위!\n")
                print("비겼다!\n")



        if myRSP == 3:
            if comRSP == 1:
                print("나: 보!, 컴퓨터: 주먹!\n")
                print("이겼다!점수 +1\n")
                score3 = score3 +1
            elif comRSP == 2:
                print("나: 보!, 컴퓨터: 가위!\n")
                print("졌다!\n")
            else:
                print("나: 보!, 컴퓨터: 보!\n")
                print("비겼다!\n")


print('랜덤게임 3종을 해봅시다!\n')
print('게임 3개가 무작위 순서로 실행됩니다.\n')
print('게임은 알파벳 3자리 맞추기, 가위바위보, 타자게임 총 3가지가 있습니다.\n')
print('게임을 성공할 때마다  점수가 1점씩 주어집니다.\n')


      
word = ""
while word != "시작":
    word = input('시작을 입력하면 게임이 진행됩니다.: ')
f=random.sample([alpha,typing,rsp],3)
f[0]()
f[1]()
f[2]()

totalscore = score1+score2+score3

print('모든 게임이 끝났습니다.!\n')
print('축하합니다! 총 점수는 %d 점이에요!'%(totalscore)) 



    






