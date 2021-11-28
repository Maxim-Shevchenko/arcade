import arcade
import random
# устанавливаем константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Star Battle"


# класс с игрой
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("space_background.png")
        self.space_ship = SpaceShip("x-wing.png", 0.5)
        self.set_mouse_visible(False)
        self.bullets = arcade.SpriteList()
        self.enemies = arcade.SpriteList()
        self.score = 0
        self.fails = 0


    # начальные значения
    def setup(self):
        self.space_ship.center_x = SCREEN_WIDTH / 2
        self.space_ship.center_y = 70
        for i in range(50):
            enemy = Enemy()
            enemy.center_x = random.randint(20, SCREEN_WIDTH - 20)
            enemy.center_y = 50 * i + SCREEN_HEIGHT
            self.enemies.append(enemy)


        # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.space_ship.draw()
        self.bullets.draw()
        self.enemies.draw()
        arcade.draw_text(f"Счет: {self.score}", 10, 20, arcade.color.WHITE, 14)

        arcade.draw_text(f"Неудачи: {self.fails}", 710, 20, arcade.color.WHITE, 14)
        if self.fails>=3:
            self.space_ship.stop()
            for bullet in self.bullets:
                bullet.stop()
                bullet.kill()
            for enemy in self.enemies:
                enemy.stop()
            arcade.draw_text(f"ПРОИГРАЛ", 100, 200, arcade.color.WHITE, 14)
    # игровая логика
    def update(self, delta_time):
        self.space_ship.update()
        self.bullets.update()
        for bullet in self.bullets:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemies)
            if len(hit_list) > 0:
                bullet.kill()
                self.score+=1
                for enemy in hit_list:
                    enemy.kill()

        self.enemies.update_animation()
        self.enemies.update()

    def on_mouse_motion(self, x, y, dx, dy):
        self.space_ship.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        bullet = Bullet()
        bullet.center_x = self.space_ship.center_x
        bullet.bottom = self.space_ship.top
        self.bullets.append(bullet)
        arcade.play_sound(bullet.laser_sound)

class SpaceShip(arcade.Sprite):
    def update(self):
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left < 0:
            self.left = 0

class Bullet(arcade.Sprite):
    def __init__(self):
        super().__init__("laser.png", 0.8)
        self.change_y = 5
        self.laser_sound = arcade.load_sound("laser.wav")

    def update(self):
        self.center_y += self.change_y

class Enemy(arcade.AnimatedTimeSprite):

    def __init__(self):
        super().__init__()
        self.textures.append(arcade.load_texture("tie fighter.png"))
        self.textures.append(arcade.load_texture("tie fighter2.png"))
        self.change_y = 1

    def update(self):
        self.center_y -= self.change_y
        if self.center_y < 0:
            self.kill()
            window.fails+=1

window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
