y = int(input())
x = 3 + y
print(f"your answer is {x}")


x = int(input())
y = 4
if x == y:
    print("всё верно")
else:
    print(f"неверно. правильный ответ: {y}")


x = 'Добрый вечер, я - диспетчер'
if 'я' in x:
    print('Всё верно')
index = x.find("я")
if index != -1:
    print(f"Всё верно, это слово по индексу тут: {index}")


s = 'My Name is Julia'
if 'Name' in s:
    print('Substring found')
index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')