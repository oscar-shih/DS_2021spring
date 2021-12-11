import json
import time
import argparse
import heapq
# --- TODO START --- #
# You can define any class or function
# You can import any python standard library : https://docs.python.org/3/library/
# However, you are not allowed to import any libraries other than python standard library, (such as numpy)
# --- TODO END --- #

def solution(json_input):
    # --- TODO START --- #
    json_sum = [0]
    arr = json_input['array']
    k = json_input['topk']
    json_sum.append(arr[0])
    for i in range(2,len(arr) + 1):
        json_sum.append(json_sum[i - 1] + arr[i - 1])
    H = []
    heapq.heapify(H)
    for i in range(1, len(arr) + 1):
        for j in range(i , len(arr) + 1):
            x = json_sum[j] - json_sum[i - 1]
            if len(H) < k:
                heapq.heappush(H, x)
            else:
                if H[0] < x:
                    heapq.heappop(H)
                    heapq.heappush(H, x)
    # --- TODO END --- #
    H.sort(reverse=True)
    # print(H)
    return H

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='input_1.json')
    parser.add_argument('--output', default='output_1.json')
    args = parser.parse_args()
    json_input = json.load(open(args.input, "r"))
    t1 = time.time()
    json_output = solution(json_input)
    t2 = time.time()
    json.dump(json_output, open(args.output, "w"))
    print("runtime of %s : %s" % (args.input, t2 - t1))

