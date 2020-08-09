import pickle
import class_data
# taking inpur from the user and stroing the details in the file

no_of_laptop = int(input("Enter how laptop's details you want to add:"))
with open('laptop.dat', mode='wb') as lp:
    for data in range(no_of_laptop):
        model = input("Enter the model: ")
        price = int(input("Enter the price: "))
        ram = input("Enter the ram: ")
        hdd = input("Enter the hdd: ")
        processor = input("Enter the processor: ")
        print()
        details = class_data.Laptop(model=model, price=price, ram=ram,
                                    hdd=hdd, processor=processor)
        pickle.dump(details, lp)
    print("details pickled sucessfully")
