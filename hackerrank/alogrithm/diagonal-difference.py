size = int(raw_input())
Number = {}
LeftDiagonal = 0
RightDiagonal = 0

for i in range(size):
    Number[i] = raw_input().split(" ")
    LeftDiagonal = LeftDiagonal + int(Number[i][i])
    RightDiagonal = RightDiagonal + int(Number[i][(size-1) -i])
print abs(LeftDiagonal - RightDiagonal)
