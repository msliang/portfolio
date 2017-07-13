groceries= ["carrots","chips","pasta","cheese","cereal"]
drinks=["juice","milk","soda"]
print(groceries[len(groceries)-1])
print(len(groceries))
groceries.append("coffee")
groceries.extend(drinks)
for item in groceries:
    print(str(groceries.index(item)+1)+":"+item)
