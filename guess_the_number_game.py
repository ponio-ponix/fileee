import random
import sys

# random.randint

sys.stdout.buffer.write(b'please min number\n')
sys.stdout.flush()
min = sys.stdin.buffer.readline()

sys.stdout.buffer.write(b'please max number\n')
sys.stdout.flush()
max = sys.stdin.buffer.readline()

while min > max:
    print("最小値のほうが大きいので入力し直し")
    sys.stdout.flush()
    max = sys.stdin.buffer.readline()
print("最大値以下なので大丈夫")
print('最大値 ' + max.decode() + '最小値 ' + min.decode())

min = int(min)
max = int(max)

random_number = random.randint(min, max)
random_number = str(random_number)

print("最大値以下最小値以下の数字がランダムで設定されたのであててください")
print(random_number)
sys.stdout.flush()
answer = sys.stdin.buffer.readline().decode().strip()

while answer != random_number:
    print("ランダムな数字と一致しませんでした、もう一度入力してください")
    sys.stdout.flush()
    answer = sys.stdin.buffer.readline().decode().strip()
print("ランダムな数字は" + answer + "でした")