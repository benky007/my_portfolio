# TODO: you got to 31:00 in the video https://www.youtube.com/watch?v=ECqUrT7IdqQ

import pygame
import sys
import math
import os
import collections

RES = WIDTH, HEIGHT = 1200, 600
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

PLAYER_POS = 1.5, 5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE_SCALE = 60

MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 60
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30, 30, 30)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

_ = False
mini_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, 3, 3, 3, _, _, _, _, _, _, _, 1, 3, 1, _, _, _, _, 1],
            [1, _, _, _, 3, _, _, _, 2, _, _, _, 3, _, 1, _, 4, _, _, 1],
            [1, _, _, _, 3, _, _, _, 2, _, 1, _, 1, _, _, _, 4, _, _, 1],
            [1, _, _, _, _, _, _, _, 4, _, 1, _, 3, _, _, _, _, _, _, 1],
            [1, 3, 2, _, _, _, _, _, _, 4, 1, _, 1, 3, 1, _, _, _, _, 1],
            [1, _, _, _, 2, 2, 2, _, _, _, _, _, _, _, _, 1, _, _, _, 1],
            [1, _, _, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class Game:
    def __init__(self, master):
        self.animated_sprite = None
        self.master = master
        self.master.init()
        self.master.mouse.set_visible(False)
        self.screen = self.master.display.set_mode(RES)
        self.clock = self.master.time.Clock()
        self.delta_time = 1
        self.map = None
        self.player = None
        self.raycasting = None
        self.object_renderer = None
        self.static_sprite = None
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.static_sprite = SpriteObject(self)
        self.animated_sprite = AnimatedSprite(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.static_sprite.update()
        self.animated_sprite.update()
        self.master.display.flip()
        self.delta_time = self.clock.tick(FPS)
        self.master.display.set_caption(f"{self.clock.get_fps()}")

    def draw(self):
        # self.screen.fill("black")
        self.object_renderer.draw()
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
        self.rel = None
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
        # if keys[self.master.K_LEFT]:
        #     self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        # if keys[self.master.K_RIGHT]:
        #     self.angle += PLAYER_ROT_SPEED * self.game.delta_time

        self.check_wall_collision(dx, dy)
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        # player facing for debugging
        # self.master.draw.line(self.game.screen, 'yellow', (self.x * 60, self.y * 60),
        #                       (self.x * 60 + WIDTH * math.cos(self.angle),
        #                        self.y * 60 + WIDTH * math.sin(self.angle)), 2)
        self.master.draw.circle(self.game.screen, 'green', (self.x * 60, self.y * 60), 9)

    def mouse_control(self):
        mx, my = self.master.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            self.master.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = self.master.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()

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
        self.ray_casting_result = []
        self.objects_to_render = []
        self.textures = self.game.object_renderer.wall_textures

    def get_objects_to_render(self):
        self.objects_to_render = []
        for ray, values in enumerate(self.ray_casting_result):
            depth, proj_height, texture, offset = values

            if proj_height < HEIGHT:
                wall_column = self.textures[texture].subsurface(offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE)
                wall_column = self.master.transform.scale(wall_column, (SCALE, proj_height))
                wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
            else:
                texture_height = TEXTURE_SIZE * HEIGHT / proj_height
                wall_column = self.textures[texture].subsurface(offset * (TEXTURE_SIZE - SCALE),
                                                                HALF_TEXTURE_SIZE - texture_height // 2, SCALE,
                                                                texture_height)
                wall_column = self.master.transform.scale(wall_column, (SCALE, HEIGHT))
                wall_pos = (ray * SCALE, 0)

            self.objects_to_render.append((depth, wall_column, wall_pos))

    def ray_cast(self):
        self.ray_casting_result = []
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        texture_vert, texture_hor = 1, 1
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
                    texture_hor = self.game.map.world_map[tile_hor]
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
                    texture_vert = self.game.map.world_map[tile_vert]
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # depth, texture offset
            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor

            # draw for debug
            # self.master.draw.line(self.game.screen, 'yellow', (60 * ox, 60 * oy),
            #                       (60 * ox + 60 * depth * cos_a, 60 * oy + 60 * depth * sin_a), 2)

            # remove fishbowl effect
            depth *= math.cos(self.game.player.angle - ray_angle)

            # projection
            proj_height = SCREEN_DIST / (depth + 0.0001)

            # draw walls for 3D debugging
            # color = [255 / (1 + depth ** 5 * 0.0002)] * 3
            # self.master.draw.rect(self.game.screen, color,
            #                       (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

            # ray casting result
            self.ray_casting_result.append((depth, proj_height, texture, offset))

            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()
        self.get_objects_to_render()


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.master = self.game.master
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/textures/sky.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))

        self.master.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.png'),
            5: self.get_texture('resources/textures/5.png')
        }


class SpriteObject:
    def __init__(self, game, path='resources/sprites/static_sprites/candlebra.png', pos=(10.5, 3.5),
                 scale=0.7, shift=0.27):
        self.sprite_half_width = 0
        self.norm_dist = 1
        self.dist = 1
        self.screen_x = 0
        self.theta = 0
        self.dy = 0
        self.dx = 0
        self.game = game
        self.master = self.game.master
        self.player = game.player
        self.x, self.y = pos
        self.image = self.master.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift

    def get_sprite_projection(self):
        proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj
        
        image = self.master.transform.scale(self.image, (proj_width, proj_height))
        
        self.sprite_half_width = proj_width // 2
        height_shift = proj_height * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2 + height_shift
        
        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)
        
        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau
            
        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        self.get_sprite()


class AnimatedSprite(SpriteObject):
    def __init__(self, game, path='resources/sprites/animated_sprites/green_light/0.png', pos=(9.5, 5.5),
                 scale=0.8, shift=0.15, animation_time=120):
        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = self.master.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = self.master.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    def get_images(self, path):
        images = collections.deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = self.master.image.load(path+'/'+file_name).convert_alpha()
                images.append(img)
        return images


if __name__ == '__main__':
    app = Game(pygame)
    app.run()
