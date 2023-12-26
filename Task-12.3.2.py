class Robots:

    def __init__(self, model, action):
        self._model = model
        self._action = action

    def _operate(self):
        return {self._action}

    def __str__(self):
        return f"Робот: {self._model} Сейчас делает: {self._operate():}."


class DusterRobots(Robots):

    def __init__(self, model, action, bunker=0):
        super().__init__(model, action)
        self.bunker = bunker

    def _operate(self):
        self.bunker += 10
        return f"{self.__str__()}\nЗаполненность мешка сейчас:{self.bunker}."


class WarRobots(Robots):

    def __init__(self, model, deep, action):
        super().__init__(model)
        self.deep = deep
        self.action = action

