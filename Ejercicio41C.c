#include <stdio.h>

int main() {
	int menor = 0, mayor = 0, n = 0, numero = 0, x = 0;
	
	printf("�Cu�ntos n�meros va a usar?");
		scanf("%d",&n);
		for (x = 0; x < n; x++){
			printf("Ingrese un n�mero: ");
				scanf("%d",&numero);
				if (x == 0){
					mayor = numero;
					menor = numero;
				}
				if (numero > mayor){
					mayor = numero;
				}
				else
					if (numero < menor){
						menor = numero;
					}
				
		}
		printf("El n�mero mayor es: ");
		printf("%d%", mayor);
		printf(" y el menor es: ");
		printf("%d%", menor);
	
}

