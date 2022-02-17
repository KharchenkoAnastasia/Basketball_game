import pygame, sys
from cmath import rect
import math
pygame.init()
pygame.display.set_caption('Basketball')
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
my_fon = pygame.image.load("2.png")
screen.blit(my_fon, [0, 0])
pygame.display.flip()
my_gol = pygame.image.load("гол_1.png")
ochku=0
i=0
r_kr=100
x_1=100
konec=0
prirost_kr=1
def result_y_korzina(x_kr):
    return (math.sqrt(math.pow(r_kr,2)-math.pow((x_kr-x_1),2)))

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    def move(self):
        if self.rect.left <= 0 or self.rect.right >= width or \
            self.rect.top <=0 :
            self.rect.center=22,430
            return 1
        else:
            return 0
            
           

class MyKorzinaClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location 

    def move(self):
        global i
        global konec
        if i<=2*r_kr and konec==0:
            y_kr=result_y_korzina(i)
            self.rect.center=250+i,250-y_kr
            i+=prirost_kr
            if i==2*r_kr:
                konec=1
        if i>=0 and konec==1:
            y_kr=result_y_korzina(i)
            self.rect.center=250+i,250+y_kr
            i-=prirost_kr
            if i==0:
                konec=0


def result_y(x,v,a):
    return ((x*math.tan(a))-((9.8*pow(x,2))/(2*pow(v,2)*pow(math.cos(a),2))))


def dalnost_poleta (v,a):
    return ((v*v*math.sin(2*a))/9.8)

class MyStrelkalass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location 


clock=pygame.time.Clock()
v=0
a=0
prirost=12 
l=int(dalnost_poleta(v,a))
x=1


my_ball=MyBallClass("ball.png",[0, 430])
my_ball.rect.center=22,430
my_korzina=MyKorzinaClass("korzina.png",[200,100])
my_korzina.rect.center=250,250
my_strelka_1=MyStrelkalass("strelka.png",[500,500])
my_strelka_1.image=pygame.transform.rotate(pygame.image.load("strelka.png"),10)
my_strelka_2=MyStrelkalass("strelka.png",[500,500])
my_strelka_2.image=pygame.transform.rotate(pygame.image.load("strelka.png"),35)
my_strelka_3=MyStrelkalass("strelka.png",[500,500])
my_strelka_3.image=pygame.transform.rotate(pygame.image.load("strelka.png"),60)
my_strelka_4=MyStrelkalass("strelka.png",[500,500])
my_strelka_4.image=pygame.transform.rotate(pygame.image.load("strelka.png"),90)

def stolknovenie():
    global ochku
    if my_korzina.rect.topleft[0]+5<=my_ball.rect.center[0]<=my_korzina.rect.topright[0]-5 and \
       my_korzina.rect.topleft[1]-40<=my_ball.rect.center[1]<=my_korzina.rect.topleft[1]-20:
        
        for t in range (1,10):
            my_ball.rect.center=my_korzina.rect.midtop[0],my_korzina.rect.midtop[1]+t*10
            screen.blit(my_fon, [0, 0])
            screen.blit(my_ball.image,my_ball.rect)
            screen.blit(my_korzina.image,my_korzina.rect)
            text_orchku=my_font.render(("Очки: "+str(ochku)),1,(0,0,255),(255,255,255))
            screen.blit(text_orchku,(0,0))
            pygame.time.delay(100)
            pygame.display.flip()
        screen.blit(my_fon, [0, 0])
        screen.blit(my_ball.image,my_ball.rect)
        screen.blit(my_korzina.image,my_korzina.rect)
        screen.blit(my_gol, [150, 100])
        text_orchku=my_font.render(("Очки: "+str(ochku)),1,(0,0,255),(255,255,255))
        screen.blit(text_orchku,(0,0))
        pygame.display.flip()
        pygame.time.delay(5000)
        ochku+=prirost_kr+int(my_korzina.rect.center[0]/100)
        my_ball.rect.center=22,430
        return (1)
    elif (my_korzina.rect.topleft[0]-20<=my_ball.rect.center[0]<=my_korzina.rect.topleft[0]+20 and \
       my_korzina.rect.topleft[1]-20<=my_ball.rect.center[1]<=my_korzina.rect.topleft[1]+40) or \
       (my_korzina.rect.topleft[0]<=my_ball.rect.center[0]<=my_korzina.rect.topright[0]  and \
       my_korzina.rect.topleft[1]+20<=my_ball.rect.center[1]<=my_korzina.rect.topleft[1]+40) or\
       my_korzina.rect.topright[0]-20<=my_ball.rect.center[0]<=my_korzina.rect.topright[0]+20 and \
       (my_korzina.rect.topright[1]-20<=my_ball.rect.center[1]<=my_korzina.rect.topright[1]+40):
        my_ball.rect.center=22,430
        return 1
    else:
        return 0

