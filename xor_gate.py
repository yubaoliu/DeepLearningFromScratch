from and_gate import AND
from or_gate import OR
from nand_gate import NAND

def XOR(x1, x2):
	s1 = OR(x1, x2)
	s2 = NAND(x1, x2)
	y = AND(s1, s2)
	return y

if __name__ == "__main__":
	print(XOR(0, 0))
	print(XOR(0, 1))
	print(XOR(1, 0))
	print(XOR(1, 1))
