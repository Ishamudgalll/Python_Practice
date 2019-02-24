class Obstable(pg.sprite.Sprite):
    def __init__(self, color, width):
            pg.sprite.Sprite.__init__(self)
            self.image = pygame.surface([width, 50])
            self.image.fill(black)
            self.rect = self.image.get_rect()
BLACK = (0,0,0)
obst1 = Obstacle(BLACK, 100)