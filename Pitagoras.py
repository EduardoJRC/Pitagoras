def Pitagoras():
    from math import sqrt
    print("------------------------------------------------------------------------------------------------------")
    print("Hoy procederemos a calcular pitagoras")
    print("Recuerde que la forma de pitagoras es c^2=a^2+b^2", " donde c es la hipotenusa y a y b son los catetos")
    lado=str(input("Ingrese el lado que desconoce: "))
    print("------------------------------------------------------------------------------------------------------")
    if lado=="c":
        a=float(input("Ingrese el valor de a: "))
        b=float(input("Ingrese el valor de b: "))
        if  a>0 and b>0:
            c=sqrt(a**2+b**2)
            print("El valor de c es de: ",c)
        else:
            print("Los valores deben ser mayores de 0")
    elif lado=="a":
        c=float(input("Ingrese el valor de c: "))
        b=float(input("Ingrese el valor de b: "))
        if c<b:
            print("Recuerde que la hipotenusa c debe tener un valor mayor que b")
        else:
            if c>0 and b>0:
                a=sqrt(c**2-b**2)
                print("El valor de a es de: ",a)
            else:
                print("Los valores deben ser diferentes de 0")
    elif lado=="b":
        c=float(input("Ingrese el valor de c: "))
        a=float(input("Ingrese el valor de a: "))
        if c<a:
            print("Recuerde que c debe sere mayor que a")
        else:
            if c<0 and a<0:
                b=sqrt(c**2-a**2)
                print("El valor de b es de: ",b)
            else:
                print("Los valores deben ser diferentes de 0")
    else:
        print("---------------------------------")
        print("Por favor ingrese un letra válida")
        print("---------------------------------")
        Pitagoras()
Pitagoras()
q="si"
while q=="si":
    q=str(input("Desea continuar?"))
    if q=="sí" or q=="si" or q=="yes" or q=="y" or q=="s":
        Pitagoras()
    else:
        print("Bye")
        break