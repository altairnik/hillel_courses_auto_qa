class Romb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == 'side_a':

            if value <= 0:
                raise ValueError("Довжина сторони повинна бути більше 0")

        elif name == 'angle_a':

            if not (0 < value < 180):
                raise ValueError("Кут повинен бути в межах від 0 до 180 градусів")

            super().__setattr__('angle_b', 180 - value)

        elif name == 'angle_b':
            raise AttributeError("Значення кута обчислюється автоматично")

        super().__setattr__(name, value)

    def __str__(self):
        return f"Ромб: сторона a = {self.side_a}, кут_а = {self.angle_a}°, кут_б = {self.angle_b}°"


try:
    rhombus = Romb(10, 60)
    print(rhombus)

    rhombus.angle_a = 45
    print(rhombus)

except ValueError as e:
    print("Помилка:", e)
except AttributeError as e:
    print("Помилка:", e)