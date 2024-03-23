
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
import unittest
import re


class NumberToThaiTextConvertor():
    digit_names = {1:"", 10:"สิบ",100:"ร้อย",1000:"พัน", 10000: "หมื่น"}
    units_names = {
      0: "ศูนย์", 1: "หนึ่ง", 2: "สอง", 3: "สาม", 4: "สี่", 5: "ห้า",
      6: "หก", 7: "เจ็ด", 8: "แปด", 9: "เก้า"
    }
    replace_suffix_pattern = {r'ศูนย์$':"", r'ศูนย์สิบ':"", r'ศูนย์\D+':"", r'สิบหนึ่ง$':"สิบเอ็ด", r'ร้อยหนึ่ง$':"ร้อยเอ็ด"}
    replace_prefix_pattern = {r'หนึ่งสิบ':"สิบ", r'สอง':"ยี่"}


    def convert(self, number):
        return self.get_thai_text(number)
    
    def get_thai_text(self, input_number):
       thai_text = ""
       str_number = str(input_number)
       
       total_digit = len(str_number)
       count_digit = total_digit
       
       index_str_number = 0
       while count_digit > 0:
            number = int(str_number[index_str_number])           
            if count_digit < 2:
                thai_text += self.get_unit_name(number)
                if total_digit > 1:
                    for pattern,replace in self.replace_suffix_pattern.items():
                        thai_text = re.sub(pattern, replace, thai_text)
            else:
                    if number != 0:
                        thai_text += self.get_unit_name(number)
                        digit = 0.1
                        for i in range(count_digit):
                            digit *= 10
                        thai_text += self.get_digit_name((int(digit)))
                        for pattern,replace in self.replace_prefix_pattern.items():
                            thai_text = re.sub(pattern, replace, thai_text)
                
            count_digit -= 1
            index_str_number += 1

       return thai_text
    
    def get_digit_name (self, number):
       return self.digit_names[number]
    
    def get_unit_name(self, number):
       return self.units_names[number]
    
    def count_digit(self,number): 
        count = 0
        while number != 0: 
            number //= 10
            count += 1
        return count
    
class TestNumberToThaiTextConvertor(unittest.TestCase):
    def setUp(self):
        self.convertor = NumberToThaiTextConvertor()

    def test_0_to_9(self):
        self.assertEqual(self.convertor.convert(0), "ศูนย์")
        self.assertEqual(self.convertor.convert(1), "หนึ่ง")
        self.assertEqual(self.convertor.convert(2), "สอง")
        self.assertEqual(self.convertor.convert(3), "สาม")
        self.assertEqual(self.convertor.convert(4), "สี่")
        self.assertEqual(self.convertor.convert(5), "ห้า")
        self.assertEqual(self.convertor.convert(6), "หก")
        self.assertEqual(self.convertor.convert(7), "เจ็ด")
        self.assertEqual(self.convertor.convert(8), "แปด")
        self.assertEqual(self.convertor.convert(9), "เก้า")
        
    def test_10_to_22(self):
        self.assertEqual(self.convertor.convert(10), "สิบ")
        self.assertEqual(self.convertor.convert(11), "สิบเอ็ด")
        self.assertEqual(self.convertor.convert(12), "สิบสอง")
        self.assertEqual(self.convertor.convert(19), "สิบเก้า")
        self.assertEqual(self.convertor.convert(20), "ยี่สิบ")
        self.assertEqual(self.convertor.convert(21), "ยี่สิบเอ็ด")
        self.assertEqual(self.convertor.convert(22), "ยี่สิบสอง")

    def test_100_101_110_111_120(self):
        self.assertEqual(self.convertor.convert(100), "หนึ่งร้อย")
        self.assertEqual(self.convertor.convert(101), "หนึ่งร้อยเอ็ด")
        self.assertEqual(self.convertor.convert(110), "หนึ่งร้อยสิบ")
        self.assertEqual(self.convertor.convert(111), "หนึ่งร้อยสิบเอ็ด")
        self.assertEqual(self.convertor.convert(120), "หนึ่งร้อยยี่สิบ")
        self.assertEqual(self.convertor.convert(121), "หนึ่งร้อยยี่สิบเอ็ด")
    
    def test_1000_1001_1010_1011_1111_1020_1021_1121(self):
        self.assertEqual(self.convertor.convert(1000), "หนึ่งพัน")
        self.assertEqual(self.convertor.convert(1001), "หนึ่งพันหนึ่ง")
        self.assertEqual(self.convertor.convert(1010), "หนึ่งพันสิบ")
        self.assertEqual(self.convertor.convert(1011), "หนึ่งพันสิบเอ็ด")
        self.assertEqual(self.convertor.convert(1111), "หนึ่งพันหนึ่งร้อยสิบเอ็ด")
        self.assertEqual(self.convertor.convert(1020), "หนึ่งพันยี่สิบ")
        self.assertEqual(self.convertor.convert(1021), "หนึ่งพันยี่สิบเอ็ด")
        self.assertEqual(self.convertor.convert(1121), "หนึ่งพันหนึ่งร้อยยี่สิบเอ็ด")
 
if __name__ == '__main__':
   unittest.main()