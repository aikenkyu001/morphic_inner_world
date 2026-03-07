# [幾何学的NL仕様]
タスク: activity_selection
インターフェース: maxActivities(self, arg1)

論理フロー:
  入力: arg1
  1. 終了時間ソート
  2. 重複排除選択
  出力: リスト長返却
