#include <stdio.h>

void main(int argc, char* argv[]){
	FILE *f;
	//char* file_name = (char*)malloc(50*sizeof(char));
	
	char* file_name[50];

	strcpy(file_name, argv[1]);
	strcat(file_name, ".txt");
	if(file_name == NULL)
	{	
		printf("File is not open!\n");
		exit(0);
	}

	f = fopen(file_name, "w");

	if(f == NULL)
		printf("File open error %s\n", argv[1]);	

	fprintf(f, "miehahahaha, ID=%s\n", argv[1]);

	fclose(f);
	printf("Hello World from Ethan! FFS!!!!!! ID = %s\n", argv[1]);
	
//	free(file_name);

	printf("FXXX the world!\n");

}
