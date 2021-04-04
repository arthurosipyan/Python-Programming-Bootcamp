# Enter Customer? (Y/N) y
# Enter Customer Name: Arthur Osipyan
# Enter Customer? (Y/N) y
# Enter Customer Name: Joe Smith
# Enter Customer? (Y/N) n
# Arthur Osipyan
# Joe Smith

customer_list = []


def main():
    create_entry = input("Enter Customer? (Y/N)")[0].lower()
    if create_entry == "y":
        f_name, l_name = input("Enter Customer Name: ").split()
        customer_list.append({"f_name": f_name, "l_name": l_name})
        main()
    else:
        for cust in customer_list:
            print(cust["f_name"], cust["l_name"])


main()
