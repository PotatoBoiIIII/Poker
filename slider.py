import pygame




class Slider:
    def __init__(self, length, from_, to, x, y ):
        self.slide = pygame.Rect(x, y, 5, length)
        self.knob = pygame.Rect(x-2, y, 10, 5)
        self.length=length
        self.from_=from_
        self.to=to

    def draw(self, screen, font):

        pygame.draw.rect(screen, (0,0,255), self.slide)
        pygame.draw.rect(screen, (255,0,0), self.knob)
        pos = pygame.mouse.get_pos()



        if pygame.mouse.get_pressed()[0] == 1 and pos[1]>=self.slide.y and pos[1]<self.slide.y+self.slide.height and pos[0]>self.slide.x-20 and pos[0]<self.slide.x+25:
            self.knob.y=pos[1]
        elif pygame.mouse.get_pressed()[0]==1 and pos[1]>self.slide.y-20 and pos[1]<self.slide.y and pos[0]>self.slide.x-20 and pos[0]<self.slide.x+25:
            self.knob.y=self.slide.y
        elif pygame.mouse.get_pressed()[0]==1 and pos[1]<self.slide.y+self.slide.height+20 and pos[1]>self.slide.y+self.slide.height and pos[0]>self.slide.x-20 and pos[0]<self.slide.x+25:
            self.knob.y=self.slide.y+self.slide.height
        value = int((self.knob.y - self.slide.y) / self.slide.height * (self.to - self.from_))+self.from_
        number_text = font.render("$" + str(value), 1, (255, 255, 255))
        screen.blit(number_text, (self.slide.x - 30, self.slide.y + self.slide.height / 2))
        return value





