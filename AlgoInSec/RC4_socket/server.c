#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>

void swap(unsigned char *a, unsigned char *b){
	int tmp = *a;
	*a = *b;
	*b = tmp;
}
void KSA(unsigned char *s){
	char *key = "socket";
	for(int i = 0; i < 256; i++)
		s[i] = i;
	int j = 0;
	for(int i = 0; i < 256; i++){
		j = (j + s[i] + key[i % 6]) % 256;
		swap(&s[i], &s[j]);
	}
}
void enc_(unsigned char *plainT, unsigned char *cipherT, int len){
	int i = 0;
	int j = 0;
	unsigned char s[256];
	KSA(s);
	for(int n = 0; n < len; n++){
		i = (i+1) % 256;
		j = (j + s[i]) % 256;
		swap(&s[i], &s[j]);
		int rnd = s[(s[i] + s[j]) % 256];
		cipherT[n] = rnd ^ plainT[n];
	}
}
int main(){
	unsigned char pT[1024] = {0};
	unsigned char cT[1024] = {0};
	struct sockaddr_in addr;

	int server_fd = socket(AF_INET, SOCK_STREAM, 0);
	addr.sin_family = AF_INET;
	addr.sin_port = htons(1337);
	addr.sin_addr.s_addr = inet_addr("127.0.0.1");

	bind(server_fd, (struct sockaddr*) &addr, sizeof(addr));
	listen(server_fd, 10);
	while(1){
		int addrlen = sizeof(addr);
		int new_s = accept(server_fd, (struct sockaddr*) &addr, &addrlen);

		read(new_s, pT, 1024);
		int n = strlen(pT);
		enc_(pT, cT, n);
		send(new_s, cT, strlen(cT), 0);

		close(new_s);
	}
	close(server_fd);
	return 0;
}
