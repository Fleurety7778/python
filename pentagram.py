import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Pentagram")

clock = pygame.time.Clock()

pent_speed = 5

pent_image = pygame.image.load("pentagram.jpg")

pent_rect = pent_image.get_rect()

pent_rect.topleft = (30,30)

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pent_rect.x -= pent_speed
    if keys[pygame.K_RIGHT]:
        pent_rect.x += pent_speed
    if keys[pygame.K_UP]:
        pent_rect.y -= pent_speed
    if keys[pygame.K_DOWN]:
        pent_rect.y += pent_speed
    if pent_rect.left < 0:
        pent_rect.left = 0
    if pent_rect.right > 800:
        pent_rect.right = 800
    if pent_rect.top < 0:
        pent_rect.top = 0
    if pent_rect.bottom > 600:
        pent_rect.bottom = 600

    screen.fill((0,0,0))

    screen.blit(pent_image, pent_rect.topleft)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()



