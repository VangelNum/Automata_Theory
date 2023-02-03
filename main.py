print("Выберите действие: \n"
      # "1) Ввод значений всех логических условий \n"
      # "2) Последовательный ввод значений \n"
      # "3) Вывод всех возможных результатов \n"
      "4) Ввести ЛСА \n"
      "Ваш выбор:"
      )


def isCorrect(LSA):
    if len(LSA) < 4:
        print("Строка не может содержать меньше 4 символов")
        return -1
    if LSA[0] != "Y" or LSA[1] != "H":
        print("Строка должна начинаться на YH")
        return -1
    if LSA[len(LSA) - 2] != 'Y' or LSA[len(LSA) - 1] != 'K':
        print("Строка должна заканчиваться на YK")
        return -1
    return 0


LSA = "YHHD1X0U1Y1Y3D2X1U5Y3WU3D5Y2D3Y1X2U2Y4YK"
buffer = []

if isCorrect(LSA) == -1:
    print("Введите другое LSA")
    LSA = input()
    while isCorrect(LSA) != 0:
        print("Введите другое LSA")
        LSA = input()

for i in range(len(LSA)):
    str = ""

    if LSA[i] == "Y" or LSA[i] == "X" or LSA[i] == "D" or LSA[i] == "U" or LSA[i] == "W":
        str = str + LSA[i]
        j = i + 1
        for k in range(j, len(LSA), 1):
            if LSA[k] != "Y" and LSA[k] != "X" and LSA[k] != "D" and LSA[k] != "U" and LSA[k] != "W":
                str = str + LSA[k]
            else:
                break
        buffer.append(str)
    else:
        if LSA[i] != 'H' and LSA[i] != 'K' and not (LSA[i].isdigit()):
            raise Exception("Invalid symbol" + LSA[i])

# print(buffer)
i = 0
FSA = 0

while i < len(buffer):
    if "X" in buffer[i]:
        index = buffer[i][1:len(buffer[i])]
        print("Введите значение X" + index + ": ")
        FSA = input()
        print("Выполняется X" + index)
    if "U" in buffer[i] and int(FSA) == 0:
        index = buffer[i][1:len(buffer[i])]
        for j in range(len(buffer)):
            if "D" + index == buffer[j]:
                i = j
    if "Y" in buffer[i]:
        index = buffer[i][1:len(buffer[i])]
        print("Выполняется Y" + index)
    i = i + 1
