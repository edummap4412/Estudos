import pyttsx3

engine = pyttsx3.init()

a = input('Qual seu nome')
print(f"Olá, como você está {a}?")
engine.say(f"Olá, como você está {a}?")
print("Porfavor, Digite sua senha")
engine.say("Porfavor, Digite sua senha")
engine.runAndWait()


def valide_senha(senha):
    contator = 0
    while contator != 2:
        if senha != 12345:
            engine.say("Senha invalida porfavor digite a senha novamente")
            engine.runAndWait()
            senha = int(input('Digite senha novamente:'))
            contator += 1
        else:
            return engine.say("Senha correta")

    if contator == 2:
        engine.say('Conta Bloqueada')
        print("Conta bloqueada")

password = int(input('Digite sua senha:'))

valide_senha(password)

engine.runAndWait()