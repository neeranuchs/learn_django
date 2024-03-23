
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

import unittest

class ArabicNumberToRomanNumberConvertor():
   all_units = [10,5,1]
   def convert(self, input_arabic_number):
      output_roman_list = []
      output_roman_number = ""
      lowest_unit_index = 0
      # largest_unit_index = self.get_largest_unit_index(input_arabic_number)
      # lowest_unit = self.units[lowest_unit_index]
      # largest_unit = self.units[largest_unit_index]
      units = self.get_unit(input_arabic_number)
      remain = input_arabic_number
      while remain > 0:
         for unit in units:
            if remain % unit == 0:
               # output_roman_number = self.get_roman_char(unit)
               output_roman_list.append(self.get_roman_char(unit))
            else:
               output_roman_list.append(self.get_roman_char(unit))
            # elif remain == unit-1:
               # output_roman_number = self.get_roman_char(unit) + self.get_roman_char(unit)
            # else:
               # output_roman_number = output_roman_number + self.get_roman_char(unit)
            remain = remain - unit
     
      return "".join(output_roman_list)       
   
   #  unit_V = 5
   #  unit_I = 1
   #  remain_I = input_arabic_number % unit_V
   #  if remain_I == 0:
   #     result = self.get_roman_char(unit_V)
   #  elif remain_I == unit_V-unit_I:
   #     result = self.get_roman_char(unit_I) + self.get_roman_char(unit_V)
   #  else:
   #  #remain_I > 0 and remain_I <= 5-2:
   #      i = 1
   #      while i <= remain_I:
   #          result = result + self.get_roman_char(unit_I)
   #          i = i+unit_I
   #          remain_I - unit_I
   #  return result
   
   def get_unit(self, input_arabic_number):
      units = []
      for i in range(len(self.all_units)):
         unit = self.all_units[i]
         if input_arabic_number % unit == 0:
            units.append(unit)
            break

         if unit - input_arabic_number == 1:
            units.append(unit)
            continue
         if input_arabic_number > unit and input_arabic_number - unit <=3:
            units.append(unit)
            break
         

         # elif (unit - remain) == 1:
         #    units.append(unit)
         #    break
         # elif remain % unit > 0 and unit < remain:
         #    units.append(unit)
         #    break
         #    if unit - input_arabic_number <= 3:
         #       units.append(unit)
         # if input_arabic_number % unit > 0 and unit - input_arabic_number == 1:
         #    units.append(unit)
         # remain = remain - unit
         # units.append(unit)
      return units
 
   def get_roman_char(self, arabic_number):
      if arabic_number == 10:
         return "X"
      if arabic_number == 5:
         return "V"
      # if remain == 1:
      return "I"
      # return ""
 
class TestArabicNumberToRomanNumberConvertor(unittest.TestCase):
   def setUp(self):
      self.convertor = ArabicNumberToRomanNumberConvertor()
   def test_1_to_5(self):
      self.assertEqual(self.convertor.convert(1), "I")
      self.assertEqual(self.convertor.convert(2), "II")
      self.assertEqual(self.convertor.convert(3), "III")
      self.assertEqual(self.convertor.convert(4), "IV")
      self.assertEqual(self.convertor.convert(5), "V")
   
   def test_6_to_10(self):
      self.assertEqual(self.convertor.convert(6), "VI")
      self.assertEqual(self.convertor.convert(7), "VII")
      self.assertEqual(self.convertor.convert(8), "VIII")
      self.assertEqual(self.convertor.convert(9), "IX")
      self.assertEqual(self.convertor.convert(10), "X")
 
if __name__ == '__main__':
   unittest.main()