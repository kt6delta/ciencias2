package AgendaRN;
import java.util.Scanner;

import AgendaRN.Logic.Datos;
import AgendaRN.Logic.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Agenda de contactos");
        System.out.println("Ingrese la cantidad de contactos a agendar: ");
        int n = sc.nextInt();
        Arbol Arbolito = new Arbol();
        Datos datos[]= new Datos[n];

        for (int i = 0; i < n; i++) {
          System.out.println("Ingrese nombre: ");
          String nombre = sc.next();
          System.out.println("Ingrese apellido: ");
          String apellido = sc.next();
          System.out.println("Ingrese ciudad: ");
          String ciudad = sc.next();
          datos[i]=new Datos(i,nombre, apellido, ciudad);
          Arbolito.insertar(datos[i]);
        }
        //Arbolito.eliminar(datos[n-1]);
        //System.out.println(Arbolito.buscar(datos[n-1]));
        Arbolito.recorrer(Recorrido.POSTORDER);//Left, Right, Nodo

    }
}
