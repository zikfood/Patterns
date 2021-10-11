from abc import ABC

"""
Базовые классы строительства зданий в sc2
"""


class MainBuilding(ABC):
    _system = 'default'

    def create(self):
        print('создано главное здание для ', self._system)


class InfantryBuilding(ABC):
    _system = 'default'

    def create(self):
        print('созданы бараки для ', self._system)


class SupplyBuilding(ABC):
    _system = 'default'

    def create(self):
        print('создано хранилище ресурсов для ', self._system)


"""
Производные классы постройки
для терранов
"""


class CommandCenter(MainBuilding):
    _system = 'Terran'


class Barracks(InfantryBuilding):
    _system = 'Terran'


class SupplyDepot(SupplyBuilding):
    _system = 'Terran'


"""
Производные классы постройки
для протоссов
"""


class Nexus(MainBuilding):
    _system = 'Protoss'


class Gateway(InfantryBuilding):
    _system = 'Protoss'


class Pylon(SupplyBuilding):
    _system = 'Protoss'


"""
Базовый класс абстрактной фабрики
"""


class AbstractFactory(ABC):
    main_building = None
    infantry_building = None
    supply_building = None

    def get_base_building(self):
        return self.main_building

    def get_infantry_building(self):
        return self.infantry_building

    def get_supply_building(self):
        return self.supply_building


"""
Производные классы абстрактной фабрики
"""


class TerranFactory(AbstractFactory):

    main_building = CommandCenter()
    infantry_building = Barracks()
    supply_building = SupplyDepot()


class ProtossFactory(AbstractFactory):

    main_building = Nexus()
    infantry_building = Gateway()
    supply_building = Pylon()


"""
Клиентский класс, использующий фабрику для создания базы
"""


class Base:
    def __init__(self, factory: AbstractFactory):
        self._factory = factory

    def create_base(self):
        main_building = self._factory.get_base_building()
        supply_building = self._factory.get_supply_building()
        infantry_building = self._factory.get_infantry_building()
        main_building.create()
        infantry_building.create()
        supply_building.create()


def create_factory(race_name: str) -> AbstractFactory:
    factory_dict = {
        "Terran": TerranFactory,
        "Protoss": ProtossFactory
    }
    return factory_dict[race_name]()


if __name__ == '__main__':
    race_name = "Protoss"
    buildings = create_factory(race_name)
    base = Base(buildings)
    base.create_base()
