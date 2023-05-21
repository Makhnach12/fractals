import random
import numpy as np
import pygame
from math import floor
from collections import deque
from pygame import gfxdraw


def renderHeights(screen, heights):
    for i, height in enumerate(heights):
        gfxdraw.pixel(screen, i, height, (255, 255, 255))


def MidPointCounter(imageWidth, heights):
    roughness = 200

    # we create a queue of the line segments we need to subdivide
    q = deque()

    # and add the first segment to it
    q.append((imageWidth - 601, imageWidth - 1, roughness))

    # now we go through and subdivide each segment
    while len(q) != 0:
        left, right, randomness = q.popleft()
        center = (left + right + 1) // 2

        # set the midpoint to the average of the two ends
        heights[center] = (heights[left] + heights[right]) // 2

        # and then add some randomness
        heights[center] = heights[center] + random.randint(-randomness, randomness)

        # if the width of the segment is greater than 2 then it can be subdivided
        if right - left > 2:
            # when we add the new line segments to the queue, we reduce the amount of randomness
            q.append((left, center, floor(randomness // 2)))
            q.append((center, right, floor(randomness // 2)))


def main():
    flag: bool = False
    iterator: int = 0
    is_iterator_moving: bool = False
    imageWidth = 600
    heights = [0] * imageWidth
    # and then initialize the first and last heights to random values
    heights[0] = random.randint(0, 256)
    heights[imageWidth - 1] = random.randint(0, 256)
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.fill((0, 0, 0))
    MidPointCounter(imageWidth, heights)
    renderHeights(screen, heights[imageWidth - 600:imageWidth - 1])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    is_iterator_moving = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    is_iterator_moving = False
        if is_iterator_moving:
            iterator += 1
            flag = False
        if iterator % 600 == 0 and not flag:
            imageWidth += 600
            heights.extend([0] * 600)
            heights[imageWidth - 1] = random.randint(0, 256)
            MidPointCounter(imageWidth, heights)
            flag = True
        screen.fill((0, 0, 0))
        renderHeights(screen, heights[0 + iterator:imageWidth - 1 + iterator])
        pygame.display.update()


main()
