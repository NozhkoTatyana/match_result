'''

Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

'''


n = int(input())
x_list = [input().split(';') for x in range(n)]
teams = set()
for i in range(len(x_list)):
    teams.add(x_list[i][0])
    teams.add(x_list[i][2])
score_table = {}
for team in teams:
    score_table[team] = [0, 0, 0, 0, 0]
for team1, goal1, team2, goal2 in x_list:
    score_table[team1][0] += 1
    score_table[team2][0] += 1
    if int(goal1) > int(goal2):
        score_table[team1][1] += 1
        score_table[team1][4] += 3
        score_table[team2][3] += 1
    elif int(goal2) > int(goal1):
        score_table[team2][1] += 1
        score_table[team2][4] += 3
        score_table[team1][3] += 1
    elif int(goal1) == int(goal2):
        score_table[team1][2] += 1
        score_table[team1][4] += 1
        score_table[team2][2] += 1
        score_table[team2][4] += 1
for key in score_table:
    print(key + ':', end='')
    print(*score_table[key])