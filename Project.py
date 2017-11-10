

from graphics import *
win=GraphWin("TicTacToe",700,700)

win.setBackground("gray")
title=Text(Point(350,30), "TIC-TAC-TOE")
title.setSize(30)
title.setFace("helvetica")
title.setStyle("bold italic")
title.draw(win)

def cantplaythere():
    inv=Text(Point(350,350),"You can't play there. Click to try again")
    inv.setSize(20)
    inv.draw(win)
    inv.setTextColor("firebrick")
    inv.setStyle("bold")
    tryagain=win.getMouse()
    if tryagain.x<700:
        inv.undraw()

instr1=Text(Point(350,350), "You go first. Click to start.")
instr1.setSize(20)
instr1.draw(win)

startclick=win.getMouse()
if startclick.x<700:
    instr1.undraw()

vl=Line(Point(250,125),Point(250,575))
vl.draw(win)
vr=Line(Point(450,125),Point(450,575))
vr.draw(win)
ht=Line(Point(100,275),Point(600,275))
ht.draw(win)
hb=Line(Point(100,425),Point(600,425))
hb.draw(win)


for i in range(100):
    play1=win.getMouse()
    if play1.x>100 and play1.x<600 and play1.y>125 and play1.y<575:
        x=Text(play1, ("X"))
        x.setSize(35)
        x.draw(win)
    else:
        cantplaythere()
    
    

##area1=Rectangle((250,275),(0,0))
##area2=Rectangle((250,0),(450,275))
##area3=Rectangle((700,0),(450,275))
##    
##make list of computer options to play
##it can pick one randomly from list
##substract out area that has already been played
##
##options=[area1, area2, area3, area4, area5, area6, area7, area8, area9]
