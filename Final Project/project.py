"""
Project: River Characteristics for Canyoning and Weather Information
Name: Rui Pereira
From: Braga, Portugal
"""


import csv, os, requests, re


class City:
    all = []

    def __init__(self, id: int, name: str):
        # Assign to self object
        self._id = id
        self._name = name

        # Appends each instance to the "all" list
        City.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open("csvs/cities.csv", "r") as file:
            reader = csv.DictReader(file)
            cities = list(reader)

        for city in cities:
            City(id=int(city.get("id")), name=city.get("name"))

    def __repr__(self):
        return f"{self.id},{self.name}"

    # Getter
    @property
    def name(self):
        return self._name

    # Getter
    @property
    def id(self):
        return self._id


class River:
    all = []

    def __init__(
        self, id, name, start_coord, end_coord, length, highest_rappel, croqui
    ):
        # Assign to self object
        self._id = id
        self._name = name
        self._start_coord = start_coord
        self._end_coord = end_coord
        self._length = length
        self._highest_rappel = highest_rappel
        self._croqui = croqui

        # Appends each instance to the 'all' list
        River.all.append(self)

    @classmethod
    def instantiate_from_csv(cls, prompt):
        for row in City.all:
            if row.id == prompt:
                city_name = str(row.name)

        path = f"csvs/{city_name.lower().replace(' ','_')}_rivers.csv"
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            rivers = list(reader)

        for river in rivers:
            River(
                id=int(river.get("id")),
                name=river.get("name"),
                start_coord=river.get("start_coord"),
                end_coord=river.get("end_coord"),
                length=river.get("length"),
                highest_rappel=river.get("highest_rappel"),
                croqui=river.get("croqui"),
            )

    def __repr__(self):
        return f"{self._id},{self._name},{self._start_coord},{self._end_coord},{self._length},{self._highest_rappel},{self._croqui}"

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def start_coord(self):
        return self._start_coord

    @property
    def end_coord(self):
        return self._end_coord

    @property
    def length(self):
        return self._length

    @property
    def highest_rappel(self):
        return self._highest_rappel

    @property
    def croqui(self):
        return self._croqui


class Weather:
    all_weather_data = []

    def __init__(
        self,
        temp,
        tempmax,
        tempmin,
        precipprob,
        windspeed,
        sunrise,
        sunset,
        cloudcover,
        description,
    ):
        # Assign to self object
        self._temp = temp
        self._tempmax = tempmax
        self._tempmin = tempmin
        self._precipprob = precipprob
        self._windspeed = windspeed
        self._sunrise = sunrise
        self._sunset = sunset
        self._cloudcover = cloudcover
        self._description = description

        # Appends each instance to the "all" list
        Weather.all_weather_data.append(self)

    def __repr__(self):
        return f"{self._temp},{self._tempmax},{self._tempmin},{self._precipprob},{self._windspeed},{self._sunrise},{self._sunset}"

    @classmethod
    def instantiate_from_request(cls, latitude, longitude):
        visualcrossing_api_key = "N3BLZ9X4MHZ7ELLF7PXEAKA6L"
        response = requests.get(
            f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{latitude},{longitude}/today?key={visualcrossing_api_key}&unitGroup=metric&include=obs&elements=tempmax,tempmin,temp,precipprob,windspeed,sunrise,sunset,cloudcover,description"
        )
        weather_data = response.json()

        Weather(
            temp=weather_data["days"][0]["temp"],
            tempmax=weather_data["days"][0]["tempmax"],
            tempmin=weather_data["days"][0]["tempmin"],
            precipprob=weather_data["days"][0]["precipprob"],
            windspeed=weather_data["days"][0]["windspeed"],
            sunrise=weather_data["days"][0]["sunrise"],
            sunset=weather_data["days"][0]["sunset"],
            cloudcover=weather_data["days"][0]["cloudcover"],
            description=weather_data["days"][0]["description"],
        )

    @property
    def temp(self):
        return self._temp

    @property
    def tempmax(self):
        return self._tempmax

    @property
    def tempmin(self):
        return self._tempmin

    @property
    def precipprob(self):
        return self._precipprob

    @property
    def windspeed(self):
        return self._windspeed

    @property
    def sunrise(self):
        return self._sunrise

    @property
    def sunset(self):
        return self._sunset

    @property
    def cloudcover(self):
        return self._cloudcover

    @property
    def description(self):
        return self._description


