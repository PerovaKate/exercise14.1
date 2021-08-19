class Recipe:
    def __init__(self, name, ingredients, desc, time, device):
        self.name= name
        self.ingredients = ingredients
        self.desc = desc
        self.time = time
        self.device= device

soup = Recipe(name= 'Борщ', ingredients= 'свекла, картошка, говядина, вода', desc='Все положите в кастрюлю и сварите',
              time= 40, device='RMC=M800S')

pie = Recipe(name= 'Пирог', ingredients='мука, яйца, яблоки', desc='Слепите и испеките', time= 50, device='RMC=M800S')

meat = Recipe(name= 'Стейк', ingredients='мясо', desc='Жарьте, пока не пожарится', time= '20', device='RMC=M800S')

print(soup.name)
print(soup.ingredients)
print(soup.desc)
print(soup.time)
print(soup.device)


print(pie.name)
print(pie.ingredients)
print(pie.desc)
print(pie.time)
print(pie.device)

print(meat.name)
print(meat.ingredients)
print(meat.desc)
print(meat.time)
print(meat.device)