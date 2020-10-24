import pygame, random

pygame.init()

rows = 50
xy = 500
d = False

while True:
    d = input('Random points? (Y or N) ')
    if d.lower() == 'y':
        d = True
        break
    elif d.lower() == 'n':
        d = False
        break
    else:
        continue

if not d:
    c = [(input('Your x1(0-50) value here: '), input('Your y1(0-50) value here: ')),
        (input('Your x2(0-50) value here: '), input('Your y2(0-50) value here: '))]
elif d:
    c = [(random.randrange(0, 50), random.randrange(0, 50)), (random.randrange(0, 50), random.randrange(0, 50))]

win = pygame.display.set_mode((xy, xy))
pygame.display.set_caption("Coords")
clock = pygame.time.Clock()


def redrawWin():
    win.fill((255, 255, 255))
    drawGrid(win, rows, xy)
    drawLine()
    pygame.display.update()


def calculator(coords):
    yy = int(coords[1][1]) - int(coords[0][1])
    xx = int(coords[1][0]) - int(coords[0][0])
    m = yy / xx
    return m


def getYpoint():
    m = calculator(c)
    b = (int(c[0][1]) * 10) - (int(c[0][0]) * m) * 10
    return b / 10


def drawGrid(win, rows, xy):
    spaceBtwn = xy // rows
    x = 0
    y = 0

    for l in range(rows):
        x = x + spaceBtwn
        y = y + spaceBtwn

        pygame.draw.aaline(win, (220, 220, 220), (x, 0), (x, xy))
        pygame.draw.aaline(win, (220, 220, 220), (0, y), (xy, y))
        pygame.draw.aaline(win, (0, 0, 0), (0, 0), (0, xy))


def drawLine():
    global c
    startx = (int(c[0][0]) * 10) + 10000
    starty = (int(c[0][1]) * 10) + calculator(c) * 10000
    endx = (int(c[0][0]) * 10) - 10000
    endy = (int(c[0][1]) * 10) - calculator(c) * 10000
    pygame.draw.aaline(win, (0, 0, 255), (startx, xy - starty), (endx, xy - endy))


def main():
    global c
    run = True
    while run:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            redrawWin()


print('The Formula F(x) = m*x + b is: ' + str(calculator(c)) + 'x + ' + str(getYpoint()))
main()
