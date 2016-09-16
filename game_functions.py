
# Standard modules
import sys
import pygame

# Non standard modules
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	""" Respond to keypresses."""
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True

	elif event.key==pygame.K_LEFT:
				ship.moving_left=True

	elif event.key==pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):		
	# Create a new bullet and add it to bullet group.
	# Fire a bullet if limit is not reached
	if len(bullets)<ai_settings.bullets_allowed:
		new_bullet=Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)

def check_keyup_events(event,ship):
	""" Respond to key releases. """

	if event.key==pygame.K_RIGHT:
				ship.moving_right=False

	elif event.key==pygame.K_LEFT:
				ship.moving_left=False


				



def check_events(ai_settings,screen,ship,bullets):
	""" Response to keypresses and mouse events."""
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()

		elif event.type==pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)

			

		elif event.type==pygame.KEYUP:
			check_keyup_events(event,ship)

			
def update_bullets(bullets):
	""" Update position of bullets and get rid of old bullets."""
	# Update bullet position
	bullets.update()

	# Get rid of bullets that has gone out of the screen.
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)

def update_screen(ai_settings,screen,ship,bullets):
	""" Update images on the screen and flip to new screen."""

	screen.fill(ai_settings.bg_color)

	# Redraw all bullets behind ship and tanks.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()