package AgendaRN;
import java.util.Scanner;
import ArbolRN.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Agenda de contactos");
        System.out.println("Ingrese la cantidad de contactos a agendar: ");
        int n = sc.nextInt();

        Arbol Arbolito = new Arbol();
        int datos[]= new int[n];
        for (int i = 0; i < n; i++) {
          Arbolito.insertar(datos[i]);
        }
        //Arbolito.eliminar(0);
        //System.out.println(Arbolito.buscar(5));
        Arbolito.recorrer(Recorrido.POSTORDER);//Left, Right, Nodo

    }
}
