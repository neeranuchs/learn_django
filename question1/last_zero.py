'''

3.เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python 
โดยห้ามใช้ math.factorial เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว

'''
import re

input = 7

int_result_factorial = 1
for i in range(1,input+1):
    int_result_factorial = int_result_factorial*i

str_result_factorial = str(int_result_factorial)
print(input,"! =", str_result_factorial)


x = re.search("0+$", str_result_factorial)
num_last_zero = 0
if x is not None:
    num_last_zero = x.end() - x.start()
print("Number of zero:", num_last_zero)

