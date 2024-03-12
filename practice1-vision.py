#感染症の拡散モデル
#コンストラクタ→インスタンスの初期化に使用される
#self→クラス内のメソッドでインスタンス自身を参照できる
#abs関数→絶対値をケイsンするための関数
#クラス内のdef→メソッド(クラス関数),クラス外のdef→関数
import random
import matplotlib.pyplot as plt

class Agent:
    def __init__(self):
        self.status = "healthy"
        self.x = random.randint(0, 30)
        self.y = random.randint(0, 30)

    def move(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])

        if self.x<0:
            self.x=0
        elif self.x>30:
            self.x=30
        elif self.y < 0:
            self.y = 0
        elif self.y>30:
            self.y=30

    #infect→感染
    def infect(self, other_agents):
        if self.status == "infected":
            for agent in other_agents:
                if agent.status == "healthy" and self.is_close(agent):
                    agent.status = "infected"

    #他のエージェントと近いかどうかを判定する
    #返り値はTrue,Falseになる
    def is_close(self, other_agent):
        return abs(self.x - other_agent.x) <= 1 and abs(self.y - other_agent.y) <= 1

# シミュレーションの設定
num_agents = 50
agents = [Agent() for _ in range(num_agents)]
""""↑解説
Agent()→Agentクラスの新しいインスタンス生成
for _in range(num_agents)→num_agents回繰り返す。
全体として→Agent()をnum_agents回繰り返して新しいインスタンスを作成し、リストにまとめる。
　　　　　→今回でいえば10個のインスタンスを生成していることになる。
"""
#初期感染者
agents[0].status = "infected"
agents[1].status = "infected"
agents[2].status = "infected"

# シミュレーションの実行
for step in range(30):
    plt.clf() #グラフをクリア
    plt.xlim(0,30)
    plt.ylim(0,30)
    plt.title(f"Step {step}")

    for agent in agents:
        agent.move()
        agent.infect(agents)
        color="green" if agent.status == "healthy" else "red"
        plt.scatter(agent.x,agent.y,color=color)
        """↑解説
        scatter関数を使用してエージェントの位置をプロット(グラフに点を書き込む)している。
        moveとinfect,colorをscatterで表している
        """
    plt.pause(0.5)

#シミュレーションの表示
plt.show()

#感染者の結果の表示

HealthyPerson=0
InfectPerson=0

for agent in agents:
    if agent.status=="healthy":
        HealthyPerson+=1
    elif agent.status=="infected":
        InfectPerson+=1
print(f"健康な人は{HealthyPerson}人,感染した人は{InfectPerson}人です。")


