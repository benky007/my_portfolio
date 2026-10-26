import pygame
from matrix import Matrix, m, v
import random


def create_edge(pair, vertexes):
    (vertex1, vertex2) = pair
    pygame.draw.line(screen, GREEN, (vertexes[vertex1][0], vertexes[vertex1][1]),
                     (vertexes[vertex2][0], vertexes[vertex2][1]))


def check_held(held, ax, ay, az, dim, turn_rate=0.1):
    print(axis)
    if held and dim == "x":
        ax += turn_rate
    if held and dim == "y":
        ay += turn_rate
    if held and dim == "z":
        az += turn_rate
    print(ax, ay, az)
    print("\n")
    return ax, ay, az


WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

scale = 100
dots = [WIDTH / 2, HEIGHT / 2]
auto = True
angleX = 0
angleY = 0
angleZ = 0
axis = "z"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning")

matrices = [v([-1, -1, 1]),
            v([1, -1, 1]),
            v([1, 1, 1]),
            v([-1, 1, 1]),
            v([-1, -1, -1]),
            v([1, -1, -1]),
            v([1, 1, -1]),
            v([-1, 1, -1])]
edges = [[0, 0] for i in range(len(matrices))]
pairs = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 7), (5, 6), (6, 7)]

projection_matrix = m("3x4", [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])

is_turning = False
turn = 0
running = True
while running:
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_z:
                axis = "z"
            if event.key == pygame.K_x:
                axis = "x"
            if event.key == pygame.K_y:
                axis = "y"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                is_turning = True
                turn = 0.1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                is_turning = True
                turn = -0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                is_turning = False
                turn = 0.1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                is_turning = False
                turn = -0.1

    # update
    if auto:
        turn1 = random.choice([0, 1, 2])
        if turn1 == 0:
            angleX -= 0.25
        if turn1 == 0:
            angleY -= 0.25
        if turn1 == 0:
            angleZ -= 0.25
    else:
        angleX, angleY, angleZ = check_held(is_turning, angleX, angleY, angleZ, axis, turn)
    # draw/render
    screen.fill(WHITE)

    for count, point in enumerate(matrices):
        rotated = point.rotate(angleZ, "z")
        rotated = rotated.rotate(angleY, "y")
        rotated = rotated.rotate(angleX, "x")
        rendered = projection_matrix.times(rotated)
        final = rendered.get("value")
        x = int(final[0][0] * scale) + dots[0]
        y = int(final[1][0] * scale) + dots[1]

        edges[count] = [x, y]
        pygame.draw.circle(screen, BLUE, (x, y), 5)

    for edge in pairs:
        create_edge(edge, edges)

    pygame.display.flip()
pygame.quit()
