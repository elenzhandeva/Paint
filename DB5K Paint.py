#PAINT SETUP

from pygame import *
from random import *
from math import *
from glob import *

screen = display.set_mode((1200,800))
display.set_caption("Always Keep the Faith")
canvasRect = Rect(200,20,950,650)

canvas = Surface((1200,800),SRCALPHA)   #surface for drawing on
canvas.set_clip(canvasRect)

savesurf = Surface((1200,800),SRCALPHA) #surface that collects all drawn items

bg=image.load("Pics/redseabg3.png")
screen.blit(bg,(0,0))
draw.rect(screen,(255,255,255),canvasRect,1)

font.init()
fontuse=False

###DICTIONARY###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def line(x1,y1,x2,y2):
     if tool=="eraser": col=(255,255,255)         #don't change original c selected
     else: col=c

     r=int(size/2)
     d=((x1-x2)**2+(y1-y2)**2)**0.5
     if d==0: d=1
     
     bx=x2-x1
     lx=bx/d   #horizontal length of small similar triange
     by=y2-y1
     ly=by/d   #vertical one

     for i in range(int(d)):
          draw.circle(canvas,col,(int(x1+lx*i),int(y1+ly*i)),r)  #draws circles along hyp of a line
     draw.circle(canvas,col,(int(x1),int(y1)),r)       #don't miss first & last circles
     draw.circle(canvas,col,(int(x2),int(y2)),r)

def circ(x1,y1,x2,y2):
     connectx=[]
     connecty=[]
     r=((x1-x2)**2+(y1-y2)**2)**0.5
     if r==0: r=1

     sz=size/2

     for thet in range (362):
          ang=radians(thet)   #converts theta in degrees (0-362) to radians
          x=int(r*cos(ang))+x1 #x and y co-ords of points along the circle to connect
          y=int(r*sin(ang))+y1
          connectx.append(x)
          connecty.append(y)
          if len(connectx)>2:
               line(connectx[thet-1],connecty[thet-1],connectx[thet],connecty[thet])

def elip(x1,y1,x2,y2):
     connectx=[]
     connecty=[]
     rx=fabs((x1-x2)/2)  #absolute values of x and y lengths in half to find center of ellipse
     ry=fabs((y1-y2)/2)
     if rx==0: rx=1
     if ry==0: ry=1
     h=x1+((x2-x1)/2)    #shifts ellipse to correct location
     k=y1+((y2-y1)/2)

     sz=size/2

     for thet in range (362):
          ang=radians(thet)
          x=int(rx*cos(ang))+h     #points on the ellipse
          y=int(ry*sin(ang))+k
          connectx.append(x)
          connecty.append(y)
          if len(connectx)>2:
               line(connectx[thet-1],connecty[thet-1],connectx[thet],connecty[thet])

def getName(showPics):
     ans = ""
     arialFont = font.SysFont("Times New Roman", 16)
     back = screen.copy()        # copy screen so we can msclkl it when done
     textArea = Rect(mx,my,200,25) # make changes here.

     if showPics:
        pics = glob("SavedFiles/*.png")
        n = len(pics)
        choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
        draw.rect(screen,(225,255,255),choiceArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),choiceArea,1)        # draw the text window and the text.
        for i in range(n):
            rfiles=pics[i].msclkl("SavedFiles/","")
            txtPic = arialFont.render(rfiles, True, (0,255,0))
            screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))
        
     typing = True
     while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE: 
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN: 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode
          
        mb=mouse.get_pressed()
        if mb[2]==1:
             typing=False
             ans=""
                    
        txtPic = arialFont.render(ans, True, (0,0,0))   ###changes typing font + size
        draw.rect(screen,(225,255,225),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)            
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        
        display.flip()
     screen.blit(back,(0,0))
     return ans

