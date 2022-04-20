class Cardholder:
    def __init__(self, name, surname, company, position, mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.mail = mail

anna = Cardholder(name="Anna", surname="Kowalska", company="A", position="ceo", mail="anna.kowalska@mail.pl")
aleksandra = Cardholder(name="Aleksandra", surname="Nowak", company="B", position="section manager", mail="aleksandra.nowak@mail.pl")
olga = Cardholder(name="Olga", surname="Wiśniewska", company="C", position="assistant", mail="olga.wisniewska@mail.pl")
jan = Cardholder(name="Jan", surname="Wójcik", company="D", position="HR", mail="jan.wojcik@mail.pl")
adam = Cardholder(name="Adam", surname="Kowalczyk", company="E", position="main dev", mail="adam.kowalczyk@mail.pl")

cardholder = [anna, aleksandra, olga, jan, adam]

print(cardholder)

for item in cardholder:
    print(item.name, item.surname, item.company, item.position, item.mail)