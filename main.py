# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:00:48 2021

@author: jmaeda
"""

import sys
from PyQt5 import QtWidgets
import mainWindow

# このファイルが直接実行された場合に以下の処理を行う
if __name__ == '__main__':
    # QApplication()はウインドウシステムを初期化し、
    # コマンドライン引数を使用してアプリケーションオブジェクトを構築する
    app = QtWidgets.QApplication(sys.argv)
    
    # 画面を構築するMainWindowクラスのオブジェクトを生成
    win = mainWindow.MainWindow()
    
    # メインウインドウを表示
    win.show()
    
    # イベントループを開始、プログラムが終了するまでイベントループを維持
    # 終了時には０が返される
    ret = app.exec_()
    
    # exec_()の戻り値を巣ステムに返してプログラムを終了する。
    sys.exit(ret)
    