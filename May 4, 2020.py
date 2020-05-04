#Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
#Input: 5
#Output: 2
#Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

class Solution:
    def findComplement(self, num: int) -> int:
        num_array = bin(num)[2:]
        output=''
        for i in range(len(num_array)):
            if num_array[i]=='0': output+='1'
            else: output+='0'
        return(int(output,2))