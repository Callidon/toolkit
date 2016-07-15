// Package bencode provides utilies to work with Bencode encoding format
// Bencode reference : https://en.wikipedia.org/wiki/Bencode
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
    strLength := bytes.SplitN(bencode, []byte(":"), 2)[0]
    length, _ := strconv.Atoi(string(strLength))
    return string(bencode[len(strLength)+1:]), length
}

// Deserialize a list of strings serialized using Bencode standard
// Reference : https://en.wikipedia.org/wiki/Bencode
func DeserializeList(bencode []byte) ([]string, int) {
	list := make([]string, 0)
	ind := 1
	for ind < len(bencode)-1 {
		strLength := bytes.SplitN(bencode[ind:], []byte(":"), 2)[0]
        length, _ := strconv.Atoi(string(strLength))
		elt, _ := DeserializeStr(bencode[ind : ind+length+1])
		list = append(list, elt)
		ind += length + 1 + len(strLength)
	}
	return list, len(list)
}
