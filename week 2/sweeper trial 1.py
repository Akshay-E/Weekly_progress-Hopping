import pygame as p
import random
import time

grid = [[0 for x in range(7)] for y in range(7)]
user_solu=[[0 for x in range(5)]for y in range(5)]
num_mine=0

def initialise():
    global grid
    global num_mine
    while num_mine<5:
        a=random.randint(1,5)
        b=random.randint(1,5)
        grid[a][b]=99
        print('loc: ',a,b)
        num_mine=0   
        for i in range(1,6):
            for j in range(1,6):
                if grid[i][j]==99:
                    num_mine=num_mine+1
    print('mines= ',num_mine)
                
    for i in range(1,6):
        for j in range(1,6):
            if grid[i][j]!=99:
                if grid[i][j+1]==99:
                    grid[i][j]=grid[i][j]+1
                if grid[i][j-1]==99:
                    grid[i][j]=grid[i][j]+1
                if grid[i+1][j]==99:
                    grid[i][j]=grid[i][j]+1
                if grid[i-1][j]==99:
                    grid[i][j]=grid[i][j]+1
                if grid[i+1][j+1]==99:
                    grid[i][j]=grid[i][j]+1
                if grid[i+1][j-1]==99:
                    grid[i][j]=grid[i][j]+1
                if grid[i-1][j+1]==99:
                    grid[i][j]=grid[i][j]+1
                if grid[i-1][j-1]==99:
                    grid[i][j]=grid[i][j]+1
                
   # for i in range(1,6):
    #    for j in range(1,6):
     #       print(grid[i][j])
    for i in range(6):
        grid[0][i]=100
        grid[i][0]=100
        grid[6][i]=100
        grid[i][6]=100
    
    

def reveal(c,r,pos):
    global moves
    
            
    if grid[r][c]==1:
        location=((c-1)*55+150,(r-1)*55+150)
        screen.blit(one,location)
        p.display.flip()
        user_solu[r-1][c-1]=1
        moves=moves+1
    elif grid[r][c]==2:
        location=((c-1)*55+150,(r-1)*55+150)
        screen.blit(two,location)
        p.display.flip()
        user_solu[r-1][c-1]=2
        moves=moves+1
    elif grid[r][c]==3:
        location=((c-1)*55+150,(r-1)*55+150)
        screen.blit(three,location)
        p.display.flip()
        user_solu[r-1][c-1]=3
        moves=moves+1
    elif grid[r][c]==4:
        location=((c-1)*55+150,(r-1)*55+150)
        screen.blit(four,location)
        p.display.flip()
        user_solu[r-1][c-1]=4
        moves=moves+1
    elif grid[r][c]==5:
        location=((c-1)*55+150,(r-1)*55+150)
        screen.blit(five,location)
        p.display.flip()
        user_solu[r-1][c-1]=5
        moves=moves+1
    elif grid[r][c]==0:
        location=((c-1)*55+150,(r-1)*55+150)
        screen.blit(zero,location)
        p.display.flip()
        user_solu[r-1][c-1]=0
        moves=moves+1
    elif grid[r][c]==99:
        location=((c-1)*55+150,(r-1)*55+150)
        screen.blit(boom,location)
        p.display.flip()
        game_over()
    
    print(moves)
    
        
    
def check():
    status=True
    global moves
    if moves==25:
        print('You have exhausted ur moves')
        for i in range(1,6):
            for j in range(1,6):
                if grid[i][j]!=user_solu[i-1][j-1]:
                    status=False
    if status==False:
        game_over()
    else:
        win()
    
    
def win():
    global running
    print('you win the game')
    screen.blit(happy,(0,0))
    p.display.flip()
    time.sleep(2)
    running=False
       
    
def flag(c,r):
    global moves
    if moves==25:
        check()
    else:
        location=((c-1)*55+150,(r-1)*55+150)
        screen.blit(flagm,location)
        p.display.flip()
        user_solu[r-1][c-1]=99
        moves=moves+1
        
    
    
    
def game_over():
    global running
    screen.blit(sad,(0,0))
    p.display.flip()
    for i in range(20):
        if i%2==0:
            screen.fill((255,0,0))
        else:
            screen.fill((255,255,255))
    time.sleep(2)
    running=False
    
    
    

initialise()   
screen=p.display.set_mode((600,600))
screen.fill((255,255,255))
p.display.set_caption('MINE_SWEEPER MODE:EASY')
boom=p.image.load('boom.jpg')
boom=p.transform.scale(boom,(50,50))
one=p.image.load('1.jpg')
one=p.transform.scale(one,(50,50))
two=p.image.load('two.jpg')
two=p.transform.scale(two,(50,50))
three=p.image.load('three.jpg')
three=p.transform.scale(three,(50,50))
four=p.image.load('4.jpg')
four=p.transform.scale(four,(50,50))
five=p.image.load('5.jpg')
five=p.transform.scale(five,(50,50))
five=p.image.load('5.jpg')
five=p.transform.scale(five,(50,50))
zero=p.image.load('0.jpg')
zero=p.transform.scale(zero,(50,50))
flagm=p.image.load('flagg.jpg')
flagm=p.transform.scale(flagm,(50,50))
happy=p.image.load('happy.png')
happy=p.transform.scale(happy,(200,200))
sad=p.image.load('sadd.png')
running=True
moves=0

for i in range(5):
        for j in range(5):
            p.draw.rect(screen,(0,0,0),(55*j+150,55*i+150,50,50))
            p.display.update()


p.display.flip()
while running:
    if moves==25:
        check()
    for event in p.event.get():
        if event.type==p.QUIT:
            running=False
            
        if event.type==p.MOUSEBUTTONDOWN:
            pos=p.mouse.get_pos()
            c=(pos[0]-150)//55+1
            r=(pos[1]-150)//55+1
            #print(pos,r,c)
            if event.button==1:
                reveal(c,r,pos)
                
            elif event.button==3:
                flag(c,r)
                
   
    #screen.fill((255,255,255))
    
    p.display.flip()
    p.time.Clock().tick(60)
    

p.quit()

        

        
        
        
        
        
 