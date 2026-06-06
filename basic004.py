import pyxel
import random

class App:
    def __init__(self):
        # pyxelの初期化
        pyxel.init(160,120, title="マウスから★の誕生")
        # マウスカーソルの表示★
        pyxel.mouse(True)
        # 各キャラクタの準備
        #★の位置を配列で持つため、空のリストを用意する
        self.star = []

        # pyxelの実行
        # （フレーム更新時、描画時に呼ぶ関数の登録)
        pyxel.run(self.update, self.draw)
    
    def update(self):
        """ フレーム更新時の処理"""
        # キー入力チェック
        # 各キャラクタの移動
        if len(self.star)< 100: 
            #リストの長さが100未満なら新たに星を追加する
            vx = vy = 0
            while vx ==0 and vy == 0:
                # vx,vyいずれかが0でなくなるまで設定しなおす
                # 両方ゼロだと星が動かない
                vx = random.randint(-3, 3)
                vy = random.randint(-3, 3)
            col = random.randint(0 ,15)
            #現在の星の位置（マウスの位置）、スピード、色をリストで追加する
            self.star.append([
                pyxel.mouse_x,
                pyxel.mouse_y,
                vx,
                vy,
                col
            ])
        # 衝突判定
        # と移動処理
        for i in range(len(self.star)-1, -1, -1): #開始,終了,ステップ
            x, y, vx, vy, col = self.star[i]
            x += vx
            y += vy
            if x < 0 or x >= pyxel.width or\
                y < 0 or y >= pyxel.height:
                # 画面の端に来たら★を消す（pop)
                self.star.pop(i)
            else:
                #位置情報の更新
                self.star[i][0] = x
                self.star[i][1] = y

    def draw(self):
        """ 描画処理 """
        # 画面クリア(色番号)
        pyxel.cls(0)

        # 各キャラクタの描画処理
        for i in range(0,len(self.star)):
            x, y, vx, vy, col = self.star[i]
            pyxel.pset(x,y,col)


if __name__ == "__main__":
    App()