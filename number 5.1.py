mas=int(input('Введите массу тела: '))
ros=int(input('Введите рост тела: '))
bmi=round((mas*10000)/(ros**2),2)
if bmi < 18.5:
    print('Индекс BMI равен ',bmi,' , диагностирован дефицит массы тела')
if 18.4 < bmi < 25.1:
    print('Индекс BMI равен ',bmi,' , все в порядке')
if 25.0 < bmi < 30.0:
    print('Индекс BMI равен ',bmi,' , диагностированно предожирение')
if 29.9 < bmi < 35.0:
    print('Индекс BMI равен ',bmi,' , диагностированно ожирение 1 степени')
if 34.9 < bmi < 40.1:
    print('Индекс BMI равен ',bmi,' , диагностированно ожирение 2 степени')
if bmi > 40.0:
    print('Индекс BMI равен ',bmi,' , диагностированно ожирение 3 степени')
########################
f=int(input('Если вам нужна справка введите 1 '))
if f==1:
    def index():
        """Эта штука выводит индекс BMI (Индекс массы тела) по весу тела и росту используя формулу BMI=m/r^2 где m - масса тела, а r - рост """
        pass
help(index)
