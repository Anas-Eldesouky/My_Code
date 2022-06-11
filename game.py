from time import sleep
import pygame, random
pygame.init()


screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("FlappyBird")
screen_rect = screen.get_rect()
bg = pygame.image.load("bg.png").convert()
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

def game_over():
	x = 400
	y = 750
	over = pygame.image.load("flappyBirdGameOver.png").convert_alpha()
	over_rect = over.get_rect(topleft=(x,y))

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
	font = pygame.font.Font("flappy-bird-font.ttf", 40)
	scroll = 0
	index = 0
	pipe_scroll = 800
	pipe_scroll_holder = 800
	pipe_scroll2 = 800
	rotate = -15
	top_pipe_rand = 0
	top_pipe_rand2 = 0
	score = 0
	highscore = 0
	finished = False
	while not finished:
		clock.tick(60)
		if top_pipe_rand == 0:
			top_pipe_rand = random.randint(170, 445)
			bottom_pipe_rand = top_pipe_rand - 445
		if top_pipe_rand2 == 0:
			top_pipe_rand2 = random.randint(170, 445)
			bottom_pipe_rand2 = top_pipe_rand2 - 445
		screen.blit(bg, screen_rect)
		pipe_scroll -= 3.5
		pipe_scroll_holder -= 3.5
		collide1 = pipes(pipe_scroll, top_pipe_rand, pipe_scroll, bottom_pipe_rand, scaled, x, y)  
		if pipe_scroll_holder < 400:
			pipe_scroll2 -= 3.5
			collide2 = pipes(pipe_scroll2, top_pipe_rand2, pipe_scroll2, bottom_pipe_rand2, scaled, x, y)
			if collide1 or collide2:
				break
		if pipe_scroll <= -52:
			pipe_scroll = 800
			top_pipe_rand = 0
		if pipe_scroll2 <= -52:
			pipe_scroll2 = 800
			top_pipe_rand2 = 0
		screen.blit(base, (scroll, 490))
		scroll -= 6
		y += 2.5
		if abs(scroll) > 60:
			scroll = 0
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			y += -5.5
			rotate = 10
		if x <= 0:
			x = 0
		elif x >= 766:
			x = 766
		if y <= 0:
			y = 0
		elif y >= 455:
			y = 455
			break
		if pipe_scroll == 19.5:
			score += 1 
		elif pipe_scroll2 == 19.5:
			score += 1
		if score > highscore:
			highscore = score
		# if highscore != 0:
		# 	highscore_text = high_score_font.render(str(highscore), True, white)
		# 	highscore_text_rect = highscore_text.get_rect(center=(400, 75))
		# 	screen.blit(highscore_text, highscore_text_rect)
		score_text = font.render(str(score), True, white)  
		score_text_rect = score_text.get_rect(center=(400, 50))
		screen.blit(score_text, score_text_rect)
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
				finished = True
	return finished

def start_screen():
	screen.blit(bg, (0, 0))
	font = pygame.font.Font("flappy-bird-font.ttf", 100)
	for i in range(3, 0, -1):
		text = font.render(str(i), True, white)
		text_rect = text.get_rect(center=(400, 300))
		screen.blit(text, text_rect)
		pygame.display.flip()
		pygame.time.delay(500)
		screen.blit(bg, (0, 0))
	finished = main()
	emp = True
	while emp:
		if finished != True:
			game_over()
		if finished == True:
			emp = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				emp = False
	pygame.quit()

var = True
while var:
	clock.tick(60)
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
				start_screen()
				# main()
				var = False
	