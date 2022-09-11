chick1, chick2, chick3, chick4, chick5 = 'สมพงศ์', 'ไก๊...ไก่', 'ไอ้ปืด', 'จิม', 'วิฆูล'
wFood = 40
chickhenW = 3.45
eF = int(input('food :'))

if eF == 50:
    layC = 'ออกไข่ 1 ฟอง'
    print(chick1, 'กิน', eF, 'g', 'โดยมีน้ำหนักตัวอยู่ที่', chickhenW, 'Kg', layC)
elif eF == 100:
    layC = 'ออกไข่ 2 ฟอง'
    print(chick1, 'กิน', eF, 'g', 'โดยมีน้ำหนักตัวอยู่ที่', chickhenW, 'Kg', layC)
elif eF == 150:
    layC = 'ออกไข่ 3 ฟอง'
    print(chick1, 'กิน', eF, 'g', 'โดยมีน้ำหนักตัวอยู่ที่', chickhenW, 'Kg', layC)
else :
    layC = 'ไม่ออกไข่'
    print(chick1, 'กิน', eF, 'g', 'โดยมีน้ำหนักตัวอยู่ที่', chickhenW, 'Kg', layC)

