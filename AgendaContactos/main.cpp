#include <iostream>

#include "arbolBinario.h"
#include "structs.h"

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

using std::string;
using namespace std;

contacto a;

int main(int argc, char** argv) {
	
	int n;
	string nombre;
	string apellido;
	string ciudad;
	
	
	cout<<"Agenda de contactos"<<endl;
	cout<<"Ingrese la cantidad de contactos a agendar: ";
	cin>>n;
	
	
	arbolBinarioOrdenadoArreglo<contacto> arbolContactos(n);
	
	for(int i=0; i<n; i++){
		
		cout<<"Contacto N."<<i+1<<endl;
		cout<<"Nombre: ";
		cin>>nombre;
		a.nombreContacto = nombre;
		cout<<"Apellido: ";
		cin>>apellido;
		a.apellidoContacto = apellido;
		cout<<"Ciudad: ";
		cin>>ciudad;
		a.ciudad = ciudad;
		arbolContactos.insertar(a);
		
	}
	
	cout<<"[+] Contactos ingresados: "<<endl;
	
	for(int i=0; i<=n; i++){
		
		a = arbolContactos.getData(i);
		cout<<"Contacto N."<<i+1<<": "<<endl;	
		cout<<a.nombreContacto<<" "<<a.apellidoContacto<<" "<<a.ciudad<<" "<<endl;	
				
	}
	
	
	
	
	return 0;
}
