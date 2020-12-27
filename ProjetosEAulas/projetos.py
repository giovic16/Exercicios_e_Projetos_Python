
print('Bem-vindo(a) a nossa biblioteca de musica, para escolher uma musica digite sim, para nega-lo digite nao!')
m1 = str(input('Musica1?'))
m2 = str(input('Musica2?'))
m3 = str(input('Musica3?'))
while 'm1' or 'm2' or 'm3':
    if m1 == 'sim' or m1 == 'Sim':
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load('m1.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass

    elif m2 == 'sim' or m2 == 'Sim':
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load('m2.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass

    elif m3 == 'sim' or m3 == 'Sim':
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load('m3.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass








