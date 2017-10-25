import sys
import pygame
from settings  import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	gf.create_fleet(ai_settings, screen, ship, aliens)

	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(aliens, bullets)
		gf.update_aliens(ai_settings, aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

		#删除消失的子弹
		# for bullet in bullets.copy():
		# 	if bullet.rect.bottom <= 0:
		# 		bullets.remove(bullet)
		# print(len(bullets))

		screen.fill(ai_settings.bg_color)
		ship.blitme()
		pygame.display.flip()

run_game()