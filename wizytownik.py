class Wizytowka:
    def __init__(self, name, surname, company, position, mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.mail = mail

Anna = Wizytowka(name="Anna", surname="Kowalska", company="A", position="ceo", mail="anna.kowalska@mail.pl")
Aleksandra = Wizytowka(name="Aleksandra", surname="Nowak", company="B", position="section manager", mail="aleksandra.nowak@mail.pl")
Olga = Wizytowka(name="Olga", surname="Wiśniewska", company="C", position="assistant", mail="olga.wisniewska@mail.pl")
Jan = Wizytowka(name="Jan", surname="Wójcik", company="D", position="HR", mail="jan.wojcik@mail.pl")
Adam = Wizytowka(name="Adam", surname="Kowalczyk", company="E", position="main dev", mail="adam.kowalczyk@mail.pl")

wizytownik = [Anna, Aleksandra, Olga, Jan, Adam]

print(wizytownik)

for item in wizytownik:
    print(item.name, item.surname, item.company, item.position, item.mail)