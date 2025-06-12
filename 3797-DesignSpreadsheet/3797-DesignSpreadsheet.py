# Last updated: 12/6/2025, 5:34:07 am
class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0].lower()) - 97
        row = int(cell[1:]) - 1

        self.rows[row][col] = value

    def getCellValue(self, cell):
        col = ord(cell[0].lower()) - 97
        row = int(cell[1:]) - 1

        return self.rows[row][col]
    
    def resetCell(self, cell: str) -> None:
        col = ord(cell[0].lower()) - 97
        row = int(cell[1:]) - 1

        self.rows[row][col] = 0

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split('+')

        if not x[0].isdigit():
            x = self.getCellValue(x)
        if not y[0].isdigit():
            y = self.getCellValue(y)

        return int(x) + int(y)
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)