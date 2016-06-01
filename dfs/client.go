package main

import (
	"fmt"
    "net"
    "bufio"
    "os"
)

func main() {
	conn, err := net.Dial("tcp", ":8080")
    if err != nil {
        fmt.Errorf("Error connecting ", err.Error())
    }
    defer conn.Close()
	// read in input from stdin
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Text to send: ")
	text, _ := reader.ReadString('\n')
	// send to socket
	fmt.Fprintf(conn, text)
	// listen for reply
	message, _ := bufio.NewReader(conn).ReadString('\n')
	fmt.Print("Message from server: " + message)
}
