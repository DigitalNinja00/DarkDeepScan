#include<stdio.h>
#include<string.h>
#include<stdlib.h>


int funtion_press(){
	system("ruby ./fun_rb/ban.rb");
	printf("\n");
	system("ruby ./fun_rb/main.rb");
	return 0;
}
int funtion_basic_scan_call(){
	system("ruby fun_rb/add.rb");
	return 0;
}
int funtion_basic_scan_with_text_none(){
	system("ruby fun_rb/add_txt.rb");
	return 0;
}
int only_port_scan_dont_txt(){
	system("ruby fun_rb/exe_only_txt.rb");
	return 0;
}
int only_port_scan_none(){
	system("ruby fun_rb/exe_only.rb");
	return 0;
}
int main(){
	funtion_press(); int input; printf("Seleccion$> ");
	scanf("%i", &input);
	if(input==1){
		int estoy_solo;
		printf("Quieres guardar el escaneo en un txt? \n[1]YES, [2]NO\n&> ");
		scanf("%i", &estoy_solo);
		if(estoy_solo==1){
			printf("Los txt del escaneo se guardan en ~/path/log/log_scan.txt\n");
			funtion_basic_scan_with_text_none();
		}else{
			if(estoy_solo==2){
				funtion_basic_scan_call();
			}else{
				printf("Caracter no valido BREAK!\n");
			}
		}
	}else{
		if(input==2){
			int why;
			printf("Quieres guardar el escaneo en un txt? \n[1]YES, [2]NO\n&> ");
			scanf("%i",&why);
			if(why==1){
				only_port_scan_none();
			}else{
				if(why==2){
					only_port_scan_dont_txt();
				}else{
					printf("Caracter no valido BREAK\n");
				}
			}
		}
	}
	return 0;
}