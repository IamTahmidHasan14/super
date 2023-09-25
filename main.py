#SUPER KEYWORD
class State:
  # stadium = "Gabba"
  def __init__(self, name, city):
    self.name = name
    self.city = city

  def details(self):
    print(f"{self.city} is the capital of {self.name}")


class City(State):

  def __init__(self, name, city, area):
    super().__init__(name, city)
    self.area = area

  def details(self):
    print(
      f"{self.city} is the capital of {self.name}. And the area is {self.area}"
    )

    super().details()


s = State("QL", "Brisbane")
s.details()
c = City("NSW", "Sydney", "433km2")
c.details()