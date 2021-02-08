import os
import sys

import pygame
import requests
API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

toponym_to_find = ','.join(input('Введите координаты в виде (координатаХ,координатаУ): ').split(',')[::-1])
spn = input('Введите масштаб в виде (значение,значение): ')

map_params = {
    'll': toponym_to_find,
    "l": "map",
    'spn': spn
}

map_api_server = "http://static-maps.yandex.ru/1.x/"


response = requests.get(map_api_server, params=map_params)

pygame.init()
screen = pygame.display.set_mode((600, 450))

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
os.remove(map_file)
