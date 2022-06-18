import pygame, random, json

# initialize pygame library
pygame.init()

# genereates the screen
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("FlappyBird")
screen_rect = screen.get_rect()
bg = pygame.image.load("assets/bg.png").convert()
bg = pygame.transform.scale(bg, (800, 600))
screen.blit(bg, screen_rect)
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

# flappybird logo
img = pygame.image.load("assets/logo.png")
img = pygame.transform.scale(img, (350, 100))
screen.blit(img, (225, 105))

# creates play button
play_button = pygame.image.load("assets/playbtn.png")
play_button = pygame.transform.scale(play_button, (200, 100))
play_rect = play_button.get_rect(topleft=(300, 300))
screen.blit(play_button, (300, 300))


def pipes(pipe_x, pipe_y, pipe_top_x, pipe_top_y, image, image_x, image_y):
	'''(float, int, float, int, Surface, list, list) -> bool
	creates pipes and checks for collision
	'''
	pipe = pygame.image.load("assets/pipe.png")
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


	

def main(diff, highscore):
	'''(list, int) -> bool, int, int
	mainframe code
	'''
	x = 20
	y = 250
	
	# loads bird images
	birds = [pygame.image.load("assets/yellowbird-downflap.png"), 
			pygame.image.load("assets/yellowbird-midflap.png"), pygame.image.load("assets/yellowbird-upflap.png")]
	bird = []
	for i in birds:
		scaled = pygame.transform.scale(i, (44, 34))
		bird.append(scaled)
	
	# loads base image and font
	base = pygame.image.load("assets/base.png")
	base = pygame.transform.scale(base, (860, 112))
	font = pygame.font.Font("assets/flappy-bird-font.ttf", 40)

	# initiating variables 
	scroll = 0
	index = 0
	pipe_scroll = 800
	pipe_scroll_holder = 800
	pipe_scroll2 = 800
	rotate = -15
	top_pipe_rand = 0
	top_pipe_rand2 = 0
	score = 0
	finished = False

	# main game loop
	while not finished:
		# sets fps
		clock.tick(60)

		# randomize pipe location
		if top_pipe_rand == 0:
			top_pipe_rand = random.randint(170, diff)
			bottom_pipe_rand = top_pipe_rand - diff
		if top_pipe_rand2 == 0:
			top_pipe_rand2 = random.randint(170, diff)
			bottom_pipe_rand2 = top_pipe_rand2 - diff

		# generates background
		screen.blit(bg, screen_rect)

		# scrolls pipes
		pipe_scroll -= 3.5
		pipe_scroll_holder -= 3.5

		# generates pipes and checks for collision
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
		
		# generates moving base
		screen.blit(base, (scroll, 490))
		scroll -= 6
		if abs(scroll) > 60:
			scroll = 0

		# constantly decends bird
		y += 2.5
		
		# checks user input and moves bird correspondingly
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

		# adds score
		if pipe_scroll == 19.5:
			score += 1 
		elif pipe_scroll2 == 19.5:
			score += 1
		
		# checks for new highscore
		if score > highscore:
			highscore = score
		
		# prints score onto screen
		score_text = font.render(str(score), True, white)  
		score_text_rect = score_text.get_rect(center=(400, 50))
		screen.blit(score_text, score_text_rect)

		# bird animation
		if index >= len(bird):
			index = 0
		image = bird[int(index)]
		image = pygame.transform.rotate(image, rotate)
		screen.blit(image, (x,y))
		if rotate == 10:
			rotate = -15
		index += 0.12

		# updates screen and checks for quitting
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finished = True
	return finished, score, highscore

def game_over(score, highscore):
	'''(int, int) -> Rect
	game over screen
	'''
	x = 225
	y = 105

	# loads fonts
	font = pygame.font.Font("assets/FlappyBird.ttf", 65)
	high_font = pygame.font.Font("assets/flappy-bird-font.ttf", 40)

	# loads game over image, sets rectangular border and prints game over
	over = pygame.image.load("assets/flappyBirdGameOver.png").convert_alpha()
	over = pygame.transform.scale(over, (350, 100))
	over_rect = over.get_rect(topleft=(x,y))
	back_rect = pygame.Rect(100, 100, 590, 350)
	back_border_rect = pygame.Rect(100, 100, 595, 355)
	back_border = pygame.draw.rect(screen, (87, 60, 75), back_border_rect, 0, 6)
	back = pygame.draw.rect(screen, (220,220,146), back_rect, 0, 6)
	screen.blit(over, over_rect)

	# prints score and score text
	score_text = high_font.render(f"{score}", True, (251,163,70))
	score_title = font.render(F"Score: ", True, (251,163,70))
	screen.blit(score_title, pygame.Rect(150, 250, 600, 600))
	screen.blit(score_text, pygame.Rect(400, 250, 600, 600))

	# prints highscore and highscore text
	high_text = high_font.render(f"{highscore}", True, (251,163,70))
	high_score_title = font.render(f"Highscore: ", True, (251,163,70))
	screen.blit(high_score_title, pygame.Rect(150, 350, 600, 600))
	screen.blit(high_text, pygame.Rect(400, 350, 600, 600))

	# generates a play again button, if clicked replays game
	play_button = pygame.image.load("assets/playbtn.png")
	play_button = pygame.transform.scale(play_button, (200, 100))
	play_rect = play_button.get_rect(center=(570, 315))
	screen.blit(play_button, play_rect)

	# updates certain parts of screen
	lst = [over_rect, back, back_border, play_rect]
	pygame.display.update(lst)
	return play_rect

