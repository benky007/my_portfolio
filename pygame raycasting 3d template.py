import pygame
import sys
import math

RES = WIDTH, HEIGHT = 1200, 600
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

PLAYER_POS = 1.5, 5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

_ = False
mini_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, 1, 1, 1, _, _, _, _, _, _, _, 1, 1, 1, _, _, _, _, 1],
            [1, _, _, _, 1, _, _, _, 1, _, _, _, 1, _, 1, _, 1, _, _, 1],
            [1, _, _, _, 1, _, _, _, 1, _, 1, _, 1, _, _, _, 1, _, _, 1],
            [1, _, _, _, _, _, _, _, 1, _, 1, _, 1, _, _, _, _, _, _, 1],
            [1, 1, 1, _, _, _, _, _, _, 1, 1, _, 1, 1, 1, _, _, _, _, 1],
            [1, _, _, _, 1, 1, 1, _, _, _, _, _, _, _, _, 1, _, _, _, 1],
            [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class Game:
    def __init__(self, master):
        self.master = master
        self.master.init()
        self.screen = self.master.display.set_mode(RES)
        self.clock = self.master.time.Clock()
        self.delta_time = 1
        self.map = None
        self.player = None
        self.raycasting = None
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.master.display.flip()
        self.delta_time = self.clock.tick(FPS)
        self.master.display.set_caption(f"{self.clock.get_fps()}")

    def draw(self):
        self.screen.fill("black")
        # for 2D
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        for event in self.master.event.get():
            if event.type == self.master.QUIT or (
                    event.type == self.master.KEYDOWN and event.key == self.master.K_ESCAPE):
                self.master.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


class Map:
    def __init__(self, game):
        self.game = game
        self.master = self.game.master
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for y, row in enumerate(self.mini_map):
            for x, value in enumerate(row):
                if value:
                    self.world_map[(x, y)] = value

    def draw(self):
        [self.master.draw.rect(self.game.screen, 'darkgray', (pos[0] * 60, pos[1] * 60, 60, 60), 2)
         for pos in self.world_map]


class Player:
    def __init__(self, game):
        self.game = game
        self.master = self.game.master
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = self.master.key.get_pressed()
        if keys[self.master.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[self.master.K_a]:
            dx += speed_sin
            dy -= speed_cos
        if keys[self.master.K_s]:
            dx -= speed_cos
            dy -= speed_sin
        if keys[self.master.K_d]:
            dx -= speed_sin
            dy += speed_cos
        if keys[self.master.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[self.master.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time

        self.check_wall_collision(dx, dy)
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        # player facing for debugging
        # self.master.draw.line(self.game.screen, 'yellow', (self.x * 60, self.y * 60),
        #                       (self.x * 60 + WIDTH * math.cos(self.angle),
        #                        self.y * 60 + WIDTH * math.sin(self.angle)), 2)
        self.master.draw.circle(self.game.screen, 'green', (self.x * 60, self.y * 60), 9)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)


class RayCasting:
    def __init__(self, game):
        self.game = game
        self.master = self.game.master

    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # depth
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            # draw for debug
            # self.master.draw.line(self.game.screen, 'yellow', (60 * ox, 60 * oy),
            #                       (60 * ox + 60 * depth * cos_a, 60 * oy + 60 * depth * sin_a), 2)

            # remove fishbowl effect
            depth *= math.cos(self.game.player.angle - ray_angle)

            # projection
            proj_height = SCREEN_DIST / (depth + 0.0001)

            # draw walls for 3D
            color = [255 / (1 + depth ** 5 * 0.0002)] * 3
            self.master.draw.rect(self.game.screen, color,
                                  (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()


if __name__ == '__main__':
    app = Game(pygame)
    app.run()
