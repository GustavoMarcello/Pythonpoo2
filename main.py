from modelo import *


vingadores = Filme('avengers - Infinite war', 2018, 160)
print(f'{vingadores.nome} - {vingadores.duracao} - Likes: {vingadores.likes}')
vingadores.dar_like()

got = Serie('Game of thrones', 2013, 7)
print(f'Nome: {got.nome} - Ano: {got.ano} - Temporadas: {got.temporada} - Likes: {got.likes}')
got.nome = 'gerra dos tronos'
got.dar_like()
print(f'Nome: {got.nome} - Ano: {got.ano} - Temporadas: {got.temporada} - Likes: {got.likes}')