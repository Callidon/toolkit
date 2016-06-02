package bencode

import (
	"bytes"
	"strconv"
	"strings"
)

// Serialize a string using Bencode standard
// Reference : https://en.wikipedia.org/wiki/Bencode
func SerializeStr(str string) []byte {
	return []byte(strconv.Itoa(len(str)) + ":" + str)
}

// Serialize a list of strings using Bencode standard
// Reference : https://en.wikipedia.org/wiki/Bencode
func SerializeList(list []string) []byte {
	var buffer bytes.Buffer
	buffer.WriteString("l")
	for _, elt := range list {
		buffer.Write(SerializeStr(elt))
	}
	buffer.WriteString("e")
	return buffer.Bytes()
}

// Deserialize a string serialized using Bencode standard
// Reference : https://en.wikipedia.org/wiki/Bencode
func DeserializeStr(bencode []byte) (string, int) {
	str := string(bencode)
	strLength := strings.Split(str, ":")[0]
	length, _ := strconv.Atoi(strLength)
	return str[len(strLength)+1:], length
}

// Deserialize a list of strings serialized using Bencode standard
// Reference : https://en.wikipedia.org/wiki/Bencode
func DeserializeList(bencode []byte) ([]string, int) {
	list := make([]string, 0)
	ind := 1
	str := string(bencode)
	for ind < len(bencode)-1 {
		strLength := strings.Split(str[ind:], ":")[0]
		length, _ := strconv.Atoi(strLength)
		elt, _ := DeserializeStr(bencode[ind : ind+length+1])
		list = append(list, elt)
		ind += length + 1 + len(strLength)
	}
	return list, len(list)
}