###IMAGES###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     #tools~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
picpencil=image.load("Pics/Tools/pencil.png")
piceraser=image.load("Pics/Tools/eraser.png")
picline=image.load("Pics/Tools/line.png")
piccircle=image.load("Pics/Tools/circle.png")
picbrush=image.load("Pics/Tools/brush.png")
picellipse=image.load("Pics/Tools/ellipse.png")
picspray=image.load("Pics/Tools/spray.png")
picrectangle=image.load("Pics/Tools/rectangle.png")
piccolourdrop=image.load("Pics/Tools/dropper.png")
picbucket=image.load("Pics/Tools/bucketfill.png")
picpoly=image.load("Pics/Tools/polygon.png")
pictext=image.load("Pics/Tools/text.png")
dark=image.load("Pics/GradSqr.png")
     #stamps~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
su = image.load("Pics/Stamps/chil-js.png")
chun = image.load("Pics/Stamps/chil-yc.png")
jae = image.load("Pics/Stamps/chil-jj.png")
minnie = image.load("Pics/Stamps/chil-cm.png")
yun = image.load("Pics/Stamps/chil-yh.png")

junsu = image.load("Pics/Stamps/junsu.png")
yoochun = image.load("Pics/Stamps/yoochun.png")
jaejoong = image.load("Pics/Stamps/jaejoong.png")
changmin = image.load("Pics/Stamps/changmin.png")
yunho = image.load("Pics/Stamps/yunho.png")

OT5 = image.load("Pics/Stamps/OT5.png")
cassie = image.load("Pics/Stamps/cassie.png")
aktf = image.load("Pics/Stamps/aktf.png")
TVXQ = image.load("Pics/Stamps/TVXQ.png")
badge = image.load("Pics/Stamps/badge.png")
     #backgrounds~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bg0 = image.load("Pics/BG/bg0.png")
bg1 = image.load("Pics/BG/bg1.png")
bg2 = image.load("Pics/BG/bg2.png")
bg3 = image.load("Pics/BG/bg3.png")
bg4 = image.load("Pics/BG/bg4.png")
bg5 = image.load("Pics/BG/bg5.png")
bg6 = image.load("Pics/BG/bg6.png")
     #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

toolpics =[picpencil, piceraser, picline,
          piccircle, picbrush, picellipse,
          picspray, picrectangle, piccolourdrop,
          picbucket,picpoly,pictext]

toolnames=["pencil","eraser","line",
           "circle","brush","ellipse",
           "spray","rectangle","colourdrop",
           "bucket","polygon","text"]

tooldims =[Rect(20,250,40,40), Rect(61,250,40,40), Rect(20,291,40,40),
          Rect(61,291,40,40), Rect(20,332,40,40), Rect(61,332,40,40),
          Rect(102,250,40,40), Rect(143,250,40,40), Rect(102,291,40,40),
          Rect(143,291,40,40), Rect(102,332,40,40), Rect(143,332,40,40)]

toolbox = Rect(19,249,165,124)

stamppics=[su, chun, jae, minnie, yun,
           junsu, yoochun, jaejoong, changmin, yunho,
           OT5, cassie, aktf, TVXQ, badge]
stpmini=[]

stampdims=[Rect(25,385,27,45), Rect(57,385,27,45), Rect(90,385,27,45),
          Rect(123,385,27,45), Rect(156,385,27,45),
          Rect(25,435,27,45), Rect(57,435,27,45), Rect(90,435,27,45),
          Rect(123,435,27,45), Rect(156,435,27,45),
          Rect(25,485,27,45), Rect(57,485,27,45), Rect(90,485,27,45),
          Rect(123,485,27,45), Rect(156,485,27,45)]

stampbox=Rect(19,379,170,180)

backgrounds = [bg0,bg1,bg2,bg3,bg4,bg5,bg6]
bgmini = []
bgdims = [Rect(50,685,130,95),Rect(210,685,130,95),Rect(370,685,130,95),Rect(530,685,130,95),
          Rect(690,685,130,95),Rect(850,685,130,95),Rect(1010,685,130,95)]
