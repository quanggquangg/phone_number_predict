import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('D:/KPDL/big_price_test.csv')
df.head(5)

data = pd.DataFrame(df)
vina = [91,94,88,83,84,85,81,82]
mobi = [70,79,77,76,78,89,90,93]
viettel = [86,96,97,98,39,38,32,33,34,35,36,37]
s1 =[]
for i in data['sim_number']:
    check_network = 4
    t = i
    for j in range(9):
        x = i%10
        i = i//10
    i = t
    for j in range(8):
        y = i%10
        i = i//10
    head_number = x * 10 + y
    for a in vina:
        if (head_number) == a:
            check_network = 3
    for a in mobi:
        if (head_number) == a:
            check_network = 2
    for a in viettel:
        if (head_number) == a:
            check_network = 1
    s1.append(check_network)
data['network'] = s1

s2 = []
s3 = []
s4 = []
tam_hoa = ['000','111','222','333','444','555','666','777','888','999']
tu_quy = ['0000','1111','2222','3333','4444','5555','6666','7777','8888','9999']
ngu_quy = ['00000','11111','22222','33333','44444','55555','66666','77777','88888','99999']
tien_3_so = ['012','123','234','345','456','567','678','789']
for i in data['sim_number']:
    t = i
    z = i
    y = i
    three_number = []
    four_number = []
    five_number = []
    check_tam_hoa = 0
    check_tu_quy = 0
    check_ngu_quy = 0
    for j in range(7):
        x = i % 1000
        if x == 0:
            check_tam_hoa = 1
        x = str(x)
        i = i // 10
        three_number.append(x)
    for j in three_number:
        for k in tam_hoa:
            if j == k:
                check_tam_hoa = 1
    s2.append(check_tam_hoa)
    if (check_tam_hoa == 1):
        for j in range(6):
            x = t % 10000
            if x == 0:
                check_tu_quy = 1
            x = str(x)
            t = t // 10
            four_number.append(x)
    for j in four_number:
        for k in tu_quy:
            if j == k:
                check_tu_quy = 1
    s3.append(check_tu_quy)
    if (check_tu_quy == 1):
        for j in range(5):
            x = z % 100000
            if x == 0:
                check_ngu_quy = 1
            x = str(x)
            z = z // 10
            five_number.append(x)
    for j in five_number:
        for k in ngu_quy:
            if j == k:
                check_ngu_quy = 1  
    s4.append(check_ngu_quy)
data['sim_tam_hoa'] = s2
data['sim_tu_quy'] = s3
data['sim_ngu_quy'] = s4

s5 = []
for i in data['sim_number']:
    check_nam_sinh = 0
    x = i % 10000
    if (x > 1900 and x < 2030):
        check_nam_sinh = 1
    s5.append(check_nam_sinh)
data['sim_nam_sinh'] = s5

s6 = []
for i in data['sim_number']:
    check_loc_phat = 0
    x = i % 100
    if (x == 68 or x == 86):
        check_loc_phat = 1
    s6.append(check_loc_phat)
data['sim_loc_phat'] = s6

s7 = []
for i in data['sim_number']:
    check_tien_3_so = 0
    x = i % 1000
    if x < 100:
            x = str(x)
            x = '0' + x
    x = str(x)
    for j in tien_3_so:
        if (x == j) :
            check_tien_3_so = 1
    s7.append(check_tien_3_so)
data['sim_so_tien'] = s7

s8 = []
for i in data['sim_number']:
    check_than_tai = 0
    x = i % 100
    if x == 39 or x == 79:
        check_than_tai = 1
    s8.append(check_than_tai)
data['sim_than_tai'] = s8

s9 = []
s10 = []
s11 = []
s12 = []
for i in data['sim_number']:
    check_sim_lap = 0
    chek_sim_dao = 0
    check_sim_lap_kep = 0
    check_sim_kep = 0
    x = i % 10000
    x1 = x % 100
    x2 = x // 100
    if (x1 == x2):
        check_sim_lap = 1
    if (x1 == 0 or x1 == 11 or x1 == 22 or x1 == 33 or x1 == 44 or x1 == 55 or x1 == 66 or x1 == 77 or x1 == 88 or x1 == 99) and (x2 == 0 or x2 == 11 or x2 == 22 or x2 == 33 or x2 == 44 or x2 == 55 or x2 == 66 or x2 == 77 or x2 == 88 or x2 == 99) :
        check_sim_lap_kep = 1
    soDaoNguoc = 0
    n = x1
    while n > 0:
        chuSoCuoi = n % 10
        soDaoNguoc = soDaoNguoc * 10 + chuSoCuoi
        n = n // 10
    if (soDaoNguoc == x2):
        chek_sim_dao = 1
    if (x1 == 0):
        check_sim_kep = 1
    s10.append(chek_sim_dao)
    s9.append(check_sim_lap)
    s11.append(check_sim_lap_kep)
    s12.append(check_sim_kep)
data['sim_lap'] = s9
data['sim_dao'] = s10
data['sim_lap_kep'] = s11
data['sim_kep'] = s12

s13 = []
for i in data['sim_number']:
    check_lap_ba = 0
    x = i % 1000000
    x1 = x % 1000
    x2 = x // 1000
    if (x1 == x2):
        check_lap_ba = 1
    s13.append(check_lap_ba)
data['sim_lap_ba'] = s13

lui_3_so = ['210','321','432','543','654','765','876','987']
s14 = []
for i in data['sim_number']:
    check_lui_3_so = 0
    x = i % 1000
    x = str(x)
    for j in lui_3_so:
        if (x == j) :
            check_lui_3_so = 1
    s14.append(check_lui_3_so)
data['sim_so_lui'] = s14

s15 = []
for i in data['sim_number']:
    x = i % 10000
    if (x < 10):
        x = str(x)
        x = '000'  + x
    elif (x > 10) and (x < 100):
        x = str(x)
        x = '00'  + x
    elif (x > 100) and (x < 1000):
        x = str(x)
        x = '0'  + x   
    x = str(x)
    s15.append(x)
data['4_so_cuoi'] = s15
print(data)
data.to_csv(r'D:\KPDL\dataset_cleaned_big_test.csv')

# # fig = plt.figure()
# # # Create an axes instance
# # ax = fig.add_axes([0,0,1,1])
# # # Create the boxplot
# # bp = ax.boxplot(df['price_vnd'])
# # plt.show()
# f = data.sort_values(by = ['price_vnd'], ascending=False)
# # Đổi tên index theo thứ tự từ 1 trở đi:
# f.index = range(1,len(df)+1)
# # print(f['price_vnd'][20000])

# # for s in range(len(f['price_vnd'])):
# #     if s == 1:
# #         print(f['price_vnd'][s])




# for i in range(20000):
#     f.drop(labels=i+1, axis= 0)
# print(f)    