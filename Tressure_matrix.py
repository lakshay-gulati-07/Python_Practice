row1 = [" ⬜️ "," ⬜️ "," ⬜️ "]
row2 = [" ⬜️ "," ⬜️ "," ⬜️ "]
row3 = [" ⬜️ "," ⬜️ "," ⬜️ "]
map = [row1,row2,row3]
print(f"{row1} \n{row2} \n{row3}")
position = input("Where you want to put tressure ?? ")
row = int(position[0])
coloumn = int(position[1])
map[row-1][coloumn-1] = "X"
print(f"\n{row1}\n{row2}\n{row3}")