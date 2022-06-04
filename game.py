import pygame
pygame.init()

class Button():
	def __init__(self, screen, width, height, x, y, text, text_color, color, border_color):
		self.screen = screen
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.text = text
		self.text_color = text_color
		self.color = color
		self.border_color = border_color
	
	def draw(self):
		rect = pygame.Rect(self.x, self.y, self.width, self.height)
		button = pygame.draw.rect(self.screen, self.color, rect)
		button_border = pygame.draw.rect(self.screen, self.border_color, rect, 2)
		font = pygame.font.SysFont("Ariel", 30)
		draw_text = font.render(self.text, True, self.text_color)
		dest = draw_text.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
		self.screen.blit(draw_text, dest)
		return button

screen = pygame.display.set_mode([800, 600])
screen_rect = screen.get_rect()
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (800, 600))
screen.blit(bg, screen_rect)

white = (255, 255, 255)
black = (0, 0, 0)

img = pygame.image.load("logo.png")
img = pygame.transform.scale(img, (350, 100))
screen.blit(img, (225, 105))

start_button = Button(screen, 200, 100, 300, 250, "Start", white, black, white)
quit_button = Button(screen, 200, 100, 300, 370, "Quit", white, black, white)
start = start_button.draw()
quit = quit_button.draw()

def main():
	x = 20
	y = 20
	bird = pygame.image.load("yellowbird-downflap.png")
	finished = False
	while not finished:
		screen.blit(bg, screen_rect)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			y -= 2
		if keys[pygame.K_DOWN]:
			y += 2
		if keys[pygame.K_RIGHT]:
			x += 2
		if keys[pygame.K_LEFT]:
			x -= 2
		if x <= 0:
			x = 0
		elif x >= 766:
			x = 766
		if y <= 0:
			y = 0
		elif y >= 576:
			y = 576
		screen.blit(bird, (x,y))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				finished = True

def start_action():
	screen.fill(black)

var = True
while var:
	clock = pygame.time.Clock()
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
			if start.collidepoint(mouse):
				start_action()
				main()
				var = False
	