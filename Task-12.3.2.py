class Robots:

    def __init__(self, model, action):
        self._model = model
        self._action = action

    def operate(self):
        print(f"\nРобот сейчас {self._action}.")


class DusterRobots(Robots):

    def __init__(self, model, action="пылесосит пол", bunker=0):
        super().__init__(model, action)
        self._bunker = bunker

    def operate(self):
        super().operate()
        print(f"Текущая заполняемость мешка = {self._bunker}.")



class WarRobots(Robots):

    def __init__(self, model, guns, action="защищает военный объект.", ):
        super().__init__(model, action)
        self._guns = guns

    def operate(self):
        super().operate()
        print(f"С помощью {self._guns} пушек.")


class WarSheeps(WarRobots):

    def __init__(self, model, guns, deep):
        super().__init__(model, guns)
        self._deep = deep

    def operate(self):
        super().operate()
        print(f"Охрана ведется на глубине {self._deep} метров.")


dustR = DusterRobots("Dust")
warR = WarRobots("WarR",10)
sheepR = WarSheeps("DeepWarR", 30,4000)

dustR.operate()
warR.operate()
sheepR.operate()





