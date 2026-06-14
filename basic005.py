import pyxel

class App:
    def __init__(self):
        # pyxelの初期化
        pyxel.init(160,120, title="パクパックン")

        # 各キャラクタの準備
        # リソースファイルのキャラクタ読み込み
        pyxel.load("my_resource.pyxres")

        self.x, self.y = 80, 60
        self.move_size = 1
        self.dir = 1        # 1:左 2:右 3:上 4:下
        self.type = 0       # 0:口を閉じてる 1:口を開いてる

        # pyxelの実行
        # （フレーム更新時、描画時に呼ぶ関数の登録)
        pyxel.run(self.update, self.draw)
    
    def update(self):
        """ フレーム更新時の処理"""
        # キー入力チェック
        if pyxel.btn(pyxel.KEY_LEFT):
            dx, dy = -1, 0
            self.dir = 1
        elif pyxel.btn(pyxel.KEY_RIGHT):
            dx, dy = 1, 0
            self.dir = 2
        elif pyxel.btn(pyxel.KEY_UP):
            dx, dy = 0, -1
            self.dir = 3
        elif pyxel.btn(pyxel.KEY_DOWN):
            dx, dy = 0, 1
            self.dir = 4
        else:
            return

        #描画するキャラクタの選択
        if pyxel.frame_count % 3 == 0:
            self.type = 1 - self.type # self.typeが1の時は0に、0の時は1に切り替わる

        # 各キャラクタの移動
        self.x += dx * self.move_size
        self.y += dy * self.move_size 

        # 衝突判定
        #画面端との衝突判定
        if self.x < 0:
            self.x = 0
        if self.x + 8 > pyxel.width:
            self.x = pyxel.width -8
        if self.y < 0:
            self.y = 0
        if self.y + 8 > pyxel.height:
            self.y = pyxel.height - 8
        
    def draw(self):
        """ 描画処理 """

        # 画面クリア(色番号)
        pyxel.cls(0)

        # 各キャラクタの描画処理
        if self.dir == 1: #右 = x軸反転表示
            pyxel.blt(self.x, self.y, 0, self.type * 8, 0, -8, 8)
        elif self.dir == 2: #左
            pyxel.blt(self.x, self.y, 0 , self.type * 8, 0, 8, 8)
        elif self.dir == 3: #上 = y軸反転表示
            pyxel.blt(self.x, self.y, 0,self.type * 8 , 8, 8,-8)
        elif self.dir == 4: #下
            pyxel.blt(self.x, self.y, 0, self.type * 8, 8 , 8, 8)
            
if __name__ == "__main__":
    App()