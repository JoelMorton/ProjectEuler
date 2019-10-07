
count = 0
for L2 in range(2):
    for L1 in range(3):
        for p50 in range(5):
            # if L1*100 + p50*50 > 200:
            #     continue
            for p20 in range(11):
                # if L1*100 + p50*50 + p20*20 > 200:
                #     continue
                for p10 in range(21):
                    # if L1 * 100 + p50 * 50 + p20 * 20 + p10 * 10 > 200:
                    #     continue
                    for p5 in range(41):
                        # if L1 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 > 200 :
                        #     continue
                        for p2 in range(101):
                            if L1 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 + p2 * 2 > 200:
                                break
                            for p1 in range(201):
                                sum = L2 * 200 + L1 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 + p2 * 2 + p1
                                if sum > 200:
                                    break
                                if sum == 200:
                                    count = count + 1
print(count)
# #358584
#
# for x in range(3):
#     for y in range(3):
#         if y == 2:
#             print('y==2')
#             break
#         print(x, y)

# count = 0
# for L2 in range(2):
#     for L1 in range(3):
#         for p50 in range(5):
#             # if L1*100 + p50*50 > 200:
#             #     continue
#             for p20 in range(11):
#                 # if L1*100 + p50*50 + p20*20 > 200:
#                 #     continue
#                 sum = L2 * 200 + L1 * 100 + p50 * 50 + p20 * 20
#                 if sum > 200:
#                     break
#                 if sum == 200:
#                     count = count + 1
# print(count)