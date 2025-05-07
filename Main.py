import pandas as pd


df = pd.read_csv("logs.csv")

#Sistema de Login
while True:
    
    Login = input("Usuario>>")
    Password = input("Senha>>")

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
            New_login = input("Novo Usuario>>")
            New_password = input("Nova Senha>>")
            if (df['Login'] != New_login).any():
                New_user = pd.DataFrame(
                    [{"Login": New_login, "Password": New_password}])
                New_user.to_csv("logs.csv", mode="a",
                                index=False, header=False)
                df = pd.read_csv("logs.csv")
            else:
                break
#Sistema de Verificação de Funcionarios
while True:
    print("--------------------------")
    print(f"      Bom dia {Login}")
    print("--------------------------")
    print("oq deseja fazer?")
    Choice = input("/Verificar/")
    match Choice:
        case "Verificar":
            print(f"{df}")
