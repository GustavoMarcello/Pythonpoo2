from modelo import *


vingadores = Filme('avengers - Infinite war', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')
vingadores.dar_like()

got = Serie('Game of thrones', 2013, 7)
print(f'Nome: {got.nome} - Ano: {got.ano} - Temporadas: {got.temporada} - Likes: {got.likes}')
got.dar_like()