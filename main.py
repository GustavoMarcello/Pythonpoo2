from modelo import *


vingadores = Filme('avengers - Infinite war', 2018, 160)
lotr = Filme('o senhor dos aneis - o retorno do rei', 2003, 200)
got = Serie('Game of thrones', 2013, 7)
sherlock = Serie('sherlock', 2018, 4)

vingadores.dar_like()
lotr.dar_like()
vingadores.dar_like()
got.dar_like()
vingadores.dar_like()
sherlock.dar_like()
sherlock.dar_like()
vingadores.dar_like()


filmes_series = [vingadores, got, lotr, sherlock]
playlist_fim_de_semana = Playlist('sessão pipoca', filmes_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Esta na lista?: {lotr in playlist_fim_de_semana}')

