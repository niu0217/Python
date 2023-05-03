import random

"""
函数功能：将华氏温度转换为摄氏温度
华氏温度转摄氏温度的公式：C = (F - 32) / 1.8
"""
def Example1():
    f = float(input('输入华氏温度：'))
    c = (f - 32) / 1.8
    print('%.1f 华氏度 = %1.f 摄氏度' % (f, c))


"""
函数功能：半径计算圆的周长和面积
"""
def Example2():
    radius = float(input('请输入圆的半径： '))
    perimeter = 2 * 3.1416 * radius  # 周长
    area = 3.14156 * radius * radius  # 面积
    print('周长：%.2f' % perimeter)
    print('面积：%.2f' % area)


"""
函数功能：一元一次函数
"""
def Example3():
    x = int(input('请输入x：'))
    y = 2 * x + 1
    print('f(%d) = %d' % (x, y))


"""
函数功能：二元二次函数
f(x, y) = 2x^2 + 3y^2 + 4xy
"""
def Example4():
    x = int(input('请输入x：'))
    y = int(input('请输入y：'))
    z = 2 * x ** 2 + 3 * y ** 2 + 4 * x * y
    print('f(%d, %d) == %d' % (x, y, z))


"""
函数功能：分离整数个位数
"""
def Example5():
    x = int(input('请输入x：'))
    single_dig = x % 10
    exp_single_dig = x // 10  # 整除
    print('个位数：%d' % single_dig)
    print('其余：%d' % exp_single_dig)


"""
函数功能：累加器 v1.0
"""
def Example6():
    s = 0
    x = int(input('输入整数：'))
    s += x
    x = int(input('输入整数：'))
    s += x
    x = int(input('输入整数：'))
    s += x
    print('总和：%d' % s)


"""
函数功能：判断闰年
"""
def Example7():
    year = int(input('请输入年份：'))
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    print(is_leap)


"""
函数功能：判断奇偶数
"""
def Example8():
    in_x = int(input('输入整数：'))
    if in_x % 2 == 0:
        print('偶数')
    else:
        print('奇数')


"""
函数功能：猜大小
用户输入一个 1-6 之间的整数，与程序随机生成的数字作比较
"""
def Example9():
    x = int(input('请输入x：'))
    y = random.randint(1, 6)  # 产生1到6的随机数
    print('程序随机数： %d' % y)
    if x > y:
        print('用户赢')
    elif x < y:
        print('程序赢')
    else:
        print('打平')


"""
函数功能：摄氏度与华氏度互换
"""
def Example11():
    trans_type = input('输入转摄氏度还是华氏度：')

    if trans_type == '摄氏度':  # 执行华氏度转摄氏度的逻辑
        f = float(input('输入华氏温度：'))
        c = (f - 32) / 1.8
        print('摄氏温度为：%.2f' % c)
    elif trans_type == '华氏度':  # 执行摄氏度转华氏度的逻辑
        c = float(input('输入摄氏温度：'))
        f = c * 1.8 + 32
        print('华氏温度为：%.2f' % f)
    else:
        print('请输入 华氏度 或 摄氏度')


"""
函数功能：是否构成三角形
"""
def Example12():
    a = float(input('输入三角形三条边：\n a = '))
    b = float(input(' b = '))
    c = float(input(' c = '))
    if a + b > c and a + c > b and b + c > a:
        print('能够构成三角形')
    else:
        print('不能构成三角形')


"""
函数功能：输出成绩等级
"""
def Example13():
    score = float(input('请输入成绩: '))
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print('成绩等级是:', grade)


"""
函数功能：计算提成 v1.0
利润 <= 10万，奖金可提10%
10万 < 利润 <= 20万，高出10万的部分提 7.5%
20万 < 利润 <= 40万，高出20万元的部分提5%
40万 < 利润 <= 60万，高出40万元的部分提3%
利润 > 60万，超过60万的部分提1%
"""
def Example14():
    profit = float(input('输入销售利润（元）： '))

    if profit <= 100000:
        bonus = profit * 0.1
    elif profit <= 200000:
        bonus = 100000 * 0.1 + (profit - 100000) * 0.075
    elif profit <= 400000:
        bonus = 100000 * 0.1 + 200000 * 0.075 + (profit - 200000) * 0.05
    elif profit <= 600000:
        bonus = 100000 * 0.1 + 200000 * 0.075 + 400000 * 0.05 + (profit - 400000) * 0.03
    else:
        bonus = 100000 * 0.1 + 200000 * 0.075 + 400000 * 0.05 + 600000 * 0.03 + (profit - 600000) * 0.01

    print('奖金：%.2f' % bonus)


"""
函数功能：分段函数
"""
def Example15():
    x = int(input('输入：'))
    if x > 0:
        y = 3 * x ** 2 + 4
    else:
        y = 2 * x + 2
    print('f(%d) = %d' % (x, y))


"""
函数功能：1-n求和
"""
def Example16():
    n = int(input('请输入x：'))
    s = 0
    while n > 0:
        s += n
        n -= 1
    print(s)


"""
函数功能：累加器 v2.0
"""
def Example17():
    s = 0
    while True:
        in_str = input('输入整数（输入q，则退出）：')
        if in_str == 'q':
            break
        x = int(in_str)
        s += x
        print('加和：%d' % s)


"""
函数功能：猜数游戏
"""
def Example18():
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('猜一个数字（1-100）: '))
        if number < answer:
            print('再大一点')
        elif number > answer:
            print('再小一点')
        else:
            print('猜对了')
            break

    print(f'共猜了{counter}次')


"""
函数功能：打印乘法口诀表
"""
def Example19():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{i}*{j} = {i * j}', end='\t')
            if j == i:
                print('\n')

"""
函数功能：判断是否是素数
"""
def Example20():
    num = int(input('请输入一个正整数: '))
    end = int(num // 2) + 1  # 只判断前半部分是否能整除即可，前半部分没有能整除的因此，后半部分肯定也没有

    is_prime = True
    for x in range(2, end):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('素数')
    else:
        print('不是素数')


"""
函数功能：斐波那契数列 v1.0
"""
def Example21():
    n = int(input('输入n： '))
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    print(f'第 {n} 位斐波那契数是：{a}')


"""
函数功能：水仙花数
水仙花数是一个3位数，该数字每个位上数字的立方和正好等于它本身，例如： $$ 153=1^3+5^3+3^3 $$
"""
def Example22():
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)


"""
函数功能：猴子吃桃
猴子第一天摘了 n 个桃子，当天吃了一半，还不瘾，又多吃了一个
第二天早上又将剩下的桃子吃掉一半，又多吃了一个
以后每天早上都吃了前一天剩下的一半零一个。
到第10天早上想再吃时，剩下一个桃子。求第一天共摘了多少。
"""
def Example23():
    peach = 1
    for i in range(9):
        peach = (peach + 1) * 2
    print(peach)


if __name__ == '__main__':
    Example23()
