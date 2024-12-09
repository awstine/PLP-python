class Smartphone:
    def __init__(self,touch,buttons):
        self.touch = touch
        self.buttons = buttons
    def huawei(self):
        self.touch = "yes"
    def motorolla(self):
        self.buttons = "yes"

phone = Smartphone("no","no")
phone.motorolla()
print(phone.touch)