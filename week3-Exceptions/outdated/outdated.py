months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date_input = input("Date: ").strip()
        if "/" in date_input:
            month, day, year = date_input.split("/")

            month = int(month)
            day = int(day)

            if 1 <= day <= 31 and 1 <= month <= 12:
                month = str(month)
                day = str(day)
                month = month.zfill(2)
                day = day.zfill(2)
                print(f"{year}-{month}-{day}", end="")
                break

            else:
                continue

        elif "," in date_input:
            month, day, year = date_input.replace(",", "").split(" ")

            if month not in months_list:
                continue
            else:
                month_in_number = months_list.index(month.title())
                day = int(day)

                if 1 <= day <= 31 and 1 <= month_in_number <= 12:
                    month, day, year = date_input.replace(",", "").split(" ")

                    if month.title() in months_list:
                        month_index = months_list.index(month.title())
                        month_index += 1
                        month_index = str(month_index)
                        month_index = month_index.zfill(2)
                        day = day.zfill(2)

                        if len(month_index) <= 1 and len(day) <=1:
                            print(f"{year}-{month_index}-{day}", end="")
                            break
                        else:
                            print(f"{year}-{month_index}-{day}", end="")
                            break
                    else:
                        continue
                else:
                    continue

    except EOFError:
        continue
    except KeyboardInterrupt:
        break
    except ValueError:
        continue