from datetime import date
from engine.base_engine import BaseEngine
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery import SpindlerBattery, NubbinBattery, BaseBattery

class Servicable:
   def needs_service() -> bool:
      pass

class Car(Servicable):
    def __init__(self, engine: BaseEngine, battery: BaseBattery):
        self.engine = engine 
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()

class CarFactory:
  def create_calliope(current_date: date,
                      last_service_date: date,
                      current_mileage: int,
                      last_service_mileage: int) -> Car:
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, date.today())
    return Car(engine, battery)

  def create_glissade(current_date: date,
                      last_service_date: date,
                      current_mileage: int,
                      last_service_mileage: int) -> Car:
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, date.today())
    return Car(engine, battery)

  def create_palindrome(current_date: date,
                        last_service_date: date,
                        warning_light_on: bool) -> Car:
    engine = SternmanEngine(warning_light_on)
    battery = SpindlerBattery(last_service_date, date.today())
    return Car(engine, battery)

  def create_rorschach(current_date: date,
                       last_service_date: date,
                       current_mileage: int,
                       last_service_mileage: int) -> Car:
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(last_service_date, date.today())
    return Car(engine, battery)

  def create_thovex(current_date: date,
                    last_service_date: date,
                    current_mileage: int,
                    last_service_mileage: int) -> Car:
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(last_service_date, date.today())
    return Car(engine, battery)

first_car = CarFactory.create_calliope(current_date=date.today(),
                           last_service_date=date.today(),
                           current_mileage=34002,
                           last_service_mileage=0)
print(first_car.needs_service())