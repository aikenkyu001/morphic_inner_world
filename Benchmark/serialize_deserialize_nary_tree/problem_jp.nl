# [幾何学的NL仕様]
タスク: serialize_deserialize_nary_tree

インターフェース: serialize(self, arg1)
論理フロー:
  入力: arg1
  1. 木直列化
  出力: 値返却

---

インターフェース: deserialize(self, arg1)
論理フロー:
  入力: arg1
  1. 木構造復元
  出力: 値返却
