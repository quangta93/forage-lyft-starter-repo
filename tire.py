class Tire:
  def needs_service() -> bool:
    pass

class CarriganTire(Tire):
  def __init__(self, values: list[float]) -> None:
    super().__init__()
    self.values =values 

  def needs_service(self) -> bool:
    for val in self.values:
      if val >= 0.9:
        return True
    return False

class OctoprimeTire(Tire):
  def __init__(self, values: list[float]) -> None:
    super().__init__()
    self.values = values

  def needs_service(self) -> bool:
    return sum(self.values) >= 3.0