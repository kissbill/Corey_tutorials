# szinkron lefutas, egymas utan lefut 2 sec
# import time

# start = time.perf_counter()


# def do_something():
#     print('Sleeping 1 second...')
#     time.sleep(1)
#     print('Done sleeping...')


# do_something()
# do_something()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} second(s)')


# process, join ###################################################
# import multiprocessing
# import time

# start = time.perf_counter()


# def do_something():
#     print('Sleeping 1 second...')
#     time.sleep(1)
#     print('Done sleeping...')


# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=do_something)
#     p2 = multiprocessing.Process(target=do_something)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} second(s)')


# # 10 thread with 2x for loop #####################################
# import multiprocessing
# import time

# start = time.perf_counter()


# def do_something():
#     print('Sleeping 1 second...')
#     time.sleep(1)
#     print('Done sleeping...')


# processes = []

# if __name__ == "__main__":
#     for n in range(10):
#         p = multiprocessing.Process(target=do_something)
#         p.start()
#         processes.append(p)

#     for process in processes:
#         process.join()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} second(s)')

# --> concurrent.futures 	#####################################
# import concurrent.futures
# import time

# start = time.perf_counter()


# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     return 'Done Sleeping...'


# if __name__ == "__main__":
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         f1 = executor.submit(do_something, 1)
#         f2 = executor.submit(do_something, 1)
#         print(f1.result())
#         print(f2.result())

#         finish = time.perf_counter()
#         print(f'Finished in {round(finish-start, 2)} second(s)')

# addig fut amig a fgv vissza nem jon result-tal

# processes = []

# if __name__ == "__main__":
# for n in range(10):
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()


# 10 thread with 2x for loop --> concurrent.futures 	#####################################
# import concurrent.futures
# import time

# start = time.perf_counter()


# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     return 'Done Sleeping...'


# if __name__ == "__main__":
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         results = [executor.submit(do_something, 1) for _ in range(10)]

#         for f in concurrent.futures.as_completed(results):
#             print(f.result())

# finish = time.perf_counter()
# print(f'Finished in {round(finish-start, 2)} second(s)')


# # 10 thread with 2x for loop with parameter --> concurrent.futures 	#####################################
# import concurrent.futures
# import time

# start = time.perf_counter()


# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     return 'Done Sleeping...'


# if __name__ == "__main__":
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         secs = [5, 4, 3, 2, 1]
#         results = [executor.submit(do_something, sec) for sec in secs]

#         for f in concurrent.futures.as_completed(results):
#             print(f.result())

# finish = time.perf_counter()
# print(f'Finished in {round(finish-start, 2)} second(s)')

# 10 thread with 2x for loop with parameter /mapping --> concurrent.futures 	#####################################
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)
        # map-> ossze mappali az ossze bemeneti ertekkel a fgv-t 5 4 3 2 1

        for result in results:
            print(result)

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
