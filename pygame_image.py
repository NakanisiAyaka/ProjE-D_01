import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#1
    tmr = 0
    kk_img = pg.image.load("ex01/fig/3.png")#2gazou
    kk_img = pg.transform.flip(kk_img,True,False)#2hanten
    kk_img = [kk_img,pg.transform.rotozoom(kk_img,10,1.0)]#3
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])#4
        screen.blit(kk_img[1], [300,200]) 
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()