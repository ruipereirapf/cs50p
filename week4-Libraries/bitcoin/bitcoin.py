import sys
import requests
import json

def main():
    number_of_bitcoin = check_command_line_arguments()

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
         sys.exit("Error doing the request")

    ##will print the API data indented
    #print(json.dumps(response.json(), indent=2))

    bitcoin_data = response.json()

    # Same as line #23
    #bpi = bitcoin_data["bpi"]
    #usd = bpi["USD"]
    #rate_float = usd["rate_float"]

    bitcoin_rate = bitcoin_data["bpi"]["USD"]["rate_float"]
    amount = number_of_bitcoin * bitcoin_rate

    print(f"${amount:,.4f}")

#checks if the arguments given in the command line are valid
def check_command_line_arguments():
    if len(sys.argv) == 2:
        try:
            return float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
            sys.exit("Missing command-line argument")



if __name__ == "__main__":
    main()