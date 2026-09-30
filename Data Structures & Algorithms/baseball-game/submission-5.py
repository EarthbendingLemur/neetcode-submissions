class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []
        for i in range(len(operations)):
            if re.match(r"^[-+]?\d*\.?\d+$", operations[i]):
                record.append(int(operations[i]))
            elif operations[i] == '+':
                record.append(record[-2] + record[-1])
            elif operations[i] == 'C':
                print(record)
                record.pop()
            elif operations[i] == 'D':
                
                record.append(2 * record[-1])
        
        res = 0
        for r in record:
            res += r
        return res
            