#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

void readTextFromFile(char *buf){
	FILE *hFile = fopen("flag.txt", "r");
	if(hFile == NULL){
		printf("Can't find the file: 'flag.txt'\n");
		exit(1);
	}
	fgets(buf, 1024, hFile);
	fclose(hFile);
}
void writeText2File(char buf[]){
	FILE *hFile = fopen("flag.txt", "w");
	int n = strlen(buf);
	for(int i = 0; i < n; i++){
		fprintf(hFile, "%X ", buf[i] & 0xff);
	}
	fclose(hFile);
}
int main(){
	char plainT[1024];
	char buf[1024];
	memset(buf, 0, sizeof(buf));
	memset(plainT, 0, sizeof(plainT));
	readTextFromFile(plainT);

	int sock_fd = socket(AF_INET, SOCK_STREAM, 0);
	struct sockaddr_in server_addr;
	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(1337);
	server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	int connection_stat = connect(sock_fd, (struct sockaddr *) &server_addr, sizeof(server_addr));

	if(connection_stat == -1){
		printf("connection error\n");
		exit(1);
	}
	send(sock_fd, plainT, strlen(plainT), 0);
	read(sock_fd, buf, 1024);
	writeText2File(buf);
	close(sock_fd);
	return 0;
}