def main():
    # Instantiates the cities from the cities file
    City.instantiate_from_csv()
    cities = City.all

    print("----------------------------------")
    print("|        Available Cities        |")
    print("----------------------------------")
    # prints the list of cities from 'cities.csv'
    for row in cities:
        print(f"{row.id} - {row.name}")

    # Gets user prompt and checks if the input is valid
    city_prompt = get_prompt()
    city_prompt = int(check_prompt(city_prompt, City))

    # Instantiates the rivers from the city file
    River.instantiate_from_csv(city_prompt)
    rivers = River.all

    clear_terminal()
    # Prints the list of rivers in the ''city'_rivers.csv'
    print("----------------------------------")
    print("|        Available Rivers        |")
    print("----------------------------------")
    for row in rivers:
        print(f"{row.id} - {row.name}")

    # Gets user prompt and check if the input is valid
    river_prompt = get_prompt()
    river_prompt = check_prompt(river_prompt, River)

    answer = want_weather()
    if check_need_weather(answer) == True:
        # Clears terminal before listing
        clear_terminal()
        latitude, longitude = list_river_info(rivers, river_prompt)

        # Instantiates the weather info
        Weather.instantiate_from_request(str(latitude), str(longitude))
        weather = Weather.all_weather_data

        list_weather_info(weather)

    elif check_need_weather(answer.lower()) == False:
        # Clears terminal before listing
        clear_terminal()
        list_river_info(rivers, river_prompt)


# Clears terminal screen
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Gets the input from the user
def get_prompt():
    return input("Choose a number: ")


# Gets the highest 'id' value given from the 'all' list from the passed object (class) in the 2nd argument
# And tests if the inputed value is within the values of that list in order to validate
def check_prompt(prompt, object):
    max_id = 0
    for obj in object.all:
        if obj.id > max_id:
            max_id = int(obj.id)
    while True:
        try:
            if prompt.isdigit() and 1 <= int(prompt) <= max_id:
                return prompt
            else:
                raise ValueError("Please enter a valid integer.")
        except ValueError as ve:
            print(ve)
            prompt = input("Choose a Number: ")


# Receives a coordinate and divides it in latitude and longitude
def get_latitude_longitude(coord):
    try:
        if matches:= re.search(r"^[-+]?[0-9]*\.?[0-9]+,\s*[-+]?[0-9]*\.?[0-9]+$", coord):
            latitude, longitude = matches.group().split(",")
            return latitude.strip(), longitude.strip()
        else:
            raise ValueError
    except ValueError:
        raise ValueError("Invalid received format")


# Asks user if he wants to receive weather data
def want_weather():
    return input("Do you want to receive Weather Information (Y/N):")


# Checks need_weather input
def check_need_weather(answer):
    answer = answer.lower()
    while True:
        if answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        else:
            answer = want_weather()


# Lists river information
def list_river_info(rivers, river_prompt):
    # prints all the selected river info
    for river in rivers:
        if river.id == int(river_prompt):
            print("-----RIVER INFO-----\n")
            print(f"River Name: {river.name}")
            print(f"Start: {river.start_coord}")
            print(f"End: {river.end_coord}")
            print(f"Length: {river.length}")
            print(f"Highest Rappel: {river.highest_rappel}")
            print(f"Croqui: {river.croqui}")
            print("WARNING: Some croquis may only be in portuguese.")
            latitude, longitude = get_latitude_longitude(river.start_coord)
            return latitude, longitude


# Lists weather information
def list_weather_info(weather):
    # Prints all weather info
    print("\n-----Weather Info-----\n")
    for condition in weather:
        print(f"Weather Description: {condition.description}")
        print(f"Current Temperature: {condition.temp}°C")
        print(f"Maximum Temperature: {condition.tempmax}°C")
        print(f"Minimum Temperature: {condition.tempmin}°C")
        if condition.precipprob.is_integer():
            print(f"Precipitation Chance: {int(condition.precipprob)}%")
        else:
            print(f"Precipitation Chance: {condition.precipprob}%")
        if condition.cloudcover == None:
            print(f"Cloud Coverage: 0%")
        else:
            print(f"Cloud Coverage: {condition.cloudcover}%")
        print(f"Windspeed: {condition.windspeed} km/h")
        print(f"Sunrise: {condition.sunrise}")
        print(f"Sunset: {condition.sunset}")


if __name__ == "__main__":
    main()