def difficulty():
	'''() -> int, str, int
	sets difficulty for game
	'''
	# reloads screen
	screen.blit(bg, screen_rect)

	# loads difficulty buttons
	easy = pygame.image.load("assets/easybtn.png")
	hard = pygame.image.load("assets/hardbtn.png")
	insane = pygame.image.load("assets/insanebtn.png")

	# scales buttons
	easy = pygame.transform.scale(easy, (225, 125))
	hard = pygame.transform.scale(hard, (225, 125))
	insane = pygame.transform.scale(insane, (225, 125))

	# gets rect for buttons
	easy_rect = easy.get_rect(center=(400, 100))
	hard_rect = hard.get_rect(center=(400, 300))
	insane_rect = insane.get_rect(center=(400, 500))

	# prints buttons
	screen.blit(easy, easy_rect)
	screen.blit(hard, hard_rect)
	screen.blit(insane, insane_rect)
	
	# updates screen
	pygame.display.update()

	# initialize variables
	highscore_easy = 0
	highscore_hard = 0
	highscore_insane = 0
	done = True

	# checks what button is clicked on screen
	while done:
		pos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = False
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if easy_rect.collidepoint(pos):
					# checks if file is created, if no file creates one and loads highscore
					try:
						with open("assets/easy_high_score.txt") as high_score:
							highscore_easy = json.load(high_score)
					except:
						pass
					return 440, "easy", highscore_easy
				elif hard_rect.collidepoint(pos):
					try:
						with open("assets/hard_high_score.txt") as high_score:
							highscore_hard = json.load(high_score)
					except:
						pass
					return 420, "hard", highscore_hard
				elif insane_rect.collidepoint(pos):
					try:
						with open("assets/insane_high_score.txt") as high_score:
							highscore_insane = json.load(high_score)
					except:
						pass
					return 400, "insane", highscore_insane

def game(diff, score_diff, highscore):
	'''(int, str, int) -> None
	runs game
	'''
	# creates file names
	if score_diff == "easy":
		score_diff = "assets/easy_high_score.txt"
	elif score_diff == "hard":
		score_diff = "assets/hard_high_score.txt"
	elif score_diff == "insane":
		score_diff = "assets/insane_high_score.txt"
	# reloads screen
	screen.blit(bg, (0, 0))

	# initialize font
	font = pygame.font.Font("assets/flappy-bird-font.ttf", 100)

	# countdown to game
	for i in range(3, 0, -1):
		text = font.render(str(i), True, white)
		text_rect = text.get_rect(center=(400, 300))
		screen.blit(text, text_rect)
		pygame.display.flip()
		pygame.time.delay(500)
		screen.blit(bg, (0, 0))
	
	# runs game
	finished, score, highscore = main(diff, highscore)

	# stores highscore into each file
	with open(score_diff, "w") as high_score:
		json.dump(int(highscore), high_score)

	# runs game over screen	
	button = game_over(score, highscore)

	# checks for game restart or exit
	emp = True
	while emp:
		if finished == True:
			emp = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				emp = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse = pygame.mouse.get_pos()
				if button.collidepoint(mouse):
					diff, score_diff, highscore = difficulty()
					game(diff, score_diff, highscore)      
					emp = False          
	pygame.quit()

# main while loop to make everything work
var = True
while var:
	# sets fps
	clock.tick(60)
	# updates screen
	pygame.display.update()

	# checks for mouse position
	mouse = pygame.mouse.get_pos()
	
	# checks for quit, escape, mouse click and runs game accordingly
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
				try:
					diff, score_diff, highscore = difficulty()
					game(diff, score_diff, highscore)
					var = False
				except:
					var = False
					pygame.quit()
pygame.quit()