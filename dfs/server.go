package main

import (
	"fmt"
	"net"
	"os"
    "strings"
)

const (
	CONN_HOST = "localhost"
	CONN_PORT = "8080"
	CONN_TYPE = "tcp"
)

func handleConnection(conn net.Conn) {
	// buffer to hold incoming data
	buf := make([]byte, 1024)
	defer conn.Close()
	fmt.Println("New client connected")
	// read incoming data
	reqLen, err := conn.Read(buf)
	if err != nil {
		fmt.Errorf("Error reading : ", err.Error())
	}
    message := strings.Trim(string(buf[0:reqLen]), "\n")
    fmt.Println("Message from client : '", message, "'")
	conn.Write([]byte("Hello you handsome devil\n"))
}

func main() {
	fmt.Println("hello from server")

	ln, err := net.Listen(CONN_TYPE, ":"+CONN_PORT)
	if err != nil {
		fmt.Errorf("Error : ", err.Error())
		os.Exit(1)
	}
	defer ln.Close()
	fmt.Println("server running on port 8080")
	for {
		conn, err := ln.Accept()
		if err != nil {
			fmt.Errorf("Error : ", err.Error())
		}
		go handleConnection(conn)
	}
}
