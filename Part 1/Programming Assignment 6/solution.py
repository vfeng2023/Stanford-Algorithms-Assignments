with open("algo1-programming_prob-2sum.txt", "r") as f:
    lines = f.readlines()
    nums = []
    for line in lines:
        nums.append(int(line))
    nums = list(set(nums))
print("finished reading file")
seen = set()
freqdict = {}
for n in nums:
    if n in freqdict:
        freqdict[n] += 1
    else:
        freqdict[n] = 1

count = 0
for t in range(-10000, 10000):
    print(t)
    for s in freqdict:
        x = t-s
        # if x == s:
        #     if freqdict[x] >= 2:
        #         count += 1
        #         break
        # else:
        if x !=s and x in freqdict:
            count += 1
            break
print(count)
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         total = nums[i] + nums[j]
#         if -10000 <=total <= 10000:
#             seen.add(total)

# print(len(seen))