class Gobj:
    def __init__(self, sprite):
        self.sprite = sprite


class Entity(Gobj):
    def __init__(self, x, y, hp, speed, dmg, sprite):
        super().__init__(sprite)
        self.x = x
        self.y = y
        self.hp = hp
        self.speed = speed
        self.dmg = dmg

    def move(self):
        pass

    def attack(self):
        pass

    def take_damage(self):
        pass


class Player(Entity):
    def __init__(self, x, y, hp, speed, dmg, sprite, money):
        super(Player, self).__init__(x, y, hp, speed, dmg, sprite)
        self.money = money

