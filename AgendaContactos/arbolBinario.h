#include <iostream>
#ifndef lib_h
#define lib_h


using namespace std;

template <class T>
struct NodoArbol {
	T clave;
	int izquierda, derecha;
};

template <class T>
class arbolBinarioOrdenadoArreglo{
	NodoArbol <T> *arbol;
	int posLlenar;
	public: arbolBinarioOrdenadoArreglo(int tam){
		arbol = new NodoArbol <T>[tam + 1];
		for (int i=0; i < tam; i++){
			arbol[i].derecha = (i*2)+1;
			arbol[i].izquierda = (i*2);
		}
		arbol[tam].derecha = 0;	
		arbol[0].izquierda = 0;	
		posLlenar=0;	
	}
	void insertar (T info);	
//	void subirGanador (T info);
	int getRaiz ();
	T getData(int pos);
	void inorden(int inicio);
	void preorden(int inicio);
	void posorden(int inicio);
	~arbolBinarioOrdenadoArreglo();
};

template <class T>
void arbolBinarioOrdenadoArreglo <T>::insertar (T info){
	int posicionLibre = arbol[0].derecha;
	int aux;
//	equipo estadioAux;
	arbol[posLlenar].clave=info;
	posLlenar++;	
}

//template <class T>
//void printLevelOrder(int root)
//{
//	
//}
//
//template <class T>
//void arbolBinarioOrdenadoArreglo<T>::subirGanador(T info){
//	int i=1;
// 	equipo nodoBusca,otro;
// 	otro=info;
// 	nodoBusca = arbol[i].clave;
//	while(otro.nombre != nodoBusca.nombre){
//		nodoBusca = arbol[i].clave;
//		i++;
//		if(otro.nombre == nodoBusca.nombre){
//			i=i/2;
//			arbol[i].clave=otro;
//		}	
//	}
//}

template <class T>
T arbolBinarioOrdenadoArreglo<T>::getData(int pos){
	return arbol[pos].clave;
	}


template <class T>
int arbolBinarioOrdenadoArreglo<T>::getRaiz (){
	return arbol[0].izquierda;
}

template <class T>
void arbolBinarioOrdenadoArreglo<T>::inorden(int inicio){
	if (inicio != 0){
		inorden(arbol[inicio].izquierda);
		cout << "- "  << arbol[inicio].clave << " -";
		inorden(arbol[inicio].derecha);
	}
}

template <class T>
void arbolBinarioOrdenadoArreglo<T>::preorden(int inicio){
	if (inicio != 0){
		cout << "- " << arbol[inicio].clave << " -";
		preorden(arbol[inicio].izquierda);		
		preorden(arbol[inicio].derecha);
	}
}

template <class T>
void arbolBinarioOrdenadoArreglo<T>::posorden(int inicio){
	if (inicio != 0){
		posorden(arbol[inicio].izquierda);		
		posorden(arbol[inicio].derecha);
		cout << "- " << arbol[inicio].clave << " -";
	}
}

template <class T>
arbolBinarioOrdenadoArreglo<T>::~arbolBinarioOrdenadoArreglo(){
	delete arbol;
}

#endif /* lib_h */

