import math
import multiprocessing
import numpy as np
from math import log
def calc_mean_std(mant, exp, return_dict):
    # m = 4
    # exp = 2
    num1 = 1
    RE_sum = 2-2*math.log(2)
    mantissas = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
    for e in range(0, 2**exp):
        for m in mantissas:
            try:
                if(np.longdouble(m*2**e) > np.longdouble(num1)):
                    num2 = np.longdouble(m*2**e)
                    half_point = np.longdouble(num1/2+num2/2)
                    temp1 = (np.longdouble(num1))*log(np.longdouble(num1)/np.longdouble(half_point))
                    temp2 = (np.longdouble(num2))*log(np.longdouble(num2)/(np.longdouble(half_point)))
                    RE_sum += temp1+temp2
                    num1 = num2
            except:
                print("Error in m="+str(m)+" and e="+str(e))
            else:
                continue
    mean_RE = np.longdouble(RE_sum/num1)
    return_dict.append([m, exp, mean_RE, num1])

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
    # np.savetxt("C:\\Users\\asus\\Desktop\\ISLS_Presentation_Stuff\\"+str(total_bits)+"bit_mre.csv", return_array, delimiter=",")
    # start_time = time.time()
    return_dict = []
    calc_mean_std(12,4,return_dict)
    print(return_dict)
