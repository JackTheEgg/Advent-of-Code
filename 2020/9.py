import math

def sumRange(nums, num):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if math.fsum(nums[i:j]) == num:
                return nums[i:j]
            elif math.fsum(nums[i:j]) > num:
                break

def checkSum(nums, num):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == num:
                return True
    return False

preamble = 25
numbers = []
checkedNums = []
lineCount = 0
faultNum = 0
with open("9.txt") as file:
    for line in file:
        lineCount += 1
        if lineCount <= preamble:
            checkedNums.append(int(line.strip()))
            numbers.append(int(line.strip()))
        else:
            if checkSum(numbers, int(line.strip())):
                del numbers[0]
                numbers.append(int(line.strip()))
                checkedNums.append(int(line.strip()))
            else:
                print("The first faulty number is", line.strip())
                faultNum = int(line.strip())
                break
faultSum = sumRange(checkedNums, faultNum)
faultSum.sort()
print(faultSum[0] + faultSum[-1])