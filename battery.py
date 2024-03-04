from datetime import date, timedelta

class BaseBattery:
  def needs_service() -> bool:
    pass

def add_n_years(current: date, num_years: int):
  if (current.month == 2) and (current.day == 29):
    return current.replace(year=current.year+num_years,
                           month=current.month+1,
                           day=1)
  return current.replace(year=current.year+num_years)

class SpindlerBattery(BaseBattery):
  def __init__(self,
               last_service_date: date,
               current_date: date) -> None:
    super().__init__()
    self.last_service_date = last_service_date
    self.current_date = current_date

  def needs_service(self) -> bool:
    return add_n_years(self.last_service_date, 2) < self.current_date

class NubbinBattery(BaseBattery):
  def __init__(self,
               last_service_date: date,
               current_date: date) -> None:
    super().__init__()
    self.last_service_date = last_service_date
    self.current_date = current_date

  def needs_service(self) -> bool:
    return add_n_years(self.last_service_date, 4) < self.current_date