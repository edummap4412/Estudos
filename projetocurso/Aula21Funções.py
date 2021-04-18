"""def greet_user(username):
    print("Hello," +username.title()+ "!")


greet_user('Jesse')


def display_message(messagem):
    print('Estou aprimorando meus conhecimentos é Função,'+messagem)


display_message('Parabéns')


def describe_pet(animal_type, pet_name):
    print("\n have a "+animal_type+".")
    print("My " +animal_type+"'s name is "+pet_name.title()+".")

describe_pet(animal_type='Hamster',pet_name='Harry')

#VALOR DEFAULT
def describe_pet(animal_type, pet_name='Willie'):
    print('\nI have a '+animal_type+ '.')
    print("My "+animal_type+ "´s name is "+pet_name.title()+".")

describe_pet('Hamster','Harry')
describe_pet('Dog')



def make_shirt(size_shirt='XXL', type_message='I love Python'):
    print(f'the size shirt is {size_shirt} and message chosen was {type_message}')


make_shirt('XXL', 'I love IT')
make_shirt('XL', ' I LovUPython')
make_shirt('L')

def Names(state,country='Brazil'):
    print(f'My state is {state} and stay in  {country}')


Names('São Paulo')
Names('Rio de Janeiro')
Names('Amazonas')"""

def espaco():
    print('-='*30)



def get_name(first_name,last_name):
    full_name = first_name+' '+last_name

    return full_name.title()

musician = get_name('michael','jackson')

print(musician)



def get_formatted_name(first_name, last_name, middle_name=' '):
    if middle_name:
        full_name = first_name + ' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name

    return full_name

musician = get_formatted_name('Jimi', 'Hendrix')
print(musician)

musician = get_formatted_name('John', 'Hooker', 'Lee')
print(musician)



def build_person(first_name, last_name):
    person = {'first': first_name ,'last':last_name}
    return person

musician = build_person('Freddie', 'Mercury')
print(musician)

for v in musician.values():
    print(v, end=' ')
print()
espaco()

def build_person(first_name, last_name, age=' '):

    person = {'first':first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

people = build_person('Eduardo', 'Mascarenhas', '25')

print(people)