bgselecbox = Rect(50,670,1020,150)
curbg=()       #current background


tool="pencil"
toolind=0           #index of tool selected from list
toolhov=0           #index of tool hovered over
size = 1
connectx=[]
connecty=[]
undo=[canvas.copy()]      #For last undo
redo=[]
dots=[]

msclkl=False
msclkr=False
msclklu=False
msclkru=False
mslift=False


#colour~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
a=255
c=(0,0,0,a)
collist=[c,c,c,c]
colourbox=Rect(121,196,62,14)
cprev=False
prevcol=(0,0,0)

     #preview/colour history
draw.rect(screen,c,(121,131,62,62),0)
draw.rect(screen,(255,255,255),(120,130,64,64),1)
for col in range (0,4):
     draw.rect(screen,collist[col],(121+col*16,196,15,15),0)
     draw.rect(screen,(255,255,255),(120+col*16,195,16,16),1)

     #alpha slider
slide=150
slider=Rect(6,230,188,10)
pointer=Rect(slide,230,5,10)
draw.rect(screen,(240,200,200),slider,0)
draw.rect(screen,(0,0,0),pointer,0)
myFont = font.SysFont("arial",9)
pt = myFont.render("<=ALPHA CHANNEL=>",1,(0,0,0))
screen.blit(pt,(60,230))


#DRAW DISPLAY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
colour=image.load("Pics/colorwheel.png")
scolour=transform.scale(colour,(100,100))
colourRect = Rect(10,120,100,100)
screen.blit(scolour,colourRect)

for t in range (len(toolnames)):
     screen.blit(toolpics[t],tooldims[t])
screen.blit(dark,tooldims[0])

draw.rect(screen,(0,0,0),toolbox,1)

for st in range(len(stamppics)):
     stampbut=transform.scale(stamppics[st],(27,45))
     stpmini.append(stampbut)
     screen.blit(stampbut,stampdims[st])

for bgp in range(len(backgrounds)):
     bgbut=transform.scale(backgrounds[bgp],(130,95))
     bgmini.append(bgbut)
     screen.blit(bgbut,bgdims[bgp])

##CASSIE STAR-----------------------------------------
#BGM~~~~~~~~
play=image.load("Pics/Tools/starplay.png")
pause=image.load("Pics/Tools/starpause.png")

mixer.init()
mixer.music.load("BGM/standbyu.wav")
mixer.music.set_volume(0.5)
mixer.music.play(-1)     #infinite loop
player=True
bgmbutton = Rect(100,50,28,28)
screen.blit(pause,(92,38))

#Undo/Redo~~
rebut=Rect(50,81,26,26)
unbut=Rect(148,78,26,26)
repic=image.load("Pics/Tools/redo.png")
unpic=image.load("Pics/Tools/undo.png")
screen.blit(repic,rebut)
screen.blit(unpic,unbut)


#Save/Load~~
savebut=Rect(15,19,26,26)
loadbut=Rect(160,14,26,26)
savepic=image.load("Pics/Tools/save.png")
loadpic=image.load("Pics/Tools/load.png")
screen.blit(savepic,savebut)
screen.blit(loadpic,loadbut)



draw.rect(canvas,(255,255,255),canvasRect,0)
screen.blit(canvas,(0,0))
mx,my = 0,0
toolpass=False
undone=False

