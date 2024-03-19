grocery_list = []
grocery_dict = {}

while True:
    try:
        item = input("").upper()
        grocery_list.append(item)
        grocery_list.sort()
    except EOFError:
        break
    except KeyboardInterrupt:
        break

for word in grocery_list:
    if word in grocery_dict:
        grocery_dict[word] += 1
    else:
        grocery_dict[word] = 1

for item in grocery_dict:
    print(grocery_dict[item], item)