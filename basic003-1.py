import pyxel

class App:
    def __init__(self):
        # pyxelの初期化
        self.windowW = 160
        self.windowH = 120
        # 修正：pyxel.width と pyxel.heightでウィンドウのサイズは取得できる。
        pyxel.init(self.windowW, self.windowH, title="キー入力１")

        # 各キャラクタの準備
        self.keystat = "_"
        self.padstat = "_"
        self.x = 50
        self.y = 50
        self.Vel = 2
        # pyxelの実行
        # （フレーム更新時、描画時に呼ぶ関数の登録)
        pyxel.run(self.update, self.draw)
    
    def update(self):
        """ フレーム更新時の処理"""
        # キー入力チェック
        if pyxel.btn(pyxel.KEY_LEFT):
            self.keystat = "<"
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.keystat = ">"
        elif pyxel.btn(pyxel.KEY_UP):
            self.keystat = "^"
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.keystat = "v"
        
        # 修正：キー入力時は　dx, dy = 1 ,1　と変化を記述するようだけど、それをすると4方向しか動かなくなる
        if pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.padstat = "<"
            self.x -= self.Vel
        elif pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.padstat = ">"
            self.x += self.Vel
        
        if pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.padstat = "^"
            self.y -= self.Vel
        elif pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.padstat = "v"
            self.y += self.Vel
                
        # 各キャラクタの移動

        if self.x < 0:
            self.x = 0
        elif self.x > pyxel.width -10:
            self.x = pyxel.width -10

        # elif self.x > self.windowW -10:
        #     self.x = self.windowW -10
        
        if self.y < 0:
            self.y = 0
        elif self.y > pyxel.height -10:
            self.y = pyxel.height -10
        # elif self.y > self.windowH -10:
        #     self.y = self.windowH -10
        
        # 衝突判定
        

    def draw(self):
        """ 描画処理 """

        # 画面クリア(色番号)
        pyxel.cls(0)
        pyxel.text(10,10,"key:" + self.keystat +" / pad:" + self.padstat,7)

        # 各キャラクタの描画処理
        pyxel.rect(self.x,self.y,10,10,3)
    
if __name__ == "__main__":
    App()