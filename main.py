import sys, os
sys.path.append("../PollutionCreater_TimeChange")

import importlib

import Pollution
importlib.reload(Pollution)
from Pollution import Pollution

import matplotlib.pyplot as plt

import random

import pandas as pd


def CreateGraphObject():
    fig = plt.figure()
    graph_object = fig.add_subplot(111)
    return graph_object





########################　メインルーチン ##########################################
def main():



    #本プログラムでは、Pollutionクラスの使い方について説明したいと思います
    #1.濃度分布モデルを2次元リストの形で作成します
    #2.作成した濃度分布モデルをPollutionクラスのコンストラクタに渡します
    #3.作成した濃度値の値をAddメソッドやAdjustValueRangeメソッドで調整します(AdjustValueRangeは3Dモデルのみにつけています。なので本プログラムでは紹介しません）
    #4.濃度分布を正しくつくることができているかどうか、Viewメソッドで確認します
    #5.作成したモデルをSaveメソッドで保存します
    #6.濃度分布モデルの上に、移動経路を描画する方法を最後に紹介します

#-------------　モデルを2次元リストで作成する　---------------------------------



    #モデルのサイズを設定
    x_end = 50
    y_end = 50




#-- 全ての位置の濃度値がゼロのモデルを作成する -------------------

    #2次元のリストを作成（「リスト内包表記」で作成。詳しくはWebで)
    zeroPollutions = [[0 for y in range(y_end)] for x in range(x_end)]
    #作成したリストをPollutionクラスのコンストラクタへ
    zeroPollutionField = Pollution(zeroPollutions)
    #画用紙オブジェクト（グラフオブジェクト）を作成
    graph_object = CreateGraphObject()
    #濃度分布を描画（なにもない真っ白なモデルが表示される)
    graph_object = zeroPollutionField.View(graph_object)
#-------------------------------------------------------------





#-- 位置によって濃度値がバラバラなモデルを作成する ----------------

    #random.uniformは指定した範囲内でランダムな値を生成する
    randomPollutions = [[random.uniform(0, 100) for y in range(y_end)] for x in range(x_end)]
    randomPollutionField = Pollution(randomPollutions)
    graph_object = CreateGraphObject()
    graph_object = randomPollutionField.View(graph_object)
#--------------------------------------------------------







#-- Addメソッドを使い、濃度分布モデルどうしを足し合わせる -----------

    #もともとのモデルに足し合わせるための、新たなモデルを生成
    addPollutions = [[random.uniform(0, 100) for y in range(y_end)] for x in range(x_end)]
    addPollutionField = Pollution(addPollutions)
    #さきほど作成したモデルにaddPollutionFieldを加算する
    randomPollutionField.Add(addPollutionField)
    #任意で濃度値の上限値を設定する（探索プログラムが組みやすくなる）
    #モデルどうしを足し合わせ、また、値の調整を行ったあとの分布を表示
    graph_object = CreateGraphObject()
    graph_object = randomPollutionField.View(graph_object)
#------------------------------------------------------------






#-- Saveメソッドで、作成したモデルを保存 ----------------------

    #実際に、保存したファイルを開いてみてください。
    #csvファイルはただ開くだけで内容が分かりますがpklファイルは専用の関数で読み取る必要があります
    randomPollutionField.Save("SaveTest/sample.csv")
    randomPollutionField.Save("SaveTest/sample.pkl")

    #pkl(pickle)データの読み出し
    print("濃度保存ファイルの内容を表示します")
    print(pd.read_pickle("SaveTest/sample.pkl"))
#------------------------------------------------------------







#-- 移動経路を描画 ---------------------------------------------

    #Viewメソッドで返却されたgraph_objectに散布図(scatter)を上書き
    xList = [0, 5, 10]
    yList = [10, 20, 30]
    graph_object.scatter(xList, yList, c = 'red', alpha = 1) #alphaは透明度
    #対応する座標位置に赤い点が表示されます
#-------------------------------------------------------------






if __name__ == "__main__":
    main()
