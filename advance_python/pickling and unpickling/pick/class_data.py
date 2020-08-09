# class file
# class_data.py

class Laptop:
    def __init__(self, model, price, ram, hdd, processor):
        self.lp_model = model
        self.lp_price = price
        self.lp_ram = ram
        self.lp_hdd = hdd
        self.lp_processor = processor

    def show_details(self):
        print(
            f"Model-->{self.lp_model}\nPrice-->{self.lp_price}\nRam-->{self.lp_ram}\nHDD-->{self.lp_hdd}\nProcessor-->{self.lp_processor}")
