class Solution:

    def getRow(self, rowIndex):
        """
        https://www.youtube.com/watch?v=PKiV5HhnfDw&t=387s
        :param rowIndex:  int
        :return:  List[int]
        """
        result = [1] + [0] * rowIndex

        for i in range(rowIndex):
            # result[0] = 1
            for j in range(i + 1, 0, -1):
                    result[j] = result[j] + result[j-1]
        return result


