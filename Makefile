all: httpd

httpd: httpd.c
	gcc -o httpd httpd.c -lpthread -W -Wall
#gcc -W -Wall -lsocket -lpthread -o httpd httpd.c

clean:
	rm httpd
