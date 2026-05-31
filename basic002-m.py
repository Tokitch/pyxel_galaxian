import pyxel

class App:
    def __init__(self):
        # pyxelの初期化
        #caption⇒title
        pyxel.init(160,120, title="グラフィック")

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


        for i in range(16):
            # x座標の設定
            x = i * 10
            # 数字の表示
            pyxel.text(x, 10, str(i) ,7)

            # ピクセルの表示
            # pix ⇒ pset
            pyxel.pset(x, 20, i)

            # 線の表示
            pyxel.line(x , 30, x + 8, 40, i)

            # 矩形の表示
            pyxel.rect(x, 50, 10, 10, i)
            
            # 円の表示
            pyxel.circ(x + 4, 80, 8, i)

        # 各キャラクタの描画処理
        pass

if __name__ == "__main__":
    App()