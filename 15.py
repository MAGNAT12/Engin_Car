class Engin:
    
    def on(self):
        print('on')

    def off(self):
        print('off')

class Car:
    
    def init(self) -> None:
        self.engin = Engin()

    def on_engin(self):
        self.engin.on()

    def off_engin(self):
        self.engin.off()


a = Car()
a.on_engin()
a.off_engin()