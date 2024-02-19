import sys
# print(len(sys.argv))

def validate_input(input_value):
    arg3 = input_value[1]
    list_length = len(input_value)

    if arg3 == "reserve" and list_length == 4:
        return True
    elif arg3 == "copy" and list_length == 4:
        return True
    elif arg3 == "duplicate-contents" and list_length == 4:
        return True
    elif arg3 == "replace-string" and list_length == 5:
        return True



while True:
    if validate_input(sys.argv):
        print("バリデーションチェックはOKです")
        break
    else:
        print("バリデーション的にダメなので入力し直してください")
        input()

input_file =  sys.argv[2]
if len(sys.argv) > 3:
    output_file = sys.argv[3]


def reverse_file_content():
    with open(input_file, 'r') as file:
        reversed_lines = reversed(file.readlines())


    with open(output_file, 'w') as file:
        for line in reversed_lines:
            file.write(line)

# コマンドの内容は下記で取得できる

# python3 file_manipulator.py reverse python_practice/data/test.txt python_practice/dump/test-dumb.txt
# ファイル名をコマンドライン引数から取得
command = sys.argv[1]
if command == "reserve":
    reverse_file_content()
elif command == "copy":
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            file.write(line)


elif command == "duplicate-contents":
    number_Reproductions = int(sys.argv[3])

    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(input_file, 'w') as file:
        for _ in range(number_Reproductions):
            for line in lines:
                file.write(line)
elif command == "replace-string":
    with open(input_file, 'r') as file:
        content = file.read()
        # fileの中で文字列を繰り返し探す

    with open(input_file, 'w') as file:
        content = content.replace(sys.argv[3], sys.argv[4])
        file.write(content)

