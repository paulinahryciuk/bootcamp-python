class Printer:
    def print_msg(self,message):
        print(f"Drukow wiadom {message}")

class Scanner:
    def scan_dock(self):
        print("Skanowanie ")
        return"zawart dokumenh"

class MultifunDev(Printer,Scanner):
    def photocopy(self):
        content = self.scan_dock()
        self.print_msg(content)

device = MultifunDev()
device.photocopy()

