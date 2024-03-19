def main():
    menu ={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    total = 0
    total = get_input("Item: ", menu, total)


def get_input(prompt, menu, total):
     while True:
            try:
                item_inputed = input(prompt).title()
                if item_inputed in menu:
                    #print(f"Valor Item: {menu[item_inputed]}")
                    total += menu[item_inputed]
                    print(f"Total: ${total:.2f}")
            except KeyboardInterrupt:
                 return total
            except EOFError:
                 return total

main()