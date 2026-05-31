import pyxel

class App:
    def __init__(self):
        # pyxelの初期化
        pyxel.init(160,120, title="基本")

        # 各キャラクタの準備
        self.x = 80
        self.y = 60
        self.move_size = 3

        # pyxelの実行
        # （フレーム更新時、描画時に呼ぶ関数の登録)
        pyxel.run(self.update, self.draw)
    
    def update(self):
        """ フレーム更新時の処理"""
        # キー入力チェック
        if pyxel.btn(pyxel.KEY_LEFT):
            dx , dy = -1 , 0
        elif pyxel.btn(pyxel.KEY_RIGHT):
            dx , dy = 1 , 0
        elif pyxel.btn(pyxel.KEY_UP):
            dx , dy = 0 , -1
        elif pyxel.btn(pyxel.KEY_DOWN):
            dx , dy = 0 , 1
        else:
            return
        # 各キャラクタの移動
        self.x += dx * self.move_size
        self.y += dy * self.move_size
        
        # 衝突判定
        if self.x < 0:
            self.x = 0
        if self.x + 10 > pyxel.width:
            self.x = pyxel.width - 10
        
        if self.y < 0:
            self.y = 0
        if self.y + 10 > pyxel.height:
            self.y = pyxel.height -10

    def draw(self):
        """ 描画処理 """

        # 画面クリア(色番号)
        pyxel.cls(0)

        # 各キャラクタの描画処理
        pyxel.rect(self.x,self.y, 10 ,10 ,14)

if __name__ == "__main__":
    App()