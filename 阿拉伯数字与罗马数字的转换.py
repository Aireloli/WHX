#coding utf-8
'''
阿拉伯数字转罗马数字
'''
class Number():
    def __init__(self, num):
        self.num = num

    def transform(self):
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        str_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_list = []
        for i in range(len(num_list)):
            while self.num >= num_list[i]:
                roman_list.append(str_list[i])
                self.num -= num_list[i]
        print(''.join(roman_list))

def judge_num(n):
    while 1:
        if not n.isdigit():
            n = input("请输入一个正整数:")
            return judge_num(n)
        else:
            n = int(n)
            if n > 3999:
                n = input("你输入的数太大了,请输入一个1到3999的整数:")
            else:
                return n

if __name__ == '__main__':
    n = input('请输入你想要转换的数字：')
    num = Number(judge_num(n))
    num.transform()
