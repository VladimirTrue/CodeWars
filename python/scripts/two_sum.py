# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

def two_sum(numbers, target):
        nums = list(numbers)
        for num in numbers:

            find = target - num
            try:
                x = list(nums).index(num)
                y = list(nums).index(find)
                if x == y:
                    nums[y] = None
                    y = list(nums).index(find)
                    return [x, y]
                else:
                    return [x, y]
            except ValueError:
                continue
