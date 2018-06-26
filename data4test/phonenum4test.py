import string
import random


def phone_num(num):
    all_phone_nums = set()
    num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
           '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
    for i in range(num):
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 8))
        res = start+end+'\n'
        all_phone_nums.add(res)
    with open('phone_num.txt', 'w', encoding='utf-8') as fw:
        fw.writelines(all_phone_nums)


def get_random_chinese_phone_num():
    num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
           '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
    start = random.choice(num_start)
    end = ''.join(random.sample(string.digits, 8))
    phone_num = start+end
    return phone_num


if __name__ == '__main__':
    print(get_random_chinese_phone_num())
