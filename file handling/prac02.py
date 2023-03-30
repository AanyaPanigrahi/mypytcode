def game():
    return 45
score=game()
with open('samplegame.t','r') as f:
    a=f.read()
if a=='' :
    with open('samplegame.t','w') as f:
        f.write(str(score))
elif int(a)<score:
    with open('samplegame.t','w') as f:
        f.write(str(score))

