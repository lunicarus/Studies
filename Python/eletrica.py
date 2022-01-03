def FormulaTensao(ra,rb,rc,t):
    ia = t/ra; # ia = 12/3 // ia =  4/  ia = 3/13
    ib = t/rb;
    ic = t/rc;
    pa = ra * ia**2;
    pb = rb * ib**2;
    pc = rc * ic**2;
    i = 0;
    if ia < 10 and ia >= 1:  
        print("Corrente parcial de Ra é:", round(ib,2), "Amperes");
        i = 0;
    else:
        while ia >= 10:
            ia = ia/10;
            i = i+1;
            if ia < 10 and ia >= 1:  
                print("Corrente parcial de Ra é:", round(ia,2),"*10^",i, "Amperes");
                i = 0; 
        while ia < 1:
            ia = ia*10
            i = i-1;
            if ia < 10 and ia >= 1:  
                print("Corrente parcial de Ra é:", round(ia,2),"*10^",i, "Amperes");
                i = 0;
    if ib < 10 and ib >= 1: 
        print("Corrente parcial de Rb é:", round(ib,2), "Amperes");
        i = 0;
    else:
        while ib >= 10:
            ib = ib/10;
            i = i+1;
            if ib < 10 and ib >= 1:  
                print("Corrente parcial de Rb é:", round(ib,2),"*10^",i, "Amperes");
                i = 0; 
        while ib < 1:
            ib = ib*10
            i = i-1;
            if ib < 10 and ib >= 1:  
                print("Corrente parcial de Rb é:", round(ib,2),"*10^",i, "Amperes");
                i = 0;
    if ic < 10 and ic >= 1: 
        print("Corrente parcial de Rb é:", round(ic,2), "Amperes");
        i = 0;
    else:
        while ic >= 10:
            ic = ic/10;
            i = i+1;
            if ic < 10 and ic >= 1:  
                print("Corrente parcial de Rc é:", round(ic,2),"*10^",i, "Amperes");
                i = 0; 
        while ic < 1:
            ic = ic*10
            i = i-1;
            if ic < 10 and ic >= 1:  
                print("Corrente parcial de Rc é:", round(ic,2),"*10^",i, "Amperes");
                i = 0;
    if pa < 10 and pa >= 1:  
        print("Potencia parcial de Ra é:", round(pa,2),"watts");
        i = 0;
    else:
        while pa >= 10:
            pa = pa/10;
            i = i+1;
            if pa < 10 and pa >= 1:  
                print("Potencia parcial de Ra é:", round(pa,2),"*10^",i,"watts");
                i = 0; 
        while pa < 1:
            pa = pa*10
            i = i-1;
            if pa < 10 and pa >= 1:  
                print("potencia parcial de Ra é:", round(pa,2),"*10^",i,"watts");
                i = 0;
    if pb < 10 and pb >= 1:  
        print("Potencia parcial de Rb é:", round(pb,2),"watts");
        i = 0;
    else:
        while pb >= 10:
            pb = pb/10;
            i = i+1;
            if pb < 10 and pb >= 1:  
                print("Potencia parcial de Rb é:", round(pb,2),"*10^",i,"watts");
                i = 0; 
        while pb < 1:
            pb = pb*10
            i = i-1;
            if pb < 10 and pb >= 1:  
                print("Potencia parcial de Rb é:", round(pb,2),"*10^",i,"watts");
                i = 0;
    if pc < 10 and pc >= 1:  
        print("Potencia parcial de Rc é:", round(pc,2),"watts");
        i = 0;
    else:
        while pc >= 10:
            pc = pc/10;
            i = i+1;
            if pc < 10 and pc >= 1:  
                print("Potencia parcial de Rc é:", round(pc,2),"*10^",i,"watts");
                i = 0; 
        while pc < 1:
            pc = pc*10
            i = i-1;
            if pc < 10 and pc >= 1:  
                print("Potencia parcial de Rc é:", round(pc,2),"*10^",i,"watts");
                i = 0;
    #if i == 3:
        #print("Corrente parcial de Rc é:", round(ic,2),"Mili amperes");  
    #elif i == 6:
        #print("Corrente parcial de Rc é:", round(ic,2),"Micro amperes");  
    #else: 
        #print("Corrente parcial de Rc é:", round(ic,2),"*10^-",i); 
