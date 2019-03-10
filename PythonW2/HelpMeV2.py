from operator import itemgetter, attrgetter

victims = [('Hùng', 18, 'nam'), ('Lan', 23, 'nữ'),
           ('Lão', 65, 'nam'), ('Bà', 62, 'nữ'), ('Tintin', 8, 'chó'),
           ('Cu', 6, 'nam'), ('Bé', 12, 'nữ')]
child_victims = []
old_victims = []
male_victim = []
female_victim = []
doggo_victim = []

for victim in victims:
    if int(victim[1]) <= 15 and victim[2] != "chó":
        child_victims.append(victim)
    if int(victim[1]) >= 60 and victim[2] != "chó":
        old_victims.append(victim)
    if int(victim[1]) < 60 and int(victim[1]) > 15 and victim[2] == "nam":
        male_victim.append(victim)
    if int(victim[1]) < 60 and int(victim[1]) > 15 and victim[2] == "nữ":
        female_victim.append(victim)
    if (victim[2] == 'chó'):
        doggo_victim.append(victim)
child_victims_sorted = sorted(child_victims, key = itemgetter(1))
print(child_victims)

old_victims_sorted = sorted(old_victims, key = itemgetter(1))
old_victims_sorted.reverse()
print(old_victims)

print(male_victim)
print(female_victim)
print(doggo_victim)
victims_sorted = []
victims_sorted.append(child_victims)
victims_sorted.append(old_victims_sorted)
victims_sorted.append(female_victim)
victims_sorted.append(doggo_victim)
victims_sorted.append(male_victim)
print(victims_sorted)
