# Last updated: 21/6/2025, 2:57:39 pm
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        x = [2]
        y = [3]
        z = [5]
        
        x_index = 0
        y_index = 0
        z_index = 0
        num = 1
        n -= 1
        while n:
            if x[x_index] == y[y_index]:
                x_index += 1
            if x[x_index] == z[z_index]:
                x_index += 1
            if y[y_index] == z[z_index]:
                y_index += 1
            
            if x[x_index] < y[y_index] and x[x_index] < z[z_index]:
                num = x[x_index]
                x_index += 1
            elif y[y_index] < z[z_index]:
                num = y[y_index]
                y_index += 1
            else:
                num = z[z_index]
                z_index += 1

            x.append(num * 2)
            y.append(num * 3)
            z.append(num * 5)
            n -= 1

        return num