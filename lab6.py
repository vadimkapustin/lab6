class Building:
    """Базовый класс Здание"""
    
    objects_count = 0
    
    def __init__(self, name, area, price_per_sqm, residents_count):
        '''
        name - название здания
        area - площадь в кв. метрах
        price_per_sqm - стоимость 1 кв. метра в рублях
        residents_count - количество проживающих
        '''
        self._name = name
        self.set_area(area)
        self.set_price_per_sqm(price_per_sqm)
        self.set_residents_count(residents_count)
        Building.objects_count += 1
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_area(self):
        return self._area
    
    def set_area(self, area):
        if area > 0:
            self._area = area
        else:
            self._area = 1
    
    def get_price_per_sqm(self):
        return self._price_per_sqm
    
    def set_price_per_sqm(self, price):
        if price >= 0:
            self._price_per_sqm = price
        else:
            self._price_per_sqm = 0
    
    def get_residents_count(self):
        return self._residents_count
    
    def set_residents_count(self, count):
        if count >= 0:
            self._residents_count = count
        else:
            self._residents_count = 0
    
    def calculate_total_cost(self):
        total_cost = self._area * self._price_per_sqm
        return total_cost
    
    def cost_per_resident_ratio(self):
        if self._residents_count > 0:
            total_cost = self.calculate_total_cost()
            ratio = total_cost / self._residents_count
            return ratio
        else:
            return float('inf')  # Бесконечность, если никто не живет
    
    def display_info(self):
        print(f"\n Информация о здании: ")
        print(f"Название: {self._name}")
        print(f"Площадь: {self._area} кв.м")
        print(f"Стоимость за кв.м: {self._price_per_sqm} руб.")
        print(f"Количество проживающих: {self._residents_count}")
        print(f"Общая стоимость: {self.calculate_total_cost():.2f} руб.")
        print(f"Соотношение стоимости к числу проживающих: {self.cost_per_resident_ratio():.2f} руб./чел.")


class CountryHouse(Building):
    
    def __init__(self, name, area, price_per_sqm, residents_count, land_area):
        """
        land_area - площадь земельного участка в кв.м (уникальное поле)
        """
        super().__init__(name, area, price_per_sqm, residents_count)
        self.set_land_area(land_area)
    
    def set_land_area(self, land_area):
        if land_area >= 0:
            self._land_area = land_area
        else:
            self._land_area = 0
    
    def get_land_area(self):
        return self._land_area
    
    def calculate_total_cost(self):
        """
        стоимость дома + стоимость земельного участка
        (стоимость земли принимаем как 30% от стоимости за кв.м дома)
        """
        house_cost = self.get_area() * self.get_price_per_sqm()
        land_cost = self._land_area * self.get_price_per_sqm() * 0.3
        return house_cost + land_cost
    
    def cost_per_resident_ratio(self):
        if self.get_residents_count() > 0:
            return self.calculate_total_cost() / self.get_residents_count()
        else:
            return float('inf')
    
    def display_info(self):
        super().display_info()
        print(f"Тип: Деревенский дом")
        print(f"Площадь участка: {self._land_area} кв.м")

class ApartmentBuilding(Building):
    
    def __init__(self, name, area, price_per_sqm, residents_count, has_parking):
        """
        has_parking - наличие парковки (уникальное поле)
        """
        super().__init__(name, area, price_per_sqm, residents_count)
        self.has_parking = has_parking
    
    def calculate_total_cost(self):
        # бонус от парковки
        base_cost = self.get_area() * self.get_price_per_sqm()
        parking_bonus = 1.1 if self.has_parking else 1.0
        total_cost = base_cost * parking_bonus
        return total_cost
    
    def cost_per_resident_ratio(self):
        if self.get_residents_count() > 0:
            total_cost = self.calculate_total_cost()
            return total_cost / self.get_residents_count()
        else:
            return float('inf')
    
    def display_info(self):
        super().display_info()
        print(f"Тип: Многоквартирный городской дом")
        print(f"Наличие парковки: {'Да' if self.has_parking else 'Нет'}")


# Демонстрация работы программы
def main():
    
    # Базовый класс Building
    building1 = Building("Офисное здание", 500, 80000, 50)
    
    # Класс CountryHouse
    country_house1 = CountryHouse("Дом в деревне", 120, 50000, 4, 1000)
    country_house2 = CountryHouse("Дачный домик", 80, 30000, 2, 600)
    
    # Класс ApartmentBuilding
    apartment1 = ApartmentBuilding("ЖК 'Солнечный'", 2000, 120000, 150, True)
    apartment2 = ApartmentBuilding("Старый дом", 800, 70000, 80, False)
    
    # Вывод информации о всех объектах
    print("\n Информация о всех созданных зданиях:")
    
    buildings = [building1, country_house1, country_house2, apartment1, apartment2]
    
    for i, building in enumerate(buildings, 1):
        print(f"\n Здание #{i}")
        building.display_info()
    
    print(f"\n Общее количество созданных объектов: {Building.objects_count}")


main()