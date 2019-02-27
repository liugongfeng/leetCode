class Solution:

    def countAndSay(self, n):
        """
        :param n: int
        :return: str
        """
        seq = '1'
        for i in range(n - 1):
            seq = self.getNext(seq)

        return seq

    def getNext(self, seq):
        i, next_seq = 0, ""
        while i < len(seq):
            count = 1
            while i < len(seq) - 1 and seq[i] == seq[i + 1]:
                count += 1
                i += 1
            next_seq += str(count) + seq[i]
            i += 1

        return next_seq

    # def countAndSay(self, n: 'int') -> 'str':
    #
    #     sequence = [1]
    #     for _ in range(n - 1):
    #         next = []
    #         for num in sequence:
    #             if not next or next[-1] != num:
    #                 next += [1, num]
    #             else:
    #                 next[-2] += 1
    #         sequence = next
    #
    #     return ''.join(map(str, sequence))

if __name__ == "__main__":
    s = Solution()
    result = s.countAndSay(4)
    print(result)

