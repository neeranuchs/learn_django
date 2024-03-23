'''

2.เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4] 
ลำดับที่มีค่ามากที่สุด คือ index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข

'''

array_input = [1,6,1,3,5,6,4]

max_value = -1
array_max_value_indexes = []
for i in range(len(array_input)):
    if array_input[i] > max_value:
        max_value = array_input[i]

for j in range(len(array_input)):
    if array_input[j] == max_value:
        array_max_value_indexes.append(j)

print(array_max_value_indexes)
