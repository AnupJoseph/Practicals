from typing import List,Type

def build_bipolar_walsh_matrix(size: int) -> List[List[int]]:
    counting_range: Type = range(size)
    bipolar_walsh_matrix: [List[List[int]]] = [[-1 for i in counting_range] for j in counting_range]
    for x in counting_range:
        for y in counting_range:
            number_of_flips: int = x&y

            # 13 here is just a trick to strip of the 0b at the start of the code
            # An alternative would be to actually strip off the characters till b and convert the rest to int 
            value_at_position: int = int(bin(number_of_flips),13)  
            bipolar_of_value: int = (value_at_position%2) or -1
            bipolar_walsh_matrix[x][y] = bipolar_of_value
    return bipolar_walsh_matrix


def display_basic(array: List[int]):
    print(f"{array}",sep="\t")
    print(f"\n")

def display_bipolar(matrix: List[List[int]]):
    print('\n')
    for row in matrix:
        display_basic(row)
        

def spread_data(data: int,code: List[int]) -> List[int]:
    return [ i*data for i in code]

def recover_data(data: List[int], code: List[int]) -> int:
    result: int = list(map(sum, zip(data, code)))[0]
    return 1 if result>0 else 0

if __name__ == "__main__":
    num_station: int = int(input(f"Enter the number of stations between which the data is to be transmitted\n"))
    bipolar_matrix = build_bipolar_walsh_matrix(num_station)

    data_a: int = int(input("Enter data of the sender A\n"))
    row_a: int = int(input("Enter row for code of A\n"))
    code_a: List[int] = bipolar_matrix[row_a-1]
    print(f"\nCode of sender A:",sep="")
    display_basic(code_a)

    data_b: int = int(input("Enter data of receiver B\n"))
    row_b: int = int(input("Enter row for code of B\n"))
    code_b: List[int] = bipolar_matrix[row_b-1]
    print(f"\nCode of sender B:",sep="")
    display_basic(code_b)

    spread_a: List[int] = spread_data(data_a,code_a)
    print(f"\nAs:",sep="")
    display_basic(spread_a)

    spread_b: List[int] = spread_data(data_b,code_b)
    print(f"\nBs:",sep="")
    display_basic(spread_b)

    spreads_sum: List[int] = list(map(sum, zip(spread_a,spread_b)))
    print(f"\nCs:",sep="")
    display_basic(spreads_sum)
    
    recovered_a: int = recover_data(spreads_sum,code_a)
    recovered_b: int = recover_data(spreads_sum,code_b)

    print(f"A data: {recovered_a}")
    print(f"B data: {recovered_b}")
