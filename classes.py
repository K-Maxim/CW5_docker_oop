from dataclasses import dataclass
from skills import GodRebuke, ShadowStep, Skill


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(name="Warrior",
                         max_health=25,
                         max_stamina=15,
                         attack=2,
                         stamina=5,
                         armor=15,
                         skill=GodRebuke()
                         )  # характеристики война

ThiefClass = UnitClass(name="Thief",
                       max_health=18,
                       max_stamina=10,
                       attack=1,
                       stamina=3,
                       armor=8,
                       skill=ShadowStep()
                       )  # характеристики вора

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}