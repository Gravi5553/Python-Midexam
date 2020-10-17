import re
import urllib.request
import json

api_end_point = "https://api.exchangerate-api.com/v4/latest/USD"
# reg ex for input validation of currency code that it accepts only three capital letters
regexp = re.compile(r'\b[A-Z]{3}\b')


# checking whether the page exists or not
def page_exists(page):
    try:
        urllib.request.urlopen(page)
        return True
    except:
        return False


# making api call call and calculating currency
def currencyAPICall(amount, from_curr, to_curr):
    if page_exists(api_end_point):
        page = urllib.request.urlopen(api_end_point)
        content = page.read().decode("utf-8")  # keep in mind the byte string needs to be decoded
        data = json.loads(content)
        if data:
            curr_rates = data["rates"]
            if from_curr != "USD":
                if to_curr not in curr_rates:
                    print("One or more currency code not found")
                    main()
                else:
                    print("From currency code not found")
                    main()
            elif to_curr not in curr_rates:
                print("TO currency code not found")
                main()
            else:
                converted_curr = float(curr_rates[to_curr])
                calculated_amount = converted_curr * float(amount)
                print(str(float(amount)) + " in " + from_curr + " = " + str(calculated_amount) + " in " + to_curr)
    else:
        print("ERROR: invalid APT endpoint")


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# validation for user input
def validateUserInput(user_input):
    if not isfloat(user_input):
        print("invalid amount " + user_input)
        main()


# function for validating from currency
def validateFromCurrency(curr):
    if not regexp.search(curr):
        print("invalid currency code " + curr)
        main()


# function or validating to currency
def validateToCurrency(curr):
    if not regexp.search(curr):
        print("invalid currency code " + curr)
        main()


def main():
    while True:
        user_input = input("Enter amount to be converted(q to quit):")
        if user_input == 'q' or user_input == 'Q':
            print("Exiting")
            break
        validateUserInput(user_input)

        from_curr = input("Enter FROM currency 3 letter code:")
        validateFromCurrency(from_curr)
        to_curr = input("Enter TO currency 3 letter code:")
        validateToCurrency(to_curr)
        currencyAPICall(user_input, from_curr, to_curr)


if __name__ == '__main__':
    main()
