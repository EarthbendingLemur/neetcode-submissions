class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        it = 1
        for i in range(2, numRows + 1):
            prev_row = res[it - 1]
            new_row = [1] * (len(prev_row) + 1)
            for j in range(1, len(new_row) - 1):
                new_row[j] = prev_row[j] + prev_row[j - 1]

            it += 1
            res.append(new_row)

        return res