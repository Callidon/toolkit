package bencode

import (
	"reflect"
	"testing"
)

var StrDatas = []string{
    "a",
    "16",
    "-125",
    "hello",
    "lot of spaces",
    ",;:!?./§ù*%µ<>&é(-è_çà)=~#{[|`\\^@]}",
}

func TestSerializeStr(t *testing.T) {
	for _, data := range StrDatas {
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
	serial := SerializeList(StrDatas)
	dserial, length := DeserializeList(serial)
	if reflect.DeepEqual(dserial, StrDatas) {
		t.Error("Error : expected ", StrDatas, " from deserialization, got ", dserial)
	}

	if length != len(StrDatas) {
		t.Error("Error : expected length = ", len(StrDatas), ", got ", len(dserial))
	}
}
