poles = 20
if poles >= 30:
    print("true")
elif poles <= 30:
    print("false")
else:
    print("invalid")

#simp = "am sorry"
#for i in range(3):
#    print(simp)

simp=1
while simp<=3:
  #  print("simp")
    simp+=1

players = ["ronaldo","messi","rashford","haaland"]
player_wanted = "haaland"
for player in players:

    if player == player_wanted:
        print("I wanted the goat")
        break
   # print(player)

countries = ["kenya","spain","morocco","italy"]
contry_wanted = "kenya"

length = len(countries)
count = 0
while count < length:
    print(countries[count])
    if countries[count] == contry_wanted:
   #     print("i wanted this country")
        break
    count+=1

ages = [23,16,65]
for age in ages:
    if age < 20:
        continue
  #  print(age)

nums = [3,-11,23,-65]
doubled = []
for num in nums:
    doubled.append(num*2)
    print(doubled)

#list compression
nums1 = [2,5,2,-5]
doubled = [num*2 for num in nums1]
print(doubled)