#######LOOP STARTS############################################
running=True
while running:
 
     for e in event.get():
          if e.type == QUIT:
               running = False
          if e.type==MOUSEBUTTONDOWN:
               if e.button == 1 or e.button == 3:
                    canvas.fill(0)      #empty canvas before copying
                    backcopy = screen.subsurface(canvasRect).copy()
                    oldscreen=screen.copy()
                    start = e.pos
                    if e.button == 1:
                         msclkl=True
                    if e.button == 3:
                         msclkr=True
               if e.button == 4:
                    size += 1
               if e.button == 5 and size>0:
                    size -= 1

          if e.type==MOUSEBUTTONUP:
               savesurf.fill(0)         #empty saved surface (no alpha overlap darkening)
               for step in undo:
                    savesurf.blit(step,(0,0))     #reblit all parts of drawing on
               if e.button == 1:
                    mslift=True
                    msclklu=True
               if e.button == 3:
                    mslift=True
                    msclkru=True

     omx,omy = mx,my
     mx,my = mouse.get_pos()
     mb = mouse.get_pressed()
     


     #MUSIC PLAYER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     if bgmbutton.collidepoint(mx,my) and msclkl==True:
          if player==True:
               player=False
               mixer.music.pause()
               screen.blit(play,(92,38))
               
          elif player==False:
               player=True
               mixer.music.unpause()
               screen.blit(pause,(92,38))
               
     #SAVE/LOAD~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     if savebut.collidepoint(mx,my) and msclkl==True:
          savename = getName(True)
          if savename!="":
               image.save(savesurf, savename+".png")

     if loadbut.collidepoint(mx,my) and msclkl==True:
          loadname = getName(True)
          if loadname!="":
               loadpic=image.load(loadname)
               if a!=255:
                    loadpic.set_alpha(a)
               canvas.blit(loadpic,(0,0))
               screen.blit(canvas,(0,0))

          #UNDO/REDO for loading pics
               if undone==True and len(redo)>0:
                    undo.append(redo[-1])
                    redo=[]
                    undone=False
               undo.append(canvas.copy())
          #~~~~~~~~~~
     
#COLOUR SELECTION~~~~~~~~~~~~~~~~~~~~~~~~~~
          #selecting colour by colourwheel, recent colours box, or colourdrop tool
     if colourRect.collidepoint(mx,my) and ((mx-60)**2+(my-170)**2)**0.5<50 or colourbox.collidepoint(mx,my) or canvasRect.collidepoint(mx,my) and tool=="colourdrop":
          if mb[0]==1:                  #allows user to preview colour without selecting it as long as left mouse held down
               prevcol=screen.get_at((mx,my))
               draw.rect(screen,prevcol,(121,131,62,62),0)
          if msclklu==True:             #selects colour only when left mouse lifted
               collist.append(c)        #add current colour to history and remove oldest colour from list
               collist=collist[-4:]
               c=screen.get_at((mx,my))
               c=(c[0],c[1],c[2],a)     #add alpha value from slider
               draw.rect(screen,c,(121,131,62,62),0)
               for col in range (0,4):
                    draw.rect(screen,collist[-(col+1)],(121+col*16,196,14,14),0)

          #alpha value slider---------------
     if slider.collidepoint(mx,my) or pointer.collidepoint(mx,my):
          if mb[0]==1:
               if mx<6: smx=6
               elif mx>189:smx=189
               else:smx=mx
               pointer=Rect(smx,230,5,10)
               draw.rect(screen,(240,200,200),slider,0)
               draw.rect(screen,(0,0,0),pointer,0)
               screen.blit(pt,(60,230))
               a=int(1.4*(smx-6))       #convert placement of pointer to and alpha int value
               if a>255: a=255
               c=(c[0],c[1],c[2],a)     #add alpha value to colour


