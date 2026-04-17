import random
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
caption = pygame.display.set_caption('Бем бем бем')

r_size, r_coordinate = (160, 160), (220, 440)

run = True

reset = pygame.image.load('C:/Users/Admin/Desktop/sprites/R.png')
cards = {
    'common': (pygame.image.load('C:/Users/Admin/Desktop/sprites/Common.png'), 0.5),
    'rare': (pygame.image.load('C:/Users/Admin/Desktop/sprites/Rare.png'), 0.3),
    'epic': (pygame.image.load('C:/Users/Admin/Desktop/sprites/Epic.png'), 0.1),
    'mythic': (pygame.image.load('C:/Users/Admin/Desktop/sprites/Mythic.png'), 0.067),
    'legendary': (pygame.image.load('C:/Users/Admin/Desktop/sprites/Legendary.png'), 0.033)
}

images = [v[0] for v in cards.values()]
weights = [v[1] for v in cards.values()]
scroll = False
random_cards = random.choices(images, weights=weights, k=random.randint(200, 1500))
start = pygame.time.get_ticks()
end = (pygame.time.get_ticks() - start)
seconds = random.randint(5, 10)

xx = 0

def falling():
    if start - end < 50 and start - end > -50:
        screen.blit(random_cards[0], (0, 0))

def render():
    global xx
    screen.blit(pygame.transform.scale(reset, r_size), r_coordinate)
    for i in range(len(random_cards)):
        if i*100+xx > -90 and i*100+xx < 600:
            screen.blit(pygame.transform.scale(random_cards[i], (90, 128)), (i*100+xx, 100))

def events():
    global run, reset, xx, scroll, start, seconds, end
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and x < r_coordinate[0] + r_size[0] and x > r_coordinate[0] and \
                y < r_coordinate[1] + r_size[1] and y > r_coordinate[1]:
            reset = pygame.image.load('C:/Users/Admin/Desktop/sprites/R hold.png')
            scroll = True
        else:
            if x < r_coordinate[0] + r_size[0] and x > r_coordinate[0] and y < r_coordinate[1] + r_size[1] and y > \
                r_coordinate[1]:
                reset = pygame.image.load('C:/Users/Admin/Desktop/sprites/R dir.png')
            else:
                reset = pygame.image.load('C:/Users/Admin/Desktop/sprites/R.png')
    if scroll:
        xx -= 10
        if end // 1000 >= seconds:
            seconds = random.randint(5, 10)
            start = end
            scroll = False
        end = pygame.time.get_ticks()
        return end
    return seconds



white = (255, 255, 255)
black = (0, 0, 0)

while run:
    x, y = pygame.mouse.get_pos()
    screen.fill(white)
    events()
    falling()
    print(start, end)
    render()
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()