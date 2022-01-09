#Problem 99

import math

"""

Step 1: Read the file
Step 2: Scan each line and hold line number of largest value

Use the Log change rule to adjust exponents. For instance, given 2^11 and 3^7
we know that log(2)(3) = log(3) / log(2) which is about 1.6, and 1.6*7 > 11

"""

def main():
    with open('base_exp.txt', 'r') as infile:

        top_lineNumber, lineCount, top_base, top_power = 0, 0, 2, 2
        
        for line in infile:
            lineCount += 1
            cursor = 0
            base = ''
            power = ''
            while line[cursor] != ',':
                base += str(line[cursor])
                cursor += 1
            cursor += 1    
            while cursor != len(line):
                power += str(line[cursor])
                cursor += 1

            #print(math.log(int(base)), math.log(int(top_base)))

            if math.log(int(base))/math.log(int(top_base)) * int(power) > top_power:
                top_lineNumber = lineCount
                top_base = int(base)
                top_power = int(power)


        print("The answer is ", top_lineNumber)            

if __name__ == '__main__':
    main()
