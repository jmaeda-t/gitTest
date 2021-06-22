# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:15:41 2021

@author: jmaeda
"""

from PyQt5 import QtWidgets
import qt_MainWindowUI
import is_weather

class MainWindow(QtWidgets.QMainWindow):
    """ 複数行コメント　MainWindowクラス
    QtWidgets.QmainWindowsを継承したサブクラスUI画面の構築を行う
    
    Attribute:
        ui(obj):Ui_MainWindowsオブジェクトを保持する。
        weather(obj):WeatherResponderオブジェクトを保持する
        place(str):天気予報の地域名を保持する
        id(int):天気予報の地域名に連動したidを保持する。
    
    """
    def __init__(self):
        """初期化の処理を行う
        
        ・スーパークラスの__init__()を呼び出す
        ・WeatherResponderオブジェクトを生成
        ・ファイル名から地域名とidのリストを作成
        ・Ui_MainWindowのsetupUi()を実行してUI画面を構築する
        ・ラジオボタンのテキストを初期化
        ・地域名とidの初期値をセット
        """
        super().__init__()
        # QMainWindowクラスの__init__()を実行
        self.ui = qt_MainWindowUI.Ui_MainWindow()
        # UI_MainWindowを生成
        self.weather = is_weather.WeatherResponder()
        # WeatherResponderを生成
        self.initInfo()
        # 地域名とidのリストを作成
        self.ui.setupUi(self)
        # setupUi()で画面を構築。MainWindow自信を引数にすることが必要
        self.initRadioButton()
        # ラジオボタンのテキストを初期化
        self.place = self.place_list[0]
        # 地域名の初期値をセット
        self.id = self.id_list[0]
        # idの初期値をセット
        
    def initInfo(self):
        """ファイルを読み込み、地域名とid番号のリストを作成する
        """
        # タブ区切りのデータファイルを読み取りモードで開く
        with open('data/place_code.txt', 'r', encoding = 'utf_8') as file:
            lines = file.readlines()
            # 一括して読み込んで1行分を1要素とするリストにする
            
        new_lines = []
        # 末尾の開業を除いた行データを保持するリスト
        for line in lines:
        # データリストから1行データを取り出す
            line = line.rstrip('\n')
            # 末尾の改行文字を取り除く
            if (line!=''):
                new_lines.append(line)
                # 空文字でないときはリストnew_linesに追加
                
        self.place_list = []
        # 行データの地域名を要素にするリスト
        self.id_list = []
        # 行データのidを要素にするリスト
        for line in new_lines:
        # 改行を削除したリストから1行データを取り出す
            place, id = line.split('\t')
            # タブで分割して地域名とidを各変数にセット
            self.place_list.append(place)
            # 地域名をplace_listに追加する。
            self.id_list.append(id)
            # idをid_listに追加する
            
    def initRadioButton(self):
        """ ラジオボタンのテキストを初期化する
        """
        for i in range(0, 8):
            # self.ui.radiobuttonに1から8までの番号を連結し、ラジオボタンの識別名をつくる
            objName = 'self.ui.radioButton_' + str(i+1) + '.setText'
            # eval()でobjnameの文字列をコード化し
            # すべての羅時をボタンのテキストをPlace_listのテキスト名にする。
            eval(objName)(self.place_list[i])
            
    def pushButtonSlot(self):
        """「天気予報を取得」ボタンのイベントハンドラー
        ・WeatherResponderクラスのget_weather()を実行して応答メッセージを取得
        ・取得した天気予報をラベルに出力
        """
        # 選択されたラジオボタンの情報を使って天気予報を取得する
        response = self.weather.get_weather(self.place, self.id)
        # 取得した情報をラベルに出力
        self.ui.labelResponce.setText(response)
        
    def clearButtonSlot(self):
        """「表示クリア」ボタンのイベントハンドラー
        ・ラベルの内容をクリアする
        """
        self.ui.labelResponce.clear()
        
    def colseEvent(self, event):
        """ウィジェットの「閉じる」イベントでコールされるイベントハンドラー
        ウィジェットを閉じるclose()メソッドの実行時にQCloseEventによって呼ばれる
        
        Overrides:
            ・メッセージボックスを表示する
            ・［Yes］がクリックされたらイベントを続行してウィジェットを閉じる
            ・［No］がクリックされたらイベントを取り消してウィジェットを閉じないようにする
            
        Parameters:
            event(QCloseEvent):「閉じる」イベント発生時に渡されるQCloseEventオブジェクト
        """
        # メッセージボックスを表示
        reply = QtWidgets.QMessageBox.question(
            self, '確認', "終了しますか", 
            buttons = QtWidgets.QMessageBox.Yes | 
            QtWidgets.QMessageBox.No)
        # [Yes]クリックでウィジェットを閉じ、「No」クリックで閉じる処理を無効にする
        
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept() # イベントを続行しcloseする
        else:
            event.ignore() # イベントを取り消してUI画面に戻る
            
    def r_buttonSlot1(self):
        """１番目ラジオボタンがオンにされたときの処理
        """
        self.place = self.place_list[0]
        self.id = self.id_list[0]
        
    def r_buttonSlot2(self):
        """2番目の羅時をボタンがONにされたときの処理
        """
        self.place = self.place_list[1]
        self.id = self.id_list[1]
        
    def r_buttonSlot3(self):
        """３番目の羅時をボタンがONにされたときの処理
        """
        self.place = self.place_list[2]
        self.id = self.id_list[2]
       
    def r_buttonSlot4(self):
        """４番目の羅時をボタンがONにされたときの処理
        """
        self.place = self.place_list[3]
        self.id = self.id_list[3]
       
    def r_buttonSlot5(self):
        """５番目の羅時をボタンがONにされたときの処理
        """
        self.place = self.place_list[4]
        self.id = self.id_list[4]
       
    def r_buttonSlot6(self):
        """６番目の羅時をボタンがONにされたときの処理
        """
        self.place = self.place_list[5]
        self.id = self.id_list[5]
       
    def r_buttonSlot7(self):
        """７番目の羅時をボタンがONにされたときの処理
        """
        self.place = self.place_list[6]
        self.id = self.id_list[6]
       
    def r_buttonSlot8(self):
        """８番目の羅時をボタンがONにされたときの処理
        """
        self.place = self.place_list[7]
        self.id = self.id_list[7]
