class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, col = len(matrix), len(matrix[0])

        t_r, b_r = 0, rows - 1

        while t_r <= b_r:
            m_r = (t_r + b_r) // 2
            if target > matrix[m_r][-1]:
                t_r = m_r + 1
            elif target < matrix[m_r][0]:
                b_r = m_r - 1
            else:
                print('found')
                break
        
        # if m_r_f < 0
    
        m_r = (t_r + b_r) // 2

        l,r = 0, col - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[m_r][m]:
                r = m - 1
            elif target > matrix[m_r][m]:
                l = m + 1
            else:
                return True
        
        return False



        return False