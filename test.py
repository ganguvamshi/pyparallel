from time import sleep
import time
from concurrent.futures import ProcessPoolExecutor


def slow_function(x):
    #print('start :{}'.format(x))
    sleep(3)
    #print('done: {}'.format(x))
    return x**2


numbers = range(4)

stime = time.time()

res = []
for n in numbers:
    res.append(slow_function(n))

print('Sequential : {} {}'.format((time.time() - stime), 'seconds'))
print('Seq result:{}'.format(res))

stime = time.time()

with ProcessPoolExecutor(max_workers=2) as ex:
    for n, pres in zip(numbers, ex.map(slow_function, numbers)):
        print("{}: res:{}".format(n, pres))
#     flist = [ex.submit(slow_function, n) for n in numbers]
#     res = []
#     for f in as_completed(flist):
#         res.update(f.result())
print('Processes : {}'.format((time.time() - stime, 'seconds')))
