from django.contrib.auth.models import User


def verifica_date(name,password):
    if  len(password) < 8 or len(password) > 16:
        return 'La password deve essera di minimo di 6 simboli e massimo di 16 simboli'
    if  len(name) < 6 or len(name) > 16:
        return 'Il nome deve essera di minimo di 5 simboli e massimo di 15 simboli'
    if not password.isalnum():
        return 'La password deve avere sia lettere che numeri'
    if not any(number.isdigit() for number in password):
        return 'La password deve avere al meno un numero'
    if not any(lettere.isalpha() for lettere in password):
        return 'La password deve avere al meno una lettera'
    else:
        return 'La password e Adatta'
    
def verifica_Unicità(name,password,email):
    if User.objects.filter(username=name).exists():
        return f'il nome {name} gia essiste'
    else:
        u = User.objects.create_user(username=name,password=password,email=email)
        u.save()
        return 'Vi siete registrati adesso ritornate nella pagina "Accesso" per entrare nel account'