#TOOL SELECTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     if toolbox.collidepoint(mx,my):
          for t in range (len(toolnames)):
               if tooldims[t].collidepoint(mx,my) or tool==toolnames[t]:
                    screen.blit(toolpics[t],tooldims[t])
                    screen.blit(dark,tooldims[t])
                    if msclkl==True:    #set tool if clicked
                         toolind=t
                         tool=toolnames[t]
                    else:          #else only temp darken pic
                         toolhov=t
               else:     #get rid of hover pic (darkened)
                    screen.blit(toolpics[t],tooldims[t])
          toolpass=True

     elif toolpass==True:          #make sure only one pic is darkened
          if toolhov!=toolind:
               screen.blit(toolpics[toolhov],tooldims[toolhov])
          toolpass=False

     if stampbox.collidepoint(mx,my):
          for st in range(len(stamppics)):
               if stampdims[st].collidepoint(mx,my) and mb[0]==1 or tool=="stamp" and sticker==stamppics[st]:
                    draw.rect(screen,(0,255,0),stampdims[st],1)
                    tool="stamp"
                    sticker=stamppics[st]
                    swid,shei=sticker.get_size()  #get dimensions of stamp for scaling
               else:
                    draw.rect(screen,(0,0,0),stampdims[st],1)
                    screen.blit(stpmini[st],stampdims[st])

     if bgselecbox.collidepoint(mx,my):
          for bkpic in range(len(backgrounds)):
               if bgdims[bkpic].collidepoint(mx,my) and msclkl==True:
                    screen.blit(backgrounds[bkpic],canvasRect)
                    canvas.blit(savesurf,(0,0))
                    screen.blit(canvas,(0,0))
                    draw.rect(screen,(0,255,0),bgdims[bkpic],1)
                    curbg=backgrounds[bkpic]
               else:
                    screen.blit(bgmini[bkpic],bgdims[bkpic])

     #MOUSE POS----
     if canvasRect.collidepoint(mx,my):
          pos=myFont.render("x, y: "+str(mx-200)+", "+str(my-5),1,(255,255,255))
          draw.rect(screen,(0,0,0),(10,780,70,20),0)
          screen.blit(pos,(10,785))
     else:
          pos=myFont.render("x, y: -, -",1,(255,255,255))
          draw.rect(screen,(0,0,0),(10,780,70,20),0)
          screen.blit(pos,(10,785))          

