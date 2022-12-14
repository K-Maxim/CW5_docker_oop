from __future__ import annotations
from abc import ABC, abstractmethod
from equipment import Equipment, Weapon, Armor
from classes import UnitClass
from random import randint
from typing import Optional


class BaseUnit(ABC):
    """Базовый класс юнита"""
    def __init__(self, name: str, unit_class: UnitClass, weapon: Weapon, armor: Armor):
        """При инициализации класса Unit используем свойства класса UnitClass"""
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.stamina = unit_class.max_stamina
        self.weapon = weapon
        self.armor = armor
        self._is_skill_used = False

    @property
    def health_points(self):
        return self.hp

    @property
    def stamina_points(self):
        return self.stamina

    def equip_weapon(self, weapon: Weapon):
        return f"{self.name} использует оружие: {weapon}"

    def equip_armor(self, armor: Armor):
        return f"{self.name} использует броню: {armor}"

    def _count_damage(self, target: BaseUnit) -> int:
        """расчет урона"""
        self.stamina -= self.weapon.stamina_per_hit * self.unit_class.stamina
        damage = self.weapon.damage * self.unit_class.attack
        if target.stamina > target.armor.stamina_per_turn * target.unit_class.stamina:
            target.stamina -= target.armor.stamina_per_turn * target.unit_class.stamina
            damage = damage - target.armor.defence * target.unit_class.armor
        damage = target.get_damage(damage)
        return damage

    def get_damage(self, damage: int) -> Optional[int]:
        """получение урона целью"""
        if damage > 0:
            self.hp -= damage
            self.hp = self.hp
            return round(damage, 1)
        return None

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        """этот метод будет переопределен ниже"""
        pass

    def use_skill(self, target: BaseUnit) -> str:
        """метод использования умения."""
        if self._is_skill_used:
            return "Навык уже использован"
        self._is_skill_used = True
        return self.unit_class.skill.use(user=self, target=target)


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """функция удар игрока:"""
        if self.stamina >= self.weapon.stamina_per_hit * self.unit_class.stamina:
            damage = self._count_damage(target)
            if damage:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона."
            return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает."
        return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
        # TODO результат функции должен возвращать следующие строки:


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """функция удар соперника"""
        if randint(0, 100) < 10 and self.stamina >= self.unit_class.skill.stamina and not self._is_skill_used:
            return self.use_skill(target)
        if self.stamina >= self.weapon.stamina_per_hit * self.unit_class.stamina:
            damage = self._count_damage(target)
            if damage:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} и наносит Вам {damage} урона."
            return f"{self.name} используя {self.weapon.name} наносит удар, но Ваш(а) {target.armor.name} его останавливает."
        return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."



