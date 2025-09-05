from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    def print(self):
        print(f"{self.__name__}: {'{'}")
        for name, value in vars(self).items():
            print(f"{name!r} = {value!r}")
        print("}")
