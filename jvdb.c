#include <stdio.h>

int main(){
    FILE *archivo;
    archivo = fopen("basededatos.txt","w");
    char *texto = "JVDB";
    fputs(texto,archivo);
    fclose(archivo);
    printf("JVDB");
    return 0; 
}