import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien


def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Set the background color.
    #bg_color = (230, 230, 230)

    # Make an alien.
    alien = Alien(ai_settings, screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, alien, bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
        # Watch for keyboard and mouse events.
        #  ffoghu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


run_game()
