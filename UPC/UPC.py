def is_valid_upc(upc_string):
    upc = []
    for number in upc_string:
        upc.append(int(number))

    upc_check = (((upc[0] + upc[2] + upc[4] + upc[6] + upc[8] + upc[10]) * 3)
                    + (upc[1] + upc[3] +upc[5] + upc[7] + upc[9])) % 10
    if upc_check != 0:
        upc_check = 10 - upc_check
    check_digit = upc[11]
    return upc_check == check_digit

input_upc_string = input("Please enter the 12 digit UPC.")
while len(input_upc_string) != 12:
    input_upc_string = input("Please enter the 12 digit UPC.")

if is_valid_upc(input_upc_string):
    print("Your UPC is valid.")
else:
    print("Your UPC is not valid.")







