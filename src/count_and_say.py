class Solution:
    def count_and_say(self, n: int) -> str:
        result = ''
        t_count = 0
        tmp = ''

        for i in range(1, n+1):
            t_result = ''
            if i == 1:
                result = '1'
            else:
                for s in result:
                    if tmp == s or tmp == '':
                        t_count += 1
                        tmp = s
                    else:
                        t_result += str(t_count) + tmp
                        tmp = ''
                        t_count = 0
                result = t_result
        return result