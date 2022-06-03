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
screen.fill((64, 122, 82))
white = (255, 255, 255)
black = (0, 0, 0)

start_button = Button(screen, 200, 100, 200, 200, "Start", white, black, white)
quit_button = Button(screen, 200, 100, 50, 50, "Quit", white, black, white)
start = start_button.draw()
quit = quit_button.draw()
def start_action():
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
		if event.type == pygame.MOUSEBUTTONDOWN:
			if start.collidepoint(mouse):
				start_action()