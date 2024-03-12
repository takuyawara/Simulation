#感染症の拡散モデル
#コンストラクタ→インスタンスの初期化に使用される
#self→クラス内のメソッドでインスタンス自身を参照できる
#abs関数→絶対値をケイsンするための関数
#クラス内のdef→メソッド(クラス関数),クラス外のdef→関数
import random

class Agent:
    def __init__(self):
        self.status = "healthy"
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])

    #infect→感染
    def infect(self, other_agents):
        if self.status == "infected":
            for agent in other_agents:
                if agent.status == "healthy" and self.is_close(agent):
                    agent.status = "infected"

    #他のエージェントと近いかどうかを判定する
    #返り血はTrue,Falseになる
    def is_close(self, other_agent):
        return abs(self.x - other_agent.x) <= 1 and abs(self.y - other_agent.y) <= 1

# シミュレーションの設定
num_agents = 10
agents = [Agent() for _ in range(num_agents)]
""""↑解説
Agent()→Agentクラスの新しいインスタンス生成
for _in range(num_agents)→num_agents回繰り返す。
全体として→Agent()をnum_agents回繰り返して新しいインスタンスを作成し、リストにまとめる。
　　　　　→今回でいえば10個のインスタンスを生成していることになる。
"""
agents[0].status = "infected"  # 初期感染者

# シミュレーションの実行
for step in range(20):
    for agent in agents:
        agent.move()
        agent.infect(agents)

    # 状態の表示
    statuses = [agent.status for agent in agents]
    print(f"Step {step}: {statuses}")
