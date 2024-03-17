#群れのシミュレーション(ボイドの法則)

#1.分離(Separation):他の個体との距離を保つ
#2.整列(Alignment):近くの個体と同じ方向に移動する
#3.結合(Cohesion):近くの個体の中心に向かって移動する
#numpy→機械学習の計算をより早く、効率的に行えるようにする拡張モジュール
#matplotlib→numpyのためのグラフ描写ライブラリ

import numpy as np
import matplotlib.pyplot as plt

class Boid:
    def __init__(self, x, y, vx, vy):
        self.position = np.array([x, y])
        #velocity→速度
        self.velocity = np.array([vx, vy])
        self.speed_limit = 2.0
        """↑解説
        ・np.array()→リストやタプルなどを受け取り、numpyの配列に変換する関数。2次元空間上の点やベクトルを表現する
        ・self.positionなどはインスタンス変数
        """

    def update(self, boids):
        # 分離
        separation_force = np.zeros(2)
        # 整列
        alignment_force = np.zeros(2)
        # 結合
        cohesion_force = np.zeros(2)

        """↑解説
        ・np.zeros→ライブラリの関数。全ての要素が0の配列を生成する。
        今回の場合2つの要素をもつ1次元配列を生成。要素は0
        ・boidは多分ボイドの法則からきてる
        """

        for boid in boids:
            #ベクトルのノルム(大きさ)を計算する。ユークリッド距離を出せる。
            distance = np.linalg.norm(self.position - boid.position)
            #この部分で比べるべきエージェントを絞っている
            if distance > 0 and distance < 10:
                #分離:他のエージェントから離れようとする力が生まれる
                separation_force += self.position - boid.position
                """↑解説
                ・selfと他のエージェント(boid)との距離を基にして力を計算している。
                　self→updateメソッドで呼び出しているエージェント
                """
                #整列:周囲のエージェントと速度(方向)を合わせようとする力が生まれる
                alignment_force += boid.velocity
                #結合:エージェントを近くのエージェントの平均位置に引き寄せる
                cohesion_force += boid.position
            """↑解説
            ・各エージェントが知覚のエージェントに対して上記3つの行動をとるように制限している。
            一定の範囲内のエージェントにのみ反応するようになる。
            """

        #分離力の平均化→分離力が群れの密度によって調整される。
        separation_force /= len(boids)
        #整列力の平均化→エージェントの群れの平均的な移動方向に合わせようとする。
        alignment_force /= len(boids)
        #エージェントが群れの中心に向かって移動するように
        cohesion_force /= len(boids)
        #計算された群れの中心から現在のエージェントの位置を引く
        cohesion_force = cohesion_force - self.position
        """↑解説
        ・群れ全体について計算している
        個々人で動かないようにするため
        ・len()関数はリストの長さ(要素の数)を返す
        """

        # 速度の更新
        self.velocity += separation_force + alignment_force + cohesion_force
        # 速度制限
        if np.linalg.norm(self.velocity) > self.speed_limit:
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * self.speed_limit

        # 位置の更新
        self.position += self.velocity

def main():
    num_boids = 50
    boids = [Boid(np.random.rand() * 100, np.random.rand() * 100,
                  np.random.rand() * 2 - 1, np.random.rand() * 2 - 1) for _ in range(num_boids)]

    #matplotlibライブラリを使ったグラフ描写において、新しい図を作成するための関数
    plt.figure()
    for _ in range(100):
        #現在の図をクリアするための関数(前の情報を消す)
        plt.clf()
        for boid in boids:
            boid.update(boids)
            """↑解説
            エージェント自身(self)と他のすべてのエージェント(boidsリスト)を引数として受け取る。
            """
            #エージェントの位置をプロットしている
            plt.plot(boid.position[0], boid.position[1], 'bo')
            """↑解説
            ・boはマーカーのスタイルを指定している(青色の⑩)
            """
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)
        plt.pause(0.1)
    plt.show()

if __name__ == "__main__":
    main()
