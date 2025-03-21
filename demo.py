# Function to convert USD to other currencies
def USD(amount, target):
    if target == 'CAD':
        return amount * 1.4280
    elif target == 'EURO':
        return amount * 0.9177
    elif target == 'USD':
        return amount
    else:
        return None


# Function to convert CAD to other currencies
def CAD(amount, target):
    if target == 'USD':
        return amount * 0.6981
    elif target == 'EURO':
        return amount * 0.6398
    elif target == 'CAD':
        return amount
    else:
        return None


# Function to convert EURO to other currencies
def EURO(amount, target):
    if target == 'USD':
        return amount * 1.0922
    elif target == 'CAD':
        return amount * 1.5628
    elif target == 'EURO':
        return amount
    else:
        return None


# Main program
try:
    amount = float(input("Enter the amount: "))

    source = input("Enter the source currency (USD/CAD/EURO): ").upper()
    target = input("Enter the target currency (USD/CAD/EURO): ").upper()

    converted = 0.00

    if source == 'USD':
        converted = USD(amount, target)
    elif source == 'CAD':
        converted = CAD(amount, target)
    elif source == 'EURO':
        converted = EURO(amount, target)
    else:
        print('Please input the correct source currency.')

    if converted is not None:
        print(f"Converted amount: {converted:.2f} {target}")
    else:
        print("Invalid target currency.")
except:
    print('Value error in amount ')