from abc import ABC, abstractmethod

# Интерфейс OldService с методом fetch_data(), который возвращает данные в старом формате
class OldService:
    @abstractmethod
    def fetch_data(self):
        pass

# Интерфейс NewService с методом get_data(), который возвращает данные в новом формате
class NewService:
    @abstractmethod
    def get_data(self):
        pass

# Реализация OldService
class OldServiceImpl(OldService):
    def fetch_data(self):
        # Возвращаем данные в старом формате
        return "Old Data Format"

# Адаптер, который адаптирует OldService к NewService
class ServiceAdapter(NewService):
    def __init__(self, old_service: OldService):
        # Принимаем объект OldService
        self.old_service = old_service

    def get_data(self):
        # Адаптируем старый формат данных к новому
        old_data = self.old_service.fetch_data()
        return f"Adapted: {old_data}"

#пример использования кода
if __name__ == "__main__":
    old_service = OldServiceImpl()

    # Создаем адаптер, передавая ему OldService
    adapter = ServiceAdapter(old_service)

    # Используем адаптер для получения данных в новом формате
    new_data = adapter.get_data()
    print(new_data)  