#DRAWING===========================================================================
     if canvasRect.collidepoint(mx,my):          
          screen.set_clip(canvasRect)
          if tool=="line":
               if mb[0]==1 or mb[2]==1:
                    canvas.fill(0)      #clears canvas while drawing (no tracing)
                    line(start[0],start[1],mx,my)
                    screen.blit(backcopy,canvasRect)   #blit original stuff
                    screen.blit(canvas,(0,0))          #blit new stuff

          if tool=="eraser" and mb[0]==1:
               if mb[0]==1:
                    connectx.append(mx)
                    connecty.append(my)
                    if len(connectx)>1:
                         line(connectx[-1],connecty[-1],connectx[-2],connecty[-2])
               if mb[0]==0:
                    connectx=[]
                    connecty=[]

          if tool=="circle":
                    if mb[0]==1:        #draw unfilled circle
                         canvas.fill(0)
                         circ(start[0], start[1], mx, my)
                         screen.blit(backcopy,canvasRect)
                         screen.blit(canvas,(0,0))
                    elif mb[2]==1:      #draw filled circle
                         rad=((start[0]-mx)**2+(start[1]-my)**2)**0.5
                         canvas.fill(0)
                         draw.circle(canvas,c,start,int(rad),0)
                         screen.blit(backcopy,canvasRect)
                         screen.blit(canvas,(0,0))
                    if mb[0]==0 and mb[2]==0:
                         connectx=[]
                         connecty=[]


          if tool=="rectangle":
               if mb[0]==1:             #draw unfilled rect
                    canvas.fill(0)
                    sz=size//2
                    xcor=[start[0],mx]            #faster to determing min/max for co-ords of rect
                    ycor=[start[1],my]
                    wid=size
                    if wid<1: wid=1
                    dx=int(((mx-start[0])**2)**0.5)    #distance between x values
                    dy=int(((my-start[1])**2)**0.5)    #distance between y values
                    for w in range(wid):               #draws thicker rects outwards
                         draw.rect(canvas,c,(min(xcor)-w,min(ycor)-w,dx+2*w,dy+2*w),1)
                    screen.blit(backcopy,canvasRect)
                    screen.blit(canvas,(0,0))

               if mb[2]==1:             #draw filled rect
                    canvas.fill(0)
                    if start[0]>=mx:
                         x=mx
                    elif mx>start[0]:
                         x=start[0]
                    if start[1]>=my:
                         y=my
                    elif my>start[1]:
                         y=start[1]
                    dx=int(((mx-start[0])**2)**0.5)
                    dy=int(((my-start[1])**2)**0.5)
                    draw.rect(canvas,c,(x,y,dx,dy))
                    screen.blit(backcopy,canvasRect)
                    screen.blit(canvas,(0,0))
                    
          if tool=="ellipse":
               if (mx,my)!=(start[0],start[1]):   #draw only if mouse moves
                    if mb[0]==1:        #draw unfilled ellipse
                         if size>1:
                              canvas.fill(0)
                              elip(start[0],start[1],mx,my)
                              screen.blit(backcopy,canvasRect)
                              screen.blit(canvas,(0,0))
                         else:     #my ellipse has more holes when width is 1
                              xcor=[start[0],mx]
                              ycor=[start[1],my]
                              dx=int(((mx-start[0])**2)**0.5)
                              dy=int(((my-start[1])**2)**0.5)
                              if dx>1 and dy>1:
                                   canvas.fill(0)
                                   draw.ellipse(canvas,c,(min(xcor),min(ycor),dx,dy),1)
                                   screen.blit(backcopy,canvasRect)
                                   screen.blit(canvas,(0,0))

                    if mb[2]==1:          #draw filled ellipse
                         screen.blit(backcopy,canvasRect)
                         if start[0]>=mx:
                              x=mx
                         elif mx>start[0]:
                              x=start[0]
                         if start[1]>=my:
                              y=my
                         elif my>start[1]:
                              y=start[1]
                         dx=int(fabs(mx-start[0]))
                         dy=int(fabs(my-start[1]))
                         canvas.fill(0)
                         draw.ellipse(canvas,c,(x,y,dx,dy))
                         screen.blit(backcopy,canvasRect)
                         screen.blit(canvas,(0,0))
                    
                    
          if tool=="pencil":
               if mb[0]==1:
                    if mx<200:mx=200
                    if my<20:my=20
                    dots.append((mx,my))
                    if len(dots)>2:
                         draw.lines(canvas,c,False,dots,1)
                         screen.blit(backcopy,canvasRect)
                         screen.blit(canvas,(0,0))
               if mb[0]==0:
                    dots=[]


          if tool=="brush":
               if mb[0]==1:
                    connectx.append(mx)
                    connecty.append(my)
                    if len(connectx)>1:
                         line(connectx[-1],connecty[-1],connectx[-2],connecty[-2])
                         screen.blit(backcopy,canvasRect)
                         screen.blit(canvas,(0,0))
               if mb[0]==0:
                    connectx=[]
                    connecty=[]

          if tool=="spray" and mb[0]==1:          
               sz=size*3           #diameter of the circle area
               s=int(sz/2)         #approx rad of circle area
               pts=randint(s,sz+s) # num of dots in the circle area
               
               for i in range(pts):
                    x1=randint(-sz,sz)  #random co-or within the size range
                    y1=randint(-sz,sz)
                    if (x1**2+y1**2)**0.5<sz:     #make sure dot is in a circular area around mx,my
                         draw.circle(canvas,c,(mx+x1,my+y1),randint(0,1))
                         screen.blit(backcopy,canvasRect)
                         screen.blit(canvas,(0,0))

          if tool=="bucket" and msclkl==True:
               oc=screen.get_at((mx,my)) #original colour at click
               if oc!=c:
                    spots=[(mx,my)]     #list of spots to be checked
                    while len(spots)>0:
                         durl=[(0,1),(0,-1),(1,0),(-1,0)] #check down, up, right, left
                         for sp in durl:
                              ching=(spots[0][0]+sp[0],spots[0][1]+sp[1]) #pixel being checked
                               #as long as spot is correct colour, not already in list to be checked and is not out of canvas boundaries
                              if screen.get_at((ching))==oc and ching not in spots and 199<ching[0]>1151 and 19<ching[1]<671:
                                   spots.append(ching)
                                   screen.set_at(ching,c)   #blit new colour onto canvas
                         del spots[0]

          if tool=="polygon":
               if dots!=[]:
                    canvas.fill(0)
                    if msclkl==True:         #drawing to dots (not first/last)
                         line(dots[0],dots[1],mx,my)                        
                         dots=[omx,omy]
                    elif msclkr==True:       #reconnecting to first dot
                         line(dot1[0],dot1[1],mx,my)                       
                         dots=[]
                    else:                    #drawing line from last dot to mouse
                         line(dots[0],dots[1],mx,my)                        
                    screen.blit(backcopy,canvasRect)
                    screen.blit(canvas,(0,0))
                    
               elif dots==[] and msclkl==True:    #first dot (one to reconnect to)
                    dot1=[mx,my]
                    dots=[mx,my]


          if tool=="text" and mb[0]==1:
               txt = getName(False)
               comicFont = font.SysFont("Comic Sans MS", 10+size*2)  ###change font of blit
               txtPic = comicFont.render(txt, True, c) ###this c changes colour
               canvas.blit(txtPic,(mx,my)) ###changes where text is blit
               screen.blit(backcopy,canvasRect)
               screen.blit(canvas,(0,0))
               
               fontuse=True

               #UNDO/REDO for text
               if undone==True and len(redo)>0:
                    undo.append(redo[-1])
                    redo=[]
                    undone=False
               undo.append(canvas.copy())
               #~~~~~~~~~~

          if tool=="stamp":
               if mb[0]==1 or mb[2]==1:
                    canvas.fill(0)
                    sz=size/3
                    if size<1: sz=1
                    sticker=transform.scale(sticker,(int(swid*sz),int(shei*sz)))     #scaling image size (scrolling)
                    if mb[2]==1:
                         sticker=transform.flip(sticker,1,0)          #right click to flip stamp horizontally
                    if a!=255: sticker.set_alpha(a) 
                    stickx=(swid*sz)/2       #to get top right corner
                    sticky=(shei*sz)/2
                    canvas.blit(sticker, (mx-int(stickx),my-int(sticky)))
                    screen.blit(backcopy,canvasRect)
                    screen.blit(canvas,(0,0))
                    
          screen.set_clip(None)

