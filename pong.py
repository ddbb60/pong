import pyxel, random

def flushballe(ballex, balley, x, y, accelleration):
    if x == 0:
        ballex += accelleration
    else:
        ballex -= accelleration
    if y == 0:
        balley += 1
    else:
        balley -= 1
    return ballex, balley

def sens_balle(x, y, scoreleft, scoreright, acceleration):
    accelleration=5
    if ballex > 232 and balley+20 >= duy and balley < duy+50: #right
        x=1
        y=random.randint(0, 1)

    if ballex < 4 and balley+20 >= guy and balley < guy+50: #left
        x=0
        y=random.randint(0, 1)


    if balley +20 >= 256: #down limit
        y=1
        
    if balley == 0: #up limit
        y=0
        
    if ballex+20 > 256: #right limit
        scoreleft += 1
        x=1
        
    if ballex < -1: #left limit
        scoreright +=1
        x=0
     
    return x, y, scoreleft, scoreright, accelleration



def defileraquetteg(guy):
    if pyxel.btn(pyxel.KEY_Z):
        if guy > 0:
            guy -=5
    if pyxel.btn(pyxel.KEY_S):
        if guy < 207:
            guy +=5
    return guy
def defileraquetted(duy):
    if pyxel.btn(pyxel.KEY_P):
        if duy > 0:
            duy -=5
    if pyxel.btn(pyxel.KEY_L):
        if duy < 207:
            duy +=5
    return duy




def update():
    global ballex, balley, guy, duy, x, y, scoreleft, scoreright, accelleration
    ballex, balley = flushballe(ballex, balley, x, y, accelleration)
    guy = defileraquetteg(guy)
    duy = defileraquetted(duy)
    x, y, scoreleft, scoreright, accelleration = sens_balle(x, y, scoreleft, scoreright, accelleration)
def create():
    pyxel.cls(0)
    pyxel.text(110, 2, str(scoreleft), 7)
    pyxel.text(144, 2, str(scoreright), 7)
    #pyxel.text(164, 2, str(accelleration), 7)
    pyxel.rect(0, guy, 4, 50, 7) #init gauche
    pyxel.rect(252, duy, 4, 50, 7) #init droite
    pyxel.rect(128, 0, 1, 256, 4) #net
    pyxel.rect(ballex, balley, 20, 20, 7)
    
pyxel.init(256, 256, title='Pong by Dominique Buccafurri')
scoreleft=0
scoreright=0
accelleration=2
x=0
y=0
ballex=0
balley=100
guy=113
duy=113

pyxel.run(update, create)


