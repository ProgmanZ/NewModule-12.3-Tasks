class Ship:

    def __init__(self, model, active=True):
        self._model = model
        self._active = active

    def __str__(self):
        return f"Модель корабля: {self._model}. {self.getter_action()}"

    def getter_action(self):
        return "Корабль идет." if self._active else "Корабль стоит на причале."

    def set_activities(self, params):
        self._active = params
        print(self.getter_action())


class War_Ship(Ship):
    def __init__(self, model, gun=0):
        super().__init__(model)
        self.__gun = gun

    def attack(self):
        return f"Корабль {self._model} атакует из {self.__gun} пушек."


class CargoShip(Ship):

    def __init__(self, model, active, fullness=0, cargo=0):
        super().__init__(model, active)
        self.__fullness = fullness
        self.__cargo = cargo

    def ship_loading(self, load=0):
        if 100 - load >= self.__cargo:
            self.__cargo += load
            print(f"Корабль {self._model} загрузили грузом = {load} и общий вес груза сейчас = {self.__cargo} тонн.")
        else:
            print(f"Недостаточно места для груза = {load} тонн на корабле.\n"
                  f"Осталось места под {100 - self.__cargo} тонн.")

    def ship_unload(self, load=0):
        if self._active:
            print("Корабль нельза разгружать, когда он идет!")
        else:

            if self.__cargo - load > 0:
                self.__cargo -= load
                print(f"Корабль {self._model} разгрузили грузом = {load} и общий вес груза = {self.__cargo} тонн.")
            elif self.__cargo == 0:
                print(f"Корабль {self._model} разгрузили.")
            else:
                print(f"На корабле {self._model} осталось разгрузить {self.__cargo} тонн")
                self.__cargo = 0


cargos = CargoShip("Грузовоз", True)
print(cargos)
cargos.ship_loading(23)
cargos.set_activities(False)
cargos.ship_unload(20)
cargos.ship_unload(20)

warship = War_Ship("Воевода", 5)
print(warship)
print(warship.attack())