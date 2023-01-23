import pygame
import const
import var
from src.UI.interface_start import START
from src.UI.interface_play import PLAY
from src.UI.interface_death import DEATH
from src.UI.interface_end import END
from src.tool.vector import Vector
"""
The entry of the program
"""


if __name__ == '__main__':
    # pygame initialization
    pygame.init()
    pygame.display.set_caption('Tomb Raider: The Origins')
    # Initialize the screen
    var.screen = pygame.display.set_mode(const.SCREEN_SIZE)
    # Initialize const file, include the music, image and animation
    const.Init()
    # Initialize the START and PLAY interface and set START as the active interface
    var.interface = var.start = START()
    var.play = PLAY()
    var.death = DEATH()
    var.end = END()

    # Use to maintain the FPS
    clock = pygame.time.Clock()

    while not var.quit:
        clock.tick(const.FPS)
        # Update the keyboard and mouse input
        var.key_up.clear()
        var.key_down.clear()
        var.mouse_up.clear()
        var.mouse_down.clear()
        var.mouse = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                var.quit = True
            elif event.type == pygame.KEYUP:
                var.key_up += [event]
            elif event.type == pygame.KEYDOWN:
                var.key_down += [event]
            elif event.type == pygame.MOUSEBUTTONUP:
                var.mouse_up += [event]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                var.mouse_down += [event]
        # Update the interface and draw the image
        var.interface.update()
        var.screen.fill((0, 0, 0))
        var.interface.draw(var.screen)
        # Display the FPS on the top left corner
        var.screen.blit(pygame.font.Font(None, 30).render("FPS: %d" % clock.get_fps(), True, (255, 255, 255)), (20, 10))
        pygame.display.update()
    pygame.quit()
