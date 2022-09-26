import unittest
from four import *

class TestMethods(unittest.TestCase):
    #успешно открыли
    def test1(self):
        self.assertIn(1, arr_b_open)
    #не совсем успешно открыли
    def test2(self):
        self.assertNotIn(1, arr_b_open)
    #успешно сохранили
    def test3(self):
        self.assertIn(1, arr_b_save)
    #не совсем успешно сохранили
    def test4(self):
        self.assertNotIn(1, arr_b_save)
    #успешно записали содержимое файла в текстовое поле(или нет)
    def test5(self):
        self.assertIn(1, arr_text)
    
if __name__ == '__main__':
    unittest.main()