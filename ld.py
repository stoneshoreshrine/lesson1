pogoda = {'city': 'Moscow', 'temperature': 20}

print(pogoda['city'])

pogoda['temperature'] -= 5

print(pogoda)

print(pogoda.get('country', 'Russia'))

pogoda['date'] = '27.05.2019'

print(len(pogoda))