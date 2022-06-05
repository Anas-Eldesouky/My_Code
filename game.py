import pygame
pygame.init()


screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("FlappyBird")
screen_rect = screen.get_rect()
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (800, 600))
screen.blit(bg, screen_rect)
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

img = pygame.image.load("logo.png")
img = pygame.transform.scale(img, (350, 100))
screen.blit(img, (225, 105))

play_button = pygame.image.load("playbtn.png")
play_button = pygame.transform.scale(play_button, (200, 100))
play_rect = play_button.get_rect(topleft=(300, 300))
screen.blit(play_button, (300, 300))


def main():
	x = 20
	y = 250
	bird = [pygame.image.load("yellowbird-downflap.png"), 
			pygame.image.load("yellowbird-midflap.png"), pygame.image.load("yellowbird-upflap.png")]
	base = pygame.image.load("base.png")
	base = pygame.transform.scale(base, (860, 112))
	scroll = 0
	index = 0
	rotate = -15
	finished = False
	while not finished:
		screen.blit(bg, screen_rect)
		screen.blit(base, (scroll, 490))
		scroll -= 4
		y += 2
		if abs(scroll) > 60:
			scroll = 0
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			y += -10
			rotate = 10
		if x <= 0:
			x = 0
		elif x >= 766:
			x = 766
		if y <= 0:
			y = 0
		elif y >= 464:
			y = 464
		
		if index >= len(bird):
			index = 0
		image = bird[int(index)]
		image = pygame.transform.rotate(image, rotate)
		screen.blit(image, (x,y))
		if rotate == 10:
			rotate = -15
		index += 0.12
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				finished = True


var = True
while var:
	clock.tick(30)
	pygame.display.update()
	mouse = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				var = False
		if event.type == pygame.QUIT:
			pygame.quit()
			var = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if play_rect.collidepoint(mouse):
				main()
				var = False
	