res = 0;
while (res != 5):
    try:
        print("informe a tensão do sistema\n")
        tensao = int(input());
        if tensao < 0 or tensao > 12:
            print("valores negativos e maiores que 12 não serão aceitos! redigite o valor da tensão!\n");
        else: 
            print(" selecione um tipo de circuito:\n 1-Serie\n 2-Paralelo\n 3-Misto\n 4-misto com um serie\n 5-encerrar progama ");
            res = int(input());
            Controle = 0;
    except ValueError:
        print("\nValor invalido! (são aceitos apenas valores inteiros!)");
        continue;
    if res ==1:
        print("\nCircuito em Serie, Devina os valores das Resistencias (Ra,Rb e Rc)");
        while Controle <= 0:
            try: #try executa um codigo que pode dar erro, dando um determinado erro(neste caso, ValueError caso o usuario informe um valor float ou char) ele executa o codigo dentro do Except
                Ra = int(input());
                Rb = int(input());
                Rc = int(input()); #converte todos os valores para Tipo int
                if Ra < 0 or Rb < 0 or Rc < 0: #testa se valores são < 0, imprime mensagem de erro se for o caso
                    print("\nValores de Resistencias Invalidos!(Numeros negativos não são aceitos!)");
                elif Ra >= 10000 or Rb >= 10000 or Rc >= 10000:
                    print("\nnão serão aceitos valores maiores que 10mil ohms!");
                else:
                    Total = Ra+Rb+Rc;
                    print("\nesse é o valor da resistência :");
                    if Total > 1000:
                        Total = Total/1000;
                        print(round(Total,2)," Kilo Ohms\n")
                        FormulaTensao(Ra,Rb,Rc,tensao);
                        break;
                    else:
                        print(round(Total,2)," Ohms\n");
                        FormulaTensao(Ra,Rb,Rc,tensao);
                        break;
            except ValueError: #Caso de erro de valor: usuario coloque um valor tipo float(2.5 por ex) ele ira imprimir a mensagem de erro abaixo
                print("\nValores de Resistencias Invalidos!(Numeros Fracionados não são aceitos!)");
                continue;
    elif res == 2:
        print("\nCircuito Em paralelo");
        while Controle == 0:
            try:
                Ra = int(input());
                Rb = int(input());
                Rc = int(input());
                if Ra < 0 or Rb < 0 or Rc < 0: #testa se valores são < 0, imprime mensagem de erro se for o caso
                    print("\nValores de Resistencias Invalidos!(Numeros negativos não são aceitos!)");
                elif Ra >= 10000 or Rb >= 10000 or Rc >= 10000:
                    print("\nnão serão aceitos valores maiores que 10mil ohms!");
                else:
                    Total = 1/(1/Ra+1/Rb+1/Rc);
                    print("\nEsse é o valor da resitencia em paralelo ");
                    if Total > 1000:
                        Total = Total/1000;
                        print(round(Total,2)," Kilo Ohms")
                        FormulaTensao(Ra,Rb,Rc,tensao);
                        break;
                    else:
                        print(round(Total,2)," Ohms");
                        FormulaTensao(Ra,Rb,Rc,tensao);
                        break;
            except ValueError: #Caso o valor seja invalido, ele executa o print abaixo
                print("\nValor invalido!, repita os 3 valores");
                continue;
    elif res == 3:
        print("\nCircuito Misto");
        print("\nO valor da Ra sera arbitrariamente o valor que esta fora do paralelo");
        while Controle != 1:
            try:
                Ra = int(input());
                Rb = int(input());
                Rc = int(input());
                if Ra < 0 or Rb < 0 or Rc < 0: #testa se valores são < 0, imprime mensagem de erro se for o caso
                    print("\nValores de Resistencias Invalidos!(Numeros negativos não são aceitos!)");
                elif Ra >= 10000 or Rb >= 10000 or Rc >= 10000:
                    print("\nnão serão aceitos valores maiores que 10mil ohms!");
                else:
                    Total = Ra+((Rb*Rc)/(Rb+Rc));
                    print("\nEsse é o valor da resistencia no circuito com resistencias mistas ");
                    if Total > 1000:
                        Total = Total/1000;
                        print(round(Total,2)," Kilo Ohms")
                        FormulaTensao(Ra,Rb,Rc,tensao);
                        break;
                    else:
                        print(round(Total,2)," Ohms");
                        FormulaTensao(Ra,Rb,Rc,tensao);
                        break;
            except ValueError:
                print("\nvalor invalido,repita os 3 valores");
                continue;
    elif res == 4:
        print("\nmisto com uma paralela com uma serie de resistores")
        print("\nresistores Ra e Rb estarão em uma série, e Rc estara em paralelo ");
        while Controle == 0:
            try:
                Ra = int(input());
                Rb = int(input());
                Rc = int(input());
                if Ra < 0 or Rb < 0 or Rc < 0: #testa se valores são < 0, imprime mensagem de erro se for o caso
                    print("\nValores de Resistencias Invalidos!(Numeros negativos não são aceitos!), Redigite os valores");
                elif Ra >= 10000 or Rb >= 10000 or Rc >= 10000:
                    print("\nnão serão aceitos valores maiores que 10mil ohms!, Redigite os Valores");
                else:
                    Total = ((Ra+Rb)*Rc)/((Ra+Rb)+Rc);
                    if Total > 1000:
                        Total = Total/1000;
                        print(round(Total,2)," Kilo Ohms")
                        FormulaTensao(Ra,Rb,Rc,tensao);
                        break;
                    else:
                        print(round(Total,2)," Ohms");
                        FormulaTensao(Ra,Rb,Rc,tensao);
                        break;
            except ValueError:
                print("\nvalor invalido, Redigite os valores");
                continue;
    elif res == 5:
        print("\nProgama encerrado!");

    else:
        print("Opção Invalida!");
        break;