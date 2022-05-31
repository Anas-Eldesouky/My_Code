import pygame
pygame.init()


menu = pygame.display.set_mode([1920, 1080])
menu.fill((65,90,120))


x = pygame.Rect(910, 515, 100, 50)
x2 = pygame.Rect(910, 575, 100, 50)
start_button = pygame.draw.rect(menu, (0, 0, 0), x)
quit_button = pygame.draw.rect(menu, (0, 0, 0), x2)
start_button_border = pygame.draw.rect(menu, (255, 255, 255), x, 2)
quit_button_border = pygame.draw.rect(menu, (255, 255, 255), x2, 2)
font = pygame.font.SysFont("Corbel", 19)
title_font = pygame.font.SysFont("Ariel", 100)
text = font.render("Start" , True, [255, 255, 255])
text2 = font.render("Quit", True, [255, 255, 255])
title_text = title_font.render("Flappy Bird", True, [255, 255, 255])
text2_rect = text2.get_rect(center = (1920 / 2, (1080 / 2) + 60))
text_rect = text.get_rect(center = (1920 / 2, 1080 / 2))
title_rect = title_text.get_rect(center = (1920 / 2, (1080 / 2) - 150))
menu.blit(text, text_rect)
menu.blit(text2, text2_rect)
menu.blit(title_text, title_rect)

def start():
	menu.fill([0, 0, 0])

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
			if quit_button.collidepoint(mouse):
				pygame.quit()
				var = False
			elif start_button.collidepoint(mouse):
				start()