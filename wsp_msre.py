import math
import multiprocessing
import numpy as np
from math import log
def calc_mean_std(mant, exp, return_dict):
    # m = 4
    # exp = 2
    num1 = 1
    square_RE_sum = 2-2*math.log(2)
    for e in range(0, 2**exp):
        for m in range(0, mant+1):
            try:
                if(np.longdouble(m*2**e) > np.longdouble(num1)):
                    num2 = np.longdouble(m*2**e)
                    half_point = np.longdouble(num1/2+num2/2)
                    square_RE_sum += (num2-num1) + (num1**2)*(1/num1-1/half_point) - 2*num1*math.log(half_point/num1)
                    square_RE_sum += (num2**2)*(1/half_point - 1/num2) - 2*num2*math.log(num2/half_point)
                    num1 = num2
            except:
                print("Error in m="+str(m)+" and e="+str(e))
            else:
                continue
    mean_square_RE = np.longdouble(square_RE_sum/num1)
    return_dict.append([m, exp, mean_square_RE])

import time
if __name__ == "__main__":
    # manager = multiprocessing.Manager()
    # return_dict = manager.list()
    # jobs = []
    # total_bits = 16
    # for i in range(8,total_bits):
    #     p = multiprocessing.Process(target=calc_mean_std, args=(i, total_bits-i, return_dict))
    #     jobs.append(p)
    #     p.start()

    # for proc in jobs:
    #     proc.join()
    # import numpy as np
    # return_array = np.asarray(return_dict)
    # print(return_array)
    # np.savetxt("C:\\Users\\asus\\Desktop\\ISLS_Presentation_Stuff\\"+str(total_bits)+"bit_msre.csv", return_array, delimiter=",")
    # start_time = time.time()
    return_dict = []
    calc_mean_std(7,3,return_dict)
    print(return_dict)
