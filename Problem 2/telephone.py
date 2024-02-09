def telephone():
    phone_number = int(input())
    prefix = int(phone_number % 10000000)

    print("(" + str(phone_number//10000000) + ")" + str(prefix) + str(phone_number % 10000))
    ''' Type your code here. '''
if __name__ == "__main__":
    telephone()