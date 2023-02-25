package AgendaRN;
import java.util.Scanner;

import AgendaRN.Logic.Datos;
import AgendaRN.Logic.*;
import java.util.Random;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Arbol Arbolito = new Arbol();
        Random random = new Random();
        System.out.println("Agenda de contactos");
        System.out.println("Ingrese la cantidad de contactos a agendar: ");
        int n = sc.nextInt();
        Datos datos[]= new Datos[n];

        long time_i = System.nanoTime(); //tiempo inicial
        for (int i = 0; i < n; i++) {
          String nombre = (char) (random.nextInt(26) + 'a')+""+(char) (random.nextInt(26) + 'a')+(char) (random.nextInt(26) + 'a');
          String apellido = (char) (random.nextInt(26) + 'a')+""+(char) (random.nextInt(26) + 'a')+(char) (random.nextInt(26) + 'a');
          String ciudad = (char) (random.nextInt(26) + 'a')+""+(char) (random.nextInt(26) + 'a')+(char) (random.nextInt(26) + 'a');
          datos[i]=new Datos(i,nombre, apellido, ciudad);
          Arbolito.insertar(datos[i]);
        }
        //Arbolito.eliminar(datos[n-1]);
        //System.out.println(Arbolito.buscar(datos[n-1]));
        Arbolito.recorrer(Recorrido.POSTORDER);//Left, Right, Nodo
        long double_f = (System.nanoTime() - time_i)/1000000;
        System.out.println("tiempo de ejecucion: " + double_f+" mili segundos");
    }
}
