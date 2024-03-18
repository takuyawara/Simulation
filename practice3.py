#ランダムウォーク
import matplotlib.pyplot as plt
import random

# パラメータ
num_steps = 1000  # ステップ数
x, y = 0, 0  # 初期位置

# 移動の記録
x_positions = [x]
y_positions = [y]

# ランダムウォークの実行
for _ in range(num_steps):
    # ランダムな方向を選択
    direction = random.choice(['up', 'down', 'left', 'right'])

    # 移動
    if direction == 'up':
        y += 1
    elif direction == 'down':
        y -= 1
    elif direction == 'left':
        x -= 1
    elif direction == 'right':
        x += 1

    # 位置の記録
    x_positions.append(x)
    y_positions.append(y)

# 結果のプロット
plt.plot(x_positions, y_positions)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('2D Random Walk')
plt.show()
