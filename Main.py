import pandas as pd
import Criptografer as c
import Descriptografer as d

df = pd.read_csv("logs.csv")

#Sistema de Login
while True:
    
    Login = c.allCripto(input("Usuario>>"),15)
    Password = c.allCripto(input("Senha>>"),15)
    Login_name = d.AllDescripto(Login,15)
    Find = False
    
    for index, row in df.iterrows():
        if row['Login'] == Login and row['Password'] == Password:
            Find = True
    if Find:
        break
    else:
        print("Úsuario não encontrado ou senha incorrestos")
        Choice = input("Deseja se Cadastrar? S/N").lower()
        if Choice == "s":

            New_login = c.allCripto(input("Novo Usuario>>"),15)
            New_password = c.allCripto(input("Nova Senha>>"),15)

            if (df['Login'] == New_login).any():
                print('Usuario já existente')
            else:
                New_user = pd.DataFrame(
                [{"Login": New_login, "Password": New_password}])
                New_user.to_csv("logs.csv", mode="a",
                                index=False, header=False)
                df = pd.read_csv("logs.csv")

#Sistema de Verificação de Funcionarios
while True:
    print("--------------------------")
    print(f"      Bom dia {Login_name}")
    print("--------------------------")
    print("oq deseja fazer?")
    Choice = input("/Verificar/")
    match Choice:
        case "Verificar":
            break
