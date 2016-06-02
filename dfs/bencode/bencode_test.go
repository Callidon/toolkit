package bencode

import (
	"reflect"
	"testing"
)

func TestSerializeStr(t *testing.T) {
	var datas = []string{
		"a",
		"16",
		"-125",
		"hello",
		"lot of spaces",
		",;:!?./§ù*%µ<>&é(-è_çà)=~#{[|`\\^@]}",
	}

	for _, data := range datas {
		serial := SerializeStr(data)
		dserial, length := DeserializeStr(serial)
		if dserial != data {
			t.Error("Error : expected '", data, "' from deserialization, got ", dserial)
		}

		if length != len(data) {
			t.Error("Error : expected length = ", len(data), ", got ", len(dserial))
		}
	}
}

func TestSerializeList(t *testing.T) {
	var datas = [][]string{
		[]string{"a", "hello", "lot of spaces", ",;:!?./§ù*%µ<>&é(-è_çà)=~#{[|`\\^@]}"},
		[]string{"1", "-15"},
	}
	for _, data := range datas {
		serial := SerializeList(data)
		dserial, length := DeserializeList(serial)
		if reflect.DeepEqual(dserial, data) {
			t.Error("Error : expected ", data, " from deserialization, got ", dserial)
		}

		if length != len(data) {
			t.Error("Error : expected length = ", len(data), ", got ", len(dserial))
		}
	}

}
