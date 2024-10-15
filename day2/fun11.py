# walrus operator - operator morsa
name = "Radek"
if name == "Radek":
    print(f"Twoje imię to {name}")
# Twoje imię to Radek

if name := "Tomek":
    print(f'Twoje imię to {name}')
# Twoje imię to Tomek


przekaski = ['hotdog', 'pizza', 'hamburger', 'frytki']
prompt = "Wybierz swoją przekąskę"

# while True:
#     choice = input(prompt)
#     if choice in przekaski:
#         break
#     print("Nie ma")

# print(f"Twój wybór {choice}")
# Twoje imię to Radek
# Twoje imię to Tomek
# Wybierz swoją przekąskęfrytki
# Twój wybór frytki

while (choice := input(prompt)) not in przekaski:
    if choice == "exit":
        break
    print("Nie ma")

print(f"Twój wybór {choice}")
