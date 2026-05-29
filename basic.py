import pyxel

class App:
    def __init__(self):
        # pyxelの初期化
        pyxel.init(160,120, caption="基本")

        # 各キャラクタの準備

        # pyxelの実行
        # （フレーム更新時、描画時に呼ぶ関数の登録)
        pyxel.run(self.update, self.draw)
    
    def update(self):
        """ フレーム更新時の処理"""
        # キー入力チェック
        # 各キャラクタの移動
        # 衝突判定
        pass

    def draw(self):
        """ 描画処理 """

        # 画面クリア(色番号)
        pyxel.cls(0)

        # 各キャラクタの移動
        pass

if __name__ == "__main__":
    App()