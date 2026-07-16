shop = int(input("บอสสั่งเก็บส่วย"))
kapook = 0
for i in range(1,shop+1):
    monny = float(input(f"ร้าน {i} ได้เท่าไหร่"))
    kapook += monny
print(kapook)

