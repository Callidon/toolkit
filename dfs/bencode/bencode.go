package bencode

import (
	"bytes"
	"strconv"
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
	length, _ := strconv.Atoi(string(bencode[0]))
	return string(bencode[2:]), length
}

// Deserialize a list of strings serialized using Bencode standard
// Reference : https://en.wikipedia.org/wiki/Bencode
func DeserializeList(bencode []byte) ([]string, int) {
	list := make([]string, 0)
	ind := 1
	for ind < len(bencode)-1 {
		eltLength, _ := strconv.Atoi(string(bencode[ind]))
		elt, _ := DeserializeStr(bencode[ind : ind+eltLength+2])
		list = append(list, elt)
		ind += eltLength + 2
	}
	return list, len(list)
}
