# klasy mixin -

class Printer:
    def print_message(self, message):
        print(f"Drukowanie wiadomości {message}")


class Scanner:
    def scan_document(self):
        print("Skanowanie dokumentu...")
        return 'Zawartość dokumentu'


class MultifunctinDevice(Printer, Scanner):
    def photocopy(self):
        content = self.scan_document()
        self.print_message(content)


printer = Printer()
printer.print_message("Komunikat")
# Drukowanie wiadomości Komunikat

scanner = Scanner()
wynik = scanner.scan_document()
print("Wynik skanowania:", wynik) # Wynik skanowania: Zawartość dokumentu

device = MultifunctinDevice()
device.photocopy()
# Skanowanie dokumentu...
# Drukowanie wiadomości Zawartość dokumentu