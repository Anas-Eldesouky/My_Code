import pygame
pygame.init()


screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("FlappyBird")
screen_rect = screen.get_rect()
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (800, 600))
screen.blit(bg, screen_rect)
clock = pygame.time.Clock()

font = pygame.font.Font("flappy-bird-font.ttf", 32)
text = font.render("9", "1", True, (156, 215, 90))

white = (255, 255, 255)
black = (0, 0, 0)

img = pygame.image.load("logo.png")
img = pygame.transform.scale(img, (350, 100))
screen.blit(img, (225, 105))

play_button = pygame.image.load("playbtn.png")
play_button = pygame.transform.scale(play_button, (200, 100))
play_rect = play_button.get_rect(topleft=(300, 300))
screen.blit(play_button, (300, 300))

def pipes(pipe_x, pipe_y, pipe_top_x, pipe_top_y, image, image_x, image_y):
	pipe = pygame.image.load("pipe.png")
	pipe_top = pygame.transform.flip(pipe, False, True)
	pipe_rect = pipe.get_rect(topleft=(pipe_x, pipe_y))
	pipe_rect_top = pipe_top.get_rect(topleft=(pipe_top_x, pipe_top_y))
	screen.blit(pipe, (pipe_x, pipe_y))
	screen.blit(pipe_top, (pipe_top_x, pipe_top_y))
	if image.get_rect(topleft=(image_x, image_y)).colliderect(pipe_rect) or image.get_rect(topleft=(image_x,image_y)).colliderect(pipe_rect_top):
		collide = True
	else:
		collide = False
	return collide

def main():
	x = 20
	y = 250
	birds = [pygame.image.load("yellowbird-downflap.png"), 
			pygame.image.load("yellowbird-midflap.png"), pygame.image.load("yellowbird-upflap.png")]
	bird = []
	for i in birds:
		scaled = pygame.transform.scale(i, (44, 34))
		bird.append(scaled)
	base = pygame.image.load("base.png")
	base = pygame.transform.scale(base, (860, 112))
	scroll = 0
	index = 0
	pipe_scroll = 800
	pipe_scroll2 = 800
	rotate = -15
	finished = False
	while not finished:
		screen.blit(bg, screen_rect)
		pipe_scroll -= 2
		collide1 = pipes(pipe_scroll, 350, pipe_scroll, -100, scaled, x, y)  
		
		if pipe_scroll < 400:
			pipe_scroll2 -= 2
			collide2 = pipes(pipe_scroll2, 400, pipe_scroll2, -50, scaled, x, y)
			if collide1 or collide2:
				finished = True

		screen.blit(base, (scroll, 490))
		scroll -= 4
		y += 2.5
		if abs(scroll) > 60:
			scroll = 0
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			y += -5
			rotate = 10
		if x <= 0:
			x = 0
		elif x >= 766:
			x = 766
		if y <= 0:
			y = 0
		elif y >= 455:
			y = 455
			finished = True
		
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
	