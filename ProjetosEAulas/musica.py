print('Bem-vindo(a) a nossa biblioteca de musica, para escolher um Hit digite sim, para nega-lo digite nao!')
cha = str(input('Cha?'))
lencol = str(input('Lençol?'))
tala = str(input('Talarica?'))
while 'cha' or 'lencol' or 'tala':
    if cha == 'sim' or cha == 'Sim':
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load('cha.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass

    elif lencol == 'sim' or lencol == 'Sim':
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load('lencol.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass

    elif tala == 'sim' or tala == 'Sim':
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load('talarica.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass









