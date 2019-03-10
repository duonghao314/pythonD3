from operator import itemgetter, attrgetter
victims = [('Hùng', 18, 'nam'), ('Lan', 23, 'nữ'),
           ('Lão', 65, 'nam'), ('Bà', 62, 'nữ'), ('Tintin', 8, 'chó'),
           ('Cu', 6, 'nam'), ('Bé', 12, 'nữ')]
print(victims) #in danh sách bệnh nhân ban đầu
list_sorted_by_old = sorted(victims,key = itemgetter(1)) #sắp xếp theo tuổi tăng dần
list_sorted_by_old.reverse() #đảo ngược danh sách
print(list_sorted_by_old)

dog_victims = [] #tạo danh sách "chó"
#kiểm tra nếu là "chó" thì xóa và đưa vào danh sách "chó"
for victim in victims:
    if victim[2] == 'chó':
        dog_victims.append(victim)
        victims.remove(victim)
#sắp xếp danh sách "Chó" theo tuổi
list_dog_sorted_by_old = sorted(dog_victims, key = itemgetter(1))
list_dog_sorted_by_old.reverse()

#Thêm danh sách chó vào sau danh sách bệnh nhân
victims.append(list_dog_sorted_by_old)
list_sorted_by_old_and_doggo = victims
#Kết quả
print(list_sorted_by_old_and_doggo)