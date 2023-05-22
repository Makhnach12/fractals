import random
import pygame
from math import floor
from collections import deque
from pygame import gfxdraw


def GetGoodRandom(heights: list[int], left: int, right: int, roughness: int):
    center = (left + right + 1) // 2
    while heights[center] <= 0 or heights[center] >= 600:
        heights[center] = (heights[left] + heights[right]) // 2 + \
                          roughness * (right - left + 1) * random.randint(-1, 1)


def renderHeights(screen, heights):
    for i, height in enumerate(heights):
        gfxdraw.pixel(screen, i, int(height), (255, 255, 255))


def MidPointCounter(imageWidth, heights, roughness):
    q = deque()

    q.append((imageWidth - 601, imageWidth - 1, roughness))

    while len(q) != 0:
        left, right, randomness = q.popleft()
        center = (left + right + 1) // 2

        GetGoodRandom(heights, left, right, roughness)

        if right - left > 2:
            q.append((left, center, floor(randomness // 2)))
            q.append((center, right, floor(randomness // 2)))


def main():
    roughness = 0.2
    flag: bool = False
    iterator: int = 0
    is_iterator_moving_right: bool = False
    is_iterator_moving_left: bool = False
    imageWidth: int = 600
    heights = [0] * imageWidth
    heights[0] = random.randint(0, 256)
    heights[imageWidth - 1] = heights[0]
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.fill((0, 0, 0))
    MidPointCounter(imageWidth, heights, roughness)
    renderHeights(screen, heights[imageWidth - 600:imageWidth - 1])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    is_iterator_moving_right = True
                if event.key == pygame.K_LEFT:
                    is_iterator_moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    is_iterator_moving_right = False
                if event.key == pygame.K_LEFT:
                    is_iterator_moving_left = False
        if is_iterator_moving_right:
            iterator += 1
            flag = False
        if is_iterator_moving_left:
            if iterator > 0:
                iterator -= 1
        if iterator % 600 == 0 and not flag:
            imageWidth += 600
            heights.extend([0] * 600)
            heights[imageWidth - 1] = heights[0] + (roughness * 600 * random.randint(-1, 1)) % 600
            MidPointCounter(imageWidth, heights, roughness)
            flag = True
        screen.fill((0, 0, 0))
        renderHeights(screen, heights[0 + iterator:imageWidth - 1 + iterator])
        pygame.display.update()


main()
