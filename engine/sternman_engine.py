from .base_engine import BaseEngine

class SternmanEngine(BaseEngine):
    def __init__(self, warning_light_on: bool):
        super().__init__()
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on
