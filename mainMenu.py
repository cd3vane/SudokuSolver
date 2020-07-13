import pygame
pygame.init()


def main():
    window = pygame.display.set_mode(540, 600)
    pygame.display.set_caption("Sudoku")
    run = True

    while run:
        for event in pygame.event.get():
            if event.type() == pygame.QUIT:
                run = False


main()
pygame.quit()
