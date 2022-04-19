def game():
    return 6

score=game()
with open('hiscore.txt') as f:
    hiscoreStr = f.read()

if(hiscoreStr==''):
    with open('hiscore.txt','w') as f:
        f.write(str(score))

if int(hiscoreStr)<score:
    with open('hiscore.txt','w') as f:
        f.write(str(score))















# f= open('hiscore.txt')
# a = f.read()
# c=int(a)
# b=game()
# f.close()
# if(b>c):
#    f = open('hiscore.txt','w')
#    f.write(str(b))
#    print("Your new high score")
# else:
#     print("you havent broke the previous high score")

    