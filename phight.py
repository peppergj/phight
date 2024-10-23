import pygame

pygame.init()

with open ("level.txt", "r") as data:
    lines = [x.strip("\n") for x in data.readlines()]

for line in lines: 
    numbers =  line.split(" ")
    array = []
    for numb in numbers:
        n = int(numb)
        print(n + 1)
        array.append(n)
    print(array)
    
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Phight')

pygame.draw.line(screen, (250, 0, 0), (960, 540 ), (200, 200), 10)
pygame.display.update()

pygame.draw.line(screen, (0, 0, 250), (500, 400), (1000, 0), 10)
pygame.display.update()

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()