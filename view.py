menu_options = {
    1: 'Registar_usuario',
    2: 'Login_usuario',
    3: 'Reserva_bilhete',
    4: 'Alteraçao_bilhete',
    5: 'Saida',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def Registar_usuario():
    arq = open("registados.txt", "a")
    print("Registe uma nova conta!")
    nome_usuario = input("Digite o seu nome de usuário: ")

    arq.write("{}\n".format(nome_usuario))
    print ("Registo realizado com sucesso")

def Login_usuario():
    arq = open("registados.txt")
    print("Efetue o login")
    nome_login = input("Digite o seu nome de usuario: ")

    registados = arq.readlines()
    if nome_login + "\n" in registados:
        print("Bem vindo, {}.".format(nome_login))
    else:
        print("Nome de usuario incorreto.")
    arq.close()

def Reserva_bilhete():
     print('Handle option \'Option 2\'')

def Alteraçao_bilhete():
     print("    1   2           3   4   5   6   7   8   9  10  11  12     13  14 ")
     print("")
     print("  ---------        ----------------------------------------    --------")
     print("K |   |   |       |   |   |   |   |   |   |   |   |   |   |   |   |   |  ")
     print("  ---------        ----------------------------------------    --------")
     print("J |   |   |       |   |   |   |   |   |   |   |   |   |   |   |   |   |  ")
     print("  ---------        ----------------------------------------    --------")
     print("I |   |   |       |   |   |   |   |   |   |   |   |   |   |   |   |   |  ")
     print("  ---------        ----------------------------------------    --------")
     print("H |   |   |       |   |   |   |   |   |   |   |   |   |   |   |   |   |  ")
     print("  ---------        ----------------------------------------    --------")
     print("G |   |   |       |   |   |   |   |   |   |   |   |   |   |   |   |   |  ")
     print("  ---------                   -----------------                --------")
     print("F |   |   |                   |VIP|VIP|VIP|VIP|               |   |   |  ")
     print("  ---------                   -----------------                --------")
     print("")
     print("  ---------        ----------------------------------------    --------")
     print("E |   |   |       |   |   |   |   |   |   |   |   |   |   |   |   |   |  ")
     print("  ---------        ----------------------------------------    --------")
     print("D |   |   |       |   |   |   |   |   |   |   |   |   |   |   |   |   |  ")
     print("  ---------        ----------------------------------------    --------")
     print("C |   |   |       |   |   |   |   |   |   |   |   |   |   |   |   |   |  ")
     print("  ---------        ----------------------------------------    --------")
     print("B |   |   |       |   |   |   |   |   |   |   |   |   |   |   |   |   |  ")
     print("  ---------        ----------------------------------------    --------")
     print("")
     print("  ---------                   -----------------                --------")
     print("A |   |   |                   |VIP|VIP|VIP|VIP|               |   |   |  ")
     print("  ---------                   -----------------                --------")



     







     



     


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Escolha uma opção: '))
        except:
            print('Por favor digite um número...')
        if option == 1:
            Registar_usuario()
        elif option == 2:
            Login_usuario()
        elif option == 3:
            Reserva_bilhete()
        elif option == 4:
            Alteraçao_bilhete()
        elif option == 5:
            print('Obrigado, volte sempre')
            exit()
        else:
            print('Opção invalida, digite um número entre 1 e 4')





print("   1  2        3  4  5  6  7  8  9  10  11  12     13  14 ")
print("")