my_font=pygame.font.SysFont("arial",30)
text_orchku=my_font.render(("Очки"+str(ochku)),1,(0,0,255),(255,255,255))

running = True
fell=0
pygame.time.set_timer(pygame.USEREVENT, 1000000)
while running:
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         running = False
     elif event.type==pygame.MOUSEBUTTONUP:
        while x<=l and fell==0:
            clock.tick(5)  
            t=result_y(x,v,a)
            Y=430-int(t)
            X=x+22
            my_ball.rect.center=X,Y
            my_korzina.move()
            screen.blit(my_fon, [0, 0])
            screen.blit(my_korzina.image, my_korzina.rect)
            screen.blit(my_ball.image,my_ball.rect)
            text_orchku=my_font.render(("Очки: "+str(ochku)),1,(0,0,255),(255,255,255))
            screen.blit(text_orchku,(0,0))
            pygame.display.flip()
            fell=stolknovenie()
            fell=my_ball.move()
            x=x+prirost
        if fell==0:
            my_ball.rect.center=l+22,430-int(result_y(l,v,a))
            my_korzina.move()
            screen.blit(my_fon, [0, 0])
            screen.blit(my_korzina.image,my_korzina.rect)
            screen.blit(my_ball.image,my_ball.rect)
            text_orchku=my_font.render(("Очки: "+str(ochku)),1,(0,0,255),(255,255,255))
            screen.blit(text_orchku,(0,0))
            pygame.display.flip()
            my_ball.rect.center=22,430
        fell=0
        x=1


     elif  event.type == pygame.MOUSEMOTION:
         my_korzina.move()
         if (event.pos[0]>22 and event.pos[1]<430):
             ygol=int(math.degrees(math.atan((430-event.pos[1])/(event.pos[0]-22))))
         
         if ygol in range(20,40):
            my_strelka_1.rect.midleft=500,500
            my_strelka_3.rect.midleft=500,500
            my_strelka_2.rect.midleft=0,350
            my_strelka_4.rect.midleft=500,500
            v=90
            a=42
            l=int(dalnost_poleta(v,a))
         elif ygol in range (40,61):
           my_strelka_1.rect.midleft=500,500
           my_strelka_2.rect.midleft=500,500
           my_strelka_3.rect.midleft=-12,320
           my_strelka_4.rect.midleft=500,500
           v=90
           a=61
           l=int(dalnost_poleta(v,a))
         elif ygol in range(61,90): 
             my_strelka_1.rect.midleft=500,500
             my_strelka_3.rect.midleft=500,500
             my_strelka_4.rect.midleft=-16,330
             my_strelka_2.rect.midleft=500,500
             v=90
             a=80
             l=int(dalnost_poleta(v,a))
         elif ygol in range(0,21):
             my_strelka_3.rect.midleft=500,500
             my_strelka_4.rect.midleft=500,500
             my_strelka_2.rect.midleft=500,500
             my_strelka_1.rect.midleft=10,415
             v=90
             a=16
             l=int(dalnost_poleta(v,a))
     elif event.type == pygame.USEREVENT:
         prirost_kr+=1
 clock.tick(5)
 my_korzina.move()  
 screen.blit(my_fon, [0, 0])
 screen.blit(my_strelka_1.image,my_strelka_1.rect)
 screen.blit(my_strelka_2.image,my_strelka_2.rect)
 screen.blit(my_strelka_3.image,my_strelka_3.rect)
 screen.blit(my_strelka_4.image,my_strelka_4.rect)
 screen.blit(my_korzina.image,my_korzina.rect)
 screen.blit(my_ball.image,my_ball.rect)
 text_orchku=my_font.render(("Очки: "+str(ochku)),1,(0,0,255),(255,255,255))
 screen.blit(text_orchku,(0,0))
 pygame.display.flip()  
pygame.quit()

