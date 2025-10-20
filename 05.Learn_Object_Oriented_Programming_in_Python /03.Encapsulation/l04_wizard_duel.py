class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    # don't touch above this line

    def get_fireballed(self, fireball_damage):
        self.fireball = fireball_damage - self.__stamina
        self.health = self.health - self.fireball

    def drink_mana_potion(self, potion_mana):
        self.potion = potion_mana + self.__intelligence
        self.mana = self.mana + self.potion        
