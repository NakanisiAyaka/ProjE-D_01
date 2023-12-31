import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#練習１
    bg_img2 = pg.image.load("ex01/fig/pg_bg.jpg")#e
    bg_img2 = pg.transform.flip(bg_img2,True,False)
    tmr = 0
    kk_img = pg.image.load("ex01/fig/3.png")#練習２
    kk_img = pg.transform.flip(kk_img,True,False)#練習２
    kk_img = [kk_img,pg.transform.rotozoom(kk_img,1,1.0),pg.transform.rotozoom(kk_img,2,1.0),pg.transform.rotozoom(kk_img,4,1.0),pg.transform.rotozoom(kk_img,6,1.0),pg.transform.rotozoom(kk_img,8,1.0),pg.transform.rotozoom(kk_img,10,1.0),pg.transform.rotozoom(kk_img,8,1.0),pg.transform.rotozoom(kk_img,6,1.0),pg.transform.rotozoom(kk_img,4,1.0),pg.transform.rotozoom(kk_img,2,1.0),pg.transform.rotozoom(kk_img,1,1.0)]#練習３
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%1600
        screen.blit(bg_img, [-x, 0])#練習４
        screen.blit(bg_img2, [1600-x,0])
        screen.blit(kk_img[tmr%12], [300,200]) #練習５
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()