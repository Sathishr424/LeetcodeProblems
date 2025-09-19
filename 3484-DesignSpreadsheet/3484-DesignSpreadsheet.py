# Last updated: 19/9/2025, 3:24:12 pm
class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = [[0] * 26 for _ in range(rows)]
    
    def convertCell(self, cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])
        return row - 1, col

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.convertCell(cell)

        self.rows[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self.convertCell(cell)

        self.rows[row][col] = 0
        
    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        cell1, cell2 = formula.split('+')

        ans = 0
        if ord(cell1[0]) >= ord('A') and ord(cell1[0]) <= ord('Z'):
            row, col = self.convertCell(cell1)
            ans += self.rows[row][col]
        else:
            ans += int(cell1)
        
        if ord(cell2[0]) >= ord('A') and ord(cell2[0]) <= ord('Z'):
            row, col = self.convertCell(cell2)
            ans += self.rows[row][col]
        else:
            ans += int(cell2)
        
        return ans


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)