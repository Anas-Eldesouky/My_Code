import pygame
pygame.init()

class button():
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
		font = pygame.font.SysFont("Ariel", 19)
		draw_text = font.render(self.text, True, self.text_color)
		dest = draw_text. get_rect(center=(self.x + self.width/2, self.y + self.height/2))
		self.screen.blit(draw_text, dest)

screen = pygame.display.set_mode([1920, 1080])
screen.fill((65,90,120))
white = (255, 255, 255)
black = (0, 0, 0)

start = button(screen, 200, 100, 700, 700, "Start", white, black, white)
start.draw()
# x = pygame.Rect(910, 515, 100, 50)
# x2 = pygame.Rect(910, 575, 100, 50)
# start_button = pygame.draw.rect(screen, black, x)
# quit_button = pygame.draw.rect(screen, black, x2)
# start_button_border = pygame.draw.rect(screen, white, x, 2)
# quit_button_border = pygame.draw.rect(screen, white, x2, 2)
# font = pygame.font.SysFont("Corbel", 19)
# title_font = pygame.font.SysFont("Ariel", 100)
# text = font.render("Start" , True, white)
# text2 = font.render("Quit", True, white)
# title_text = title_font.render("Flappy Bird", True, white)
# text2_rect = text2.get_rect(center = (1920 / 2, (1080 / 2) + 60))
# text_rect = text.get_rect(center = (1920 / 2, 1080 / 2))
# title_rect = title_text.get_rect(center = (1920 / 2, (1080 / 2) - 150))
# screen.blit(text, text_rect)
# screen.blit(text2, text2_rect)
# screen.blit(title_text, title_rect)

def start():
	screen.fill(black)

var = True
while var:
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
		# if event.type == pygame.MOUSEBUTTONDOWN:
		# 	if quit_button.collidepoint(mouse):
		# 		pygame.quit()
		# 		var = False
		# 	elif start_button.collidepoint(mouse):
		# 		start()