###Undo/Redo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     if mslift==True and canvasRect.collidepoint(mx,my):
          undo.append(canvas.copy())    #copy canvas when mouse lifted (after all drawing is done)

     if msclkl==True:
          if unbut.collidepoint(mx,my) and len(undo)>0:
               screen.blit(oldscreen,(0,0))
               screen.blit(curbg,canvasRect) #blit on current background
               for step in undo:             #layer on all drawing to canvas
                    canvas.blit(step,(0,0))
               screen.blit(canvas,(0,0))     #blit canvas to screen
               redo.append(undo[-1])         #remove last surface and add to redo list
               del undo[-1]
               undone=True                   ### middle of the list
          if rebut.collidepoint(mx,my) and len(redo)>0:
               screen.blit(curbg,canvasRect)
               for step in undo:
                    canvas.blit(step,(0,0))
               canvas.blit(redo[-1],(0,0))
               screen.blit(canvas,(0,0))
               undo.append(redo[-1])
               del redo[-1]
                         
     if undone==True and canvasRect.collidepoint(mx,my) and len(redo)>0:
          if mb[0]==1 or mb[2]==1:           # check undo/redo flag so if starts drawing again, del redo list
               undo.append(redo[-1])
               redo=[]
               undone=False
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     cprev=False
     msclkl=False
     msclkr=False
     msclklu=False
     msclkru=False
     mslift=False

     display.flip()
font.quit()
if fontuse==True:
     del comicFont

quit()
