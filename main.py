f = open("input.txt")
id_ranges = f.read().split(",")
count = 0

for id_range in id_ranges:
 limits = id_range.split("-")

 for i in range(int(limits[0]), int(limits[1]) + 1):
  i_str = str(i)
  lengthNum = len(i_str) 
  if i_str[0:lengthNum//2] == i_str[lengthNum//2:lengthNum]:
   count += i

print(f"Nombre de ID supprimer : {count}")
