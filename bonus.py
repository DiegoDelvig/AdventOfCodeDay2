
"""
Si "101010" = s
on fait s + s
puis on enlève le premier et le dernier caractère
on cherche si "101010" est dans le résultat
"""

f = open("input.txt")
id_ranges = f.read().split(",")
count = 0

for id_range in id_ranges:
 limits = id_range.split("-")

 for i in range(int(limits[0]), int(limits[1]) + 1):
  i_str = str(i)
  doubleI_str = i_str + i_str
  modified_i_str = doubleI_str[1:-1]
  if i_str in modified_i_str:
    count += i 

print(f"Nombre de ID supprimer : {count}")
