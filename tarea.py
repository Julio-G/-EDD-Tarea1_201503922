class Nodo:
    def __init__(self, dato=None, sig=None):
        self.dato = dato
        self.sig = sig
class Lista:
    def __init__(self):
        self.inicio = None

    def insertar(self, dato):
        self.inicio = Nodo(dato=dato, sig=self.inicio)

    def insertar(self, dato):
        self.inicio = Nodo(dato=dato, sig=self.inicio)

    def eliminar(self,dato):
        if(self.inicio!=None):
            aux=self.inicio
            anterior=None
            while(aux.dato!=dato and aux!=None):
                anterior=aux
                aux=aux.sig
            if(aux==self.inicio):
                self.inicio=aux.sig
            elif(aux.dato==dato and aux!=self.inicio and aux.sig!=None):
                anterior.sig=aux.sig
                aux.sig=None
            elif(aux.dato==dato and aux!=self.inicio and aux.sig==None):
                anterior.sig=None
            elif(aux==None):
                print("No se encontro")
        else:
            print("No hay elementos en la lista")

    def modificar(self, dato,dato2):
        if (self.inicio != None):
            aux2 = self.inicio
            aux = self.inicio
            anterior = None
            while (aux.dato != dato and aux != None):
                anterior = aux
                aux = aux.sig
            if (aux != None):
                aux.dato = dato2;
            elif(aux==None):
                print("No se encontro")
        else:
            print("No hay elementos en la lista")

    def mostrar( self ):
        aux = self.inicio
        while aux != None:
            print(aux.dato)
            aux = aux.sig
n1=0;
lista=Lista()
while(n1!=5):

   print(".: Menu :.");
   print("1) Insertar");
   print("2) Modificar");
   print("3) Eliminar");
   print("4) Mostrar");
   print("5) Salir");
   n1=int(input("Ingrese el numero: "));
   if n1==1:
       n2 = input("Ingrese el dato a insertar");
       lista.insertar(n2)

   elif n1==2:
       n2 = input("Ingrese el dato a modificar");
       n3 = input("Ingrese el dato a colocar");
       lista.modificar(n2,n3)
   elif n1==3:
       n2 = input("Ingrese el dato a eliminar");
       lista.eliminar(n2)
   elif n1==4:
       lista.mostrar()
