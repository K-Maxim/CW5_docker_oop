from dataclasses import dataclass, field
from typing import List
from random import uniform
import marshmallow_dataclass
import marshmallow
import json


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    max_damage: float
    min_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        return round(uniform(self.min_damage, self.max_damage), 1)


WeaponSchema = marshmallow_dataclass.class_schema(Weapon)
ArmorSchema = marshmallow_dataclass.class_schema(Armor)


@dataclass
class EquipmentData:
    # TODO содержит 2 списка - с оружием и с броней
    weapons: [List]
    armors: [List]


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Weapon:
        # TODO возвращает объект оружия по имени
        for weapon in self.equipment.weapons:
            if weapon_name == weapon.name:
                print(weapon)
                return weapon

    def get_armor(self, armor_name) -> Armor:
        # TODO возвращает объект брони по имени
        for armor in self.equipment.armors:
            if armor_name == armor.name:
                return armor

    def get_weapons_names(self) -> list:
        # TODO возвращаем список с оружием
        return [weapons.name for weapons in self.equipment.weapons]

    def get_armors_names(self) -> list:
        # TODO возвращаем список с броней
        return [armor.name for armor in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        # TODO этот метод загружает json в переменную EquipmentData
        with open("./data/equipment.json", 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return EquipmentData(weapons=WeaponSchema(many=True).load(data['weapons']),
                             armors=ArmorSchema(many=True).load(data['armors']))
