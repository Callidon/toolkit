package bencode

import "testing"

func TestSerializeStr(t *testing.T) {
  sref := SerializeStr("hello")
  dsref, length := DeserializeStr(sref)
  if dsref != "hello" {
      t.Error("Error : expected 'hello' from deserialization, got ", dsref)
  }

  if length != 5 {
      t.Error("Error : expected length = 5, got ", dsref)
  }
  //fmt.Println(DeserializeString(stest))
  //test := []string{"toto", "momo", "lolo"}
  //stest := SerializeList(test)
  //fmt.Println(DeserializeList(stest))
}
