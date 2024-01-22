# inheritance

class Monster:
    def __init__(self,hp,name,damage):
        self.hp = hp
        self.name = name
        self.damage = damage
    def attack(self, character):
        character.hp -= self.damage

class Slime(Monster):
    def __init__(self,hp,name,damage,poison):
        super().__init__(hp,name,damage) # 부모의 생성자
        self.poison = poison # 자기의 생성자

    def sprayPoison(self,charcter):
        character.hp -= self.damage + self.poison

# kim = Character()
a = Slime(hp:50, name:'귀여운슬라임', damage:30,poison:5)
# a.attack(kim)
# a.sprayPoison(kim)
