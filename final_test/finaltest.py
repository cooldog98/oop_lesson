class Diagrams:
    class Person:
        def __init__(self, name: str = 'mandatory', born: str = '500', job: str = 'Unemployed', level: int = 1, money: int = 0):
            if not isinstance(name, str):
                raise TypeError
            if isinstance(born, float):
                raise TypeError
            if not isinstance(level, int):
                raise TypeError
            if money < 0:
                raise ValueError
            elif not isinstance(money, int):
                raise TypeError
            self.name = name
            self.born = born
            self.job = job
            self.level = level
            self.money = money

        def get_name(self):
            return self.name

        def set_name(self, name):
            return self.name == name

        def get_born(self):
            return self.born

        def set_born(self, born):
            return self.born == born

        def get_job(self):
            return self.job

        def set_job(self, job):
            return self.job == job

        def get_level(self):
            return self.level

        def set_level(self, level):
            return self.level == level

        def get_money(self):
            return self.money

        def set_money(self, money):
            return self.money == money

        def __str__(self):
            return f'[{self.job} {self.name}, Level {self.level}, born Year {self.born}, $ {self.money}]'
        def __str__(self):
            return f'[{self.job} {self.name}, Level {self.level}, born Year {self.born}, $ {self.money}]'

        # @property
        # def get_name(self):
        #     return self.name

        # def set_name(self, name):
        #     if not isinstance(name, str):
        #         raise TypeError
        #     return self.name == name

        # @property
        # def get_born(self):
        #     return self.born

        # def set_born(self, born):
        #     if not isinstance(born, str):
        #         raise TypeError
        #     return self.born == born

        # @property
        # def job(self):
        #     return self.job

        # @job.setter
        # def job(self, job):
        #     if not isinstance(job, str):
        #         raise TypeError
        #     return self.job == job

        # @property
        # def get_level(self):
        #     return self.level

        # def set_level(self, level):
        #     if not isinstance(level, int):
        #         raise TypeError
        #     return self.level == level

        # @property
        # def get_money(self):
        #     return self.money

        # def set_money(self, money):
        #     if money < 0:
        #         raise ValueError
        #     elif not isinstance(money, str):
        #         raise TypeError
        #     return self.money == money

    p = Person('Bob', 500, 'Unemployed', 1, 100)
    print(p)
    p = Person('Bob', 400, 'Carpenter', 2)
    print(p)
    p = Person('Bob', level=2, job='Something')
    print(p)
    p = Person('Joe', born=100.0)
    print(p)
    p = Person('Bob', money=-1)
    print(p)

    class Quest:
        def __init__(self, title: str ='mandatory', level:int = 1, reward:int = 0, job:str = '*'):
            if not isinstance(title, str):
                raise TypeError
            if not isinstance(level, int):
                raise TypeError
            if not isinstance(reward, int):
                raise TypeError
            elif reward < 0:
                raise ValueError
            if not isinstance(job, str):
                raise TypeError
            self.title = title
            self.level = level
            self.reward = reward
            self.job = job

        def get_title(self):
            return self.title

        def set_title(self, title):
            return self.title == title

        def get_level(self):
            return self.level

        def set_level(self, level):
            return self.level == level

        def get_reward(self):
            return self.reward

        def set_reward(self, reward):
            return self.reward == reward

        def get_job(self):
            return self.job

        def set_job(self, job):
            return self.job == job

        def __str__(self):
            return f'[Quest "{self.title}" for Level {self.level} {self.job}, $ {self.reward}]'

    class Adventurer:
        def __init__(self,  title, level, reward, job):
            super().__init__(title: str ='mandatory', level:int = 1, reward:int = 0, job:str = '*')


