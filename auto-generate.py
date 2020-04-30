from anti import Anti
from cor import Cor
from indep import Indep
def main():
    number = int(input("number of points:"))
    dimension_from = int(input("dimension start:"))
    dimension_end = int(input("dimension end:"))
    for dimension in range(dimension_from, dimension_end + 1):
        cor = Cor(number, dimension)
        cor.generate()
        indep = Indep(number, dimension)
        indep.generate()
        anti = Anti(number, dimension)
        anti.generate()
if __name__ == "__main__":
    main()
