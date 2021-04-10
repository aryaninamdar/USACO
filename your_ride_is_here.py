inn = open ('ride.in', 'r')
lines = inn.readlines()
lines = [x.strip() for x in lines] 
out = open ('ride.out', 'w')
comet_name = lines[0]
group_name = lines[1]

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

comet_sum = 1
for letter in comet_name:
  comet_num = alphabet_list.index(letter) + 1
  comet_sum *= comet_num

group_sum = 1
for letter in group_name:
  group_num = alphabet_list.index(letter) + 1
  group_sum *= group_num

if (comet_sum % 47 == group_sum % 47):
  out.write ('GO\n')
  out.close()
else:
  out.write ('STAY\n')
  out.close()
