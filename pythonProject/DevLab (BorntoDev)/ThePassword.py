'''
 password โดยมีเงื่อนไขว่าต้องมีตัวอักษรอย่างน้อย 3 ตัวอักษร และไม่เกิน 20 ตัวอักษร
โดยจะต้องมีอักษรพิมพ์ใหญ่อย่างน้อย 1 ตัวอักษร ตัวพิมพ์เล็กอย่างน้อย 1 ตัวอักษร ตัวเลขอย่างน้อย 1 ตัวอักษร และสัญลักษณ์
อย่างน้อย 1 ตัวอักษร หาสามารถใช้ได้ให้แสดงค่า Valid และไม่ครบเงื่อนไขให้ใช้ค่า Invalid
'''
message = input()
if 20 >= len(message) >= 3:
    listUpper = []
    listLower = []
    listNumber = []
    listSign = []
    for c in message:
        if c.isupper():
            listUpper.append(c)
        elif c.islower():
            listLower.append(c)
        elif c.isdigit():
            listNumber.append(c)
        else:
            listSign.append(c)

    if len(listUpper) >= 1:
        if len(listLower) >= 1:
            if len(listNumber) >= 1:
                if len(listSign) >= 1:
                    print("Valid")
                else:
                    print('Invalid')
            else:
                print('Invalid')
        else:
            print('Invalid')
else:
    print('Invalid')