# write test cases for the classes in classes.py
import unittest
import classes
import random
import string

class TestClasses(unittest.TestCase):

    def test_Car(self):
        car = classes.Car("Toyota", "Corolla", 2020, "black")
        self.assertEqual(car.make, "Toyota")
        self.assertEqual(car.model, "Corolla")
        self.assertEqual(car.year, 2020)
        self.assertEqual(car.color, "black")
        self.assertEqual(car.speed, 0)
        self.assertEqual(car.is_engine_on, False)
        self.assertEqual(car.is_moving, False)
        self.assertEqual(car.is_parked, True)

        car.start_engine()
        self.assertEqual(car.is_engine_on, True)
        self.assertEqual(car.is_moving, False)
        self.assertEqual(car.is_parked, False)

        car.accelerate(50)
        self.assertEqual(car.speed, 50)
        self.assertEqual(car.is_moving, True)
        self.assertEqual(car.is_parked, False)

        car.accelerate(100)
        self.assertEqual(car.speed, 100)

        car.decelerate(50)
        self.assertEqual(car.speed, 50)

        car.stop_engine()
        self.assertEqual(car.is_engine_on, False)
        self.assertEqual(car.is_moving, False)
        self.assertEqual(car.is_parked, True)

    def test_Person(self):
        pass
    
    