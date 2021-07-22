# contacts.py
# Другим атрибутом для Employee может быть Address:

class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode
    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)

# Мы реализовали базовый класс адресов, который содержит обычные компоненты для адреса. Сделали атрибут street2 необязательным, поскольку не все адреса будут иметь этот компонент.
