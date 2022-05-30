import pygame
pygame.init()


menu = pygame.display.set_mode([1000, 600])
menu.fill((65,90,120))


x = pygame.Rect(450, 275, 100, 50)
button = pygame.draw.rect(menu, (0, 0, 0), x)
button_border = pygame.draw.rect(menu, (255, 255, 255), x, 2)
font = pygame.font.SysFont("Corbel", 19)
text = font.render("Quit" , True, [255, 255, 255])
text_test = text.get_rect(center = (1000 / 2, 600 / 2))
menu.blit(text, text_test)


var = True
while var:
	pygame.display.update()
	mouse = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			var = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if button.collidepoint(mouse):
				pygame.quit()
				var = False