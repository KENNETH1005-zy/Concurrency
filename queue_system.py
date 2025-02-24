import numpy as np
import queue
import threading
import multiprocessing
import time

# Configurable Queue Size
QUEUE_SIZE = 10
MATRIX_SIZE = 500
CALL_RATE = 0.1
TOTAL_CALLS = 50


def generate_large_matrix(size):
    return np.random.rand(size, size)


def matrix_multiplication_task(q, result_list):
    while True:
        try:
            A, B = q.get(timeout=5)  # Get matrices from the queue
            result = np.matmul(A, B)  # Perform multiplication
            result_list.append(result)  # Store result
            if isinstance(q, queue.Queue):  # Only call task_done for threading.Queue
                q.task_done()
        except queue.Empty:
            break


def run_multithreading():
    print("Running Multi-threading Test")
    q = queue.Queue(QUEUE_SIZE)
    results = []
    threads = []

    for _ in range(5):  # 5 worker threads
        t = threading.Thread(target=matrix_multiplication_task, args=(q, results))
        t.start()
        threads.append(t)

    for _ in range(TOTAL_CALLS):
        A, B = generate_large_matrix(MATRIX_SIZE), generate_large_matrix(MATRIX_SIZE)
        q.put((A, B))
        time.sleep(CALL_RATE)

    q.join()
    for t in threads:
        t.join()
    print("Multi-threading Test Completed")


def run_multiprocessing():
    print("Running Multi-processing Test")
    q = multiprocessing.Queue(QUEUE_SIZE)
    manager = multiprocessing.Manager()
    results = manager.list()
    processes = []

    for _ in range(5):  # 5 worker processes
        p = multiprocessing.Process(target=matrix_multiplication_task, args=(q, results))
        p.start()
        processes.append(p)

    for _ in range(TOTAL_CALLS):
        A, B = generate_large_matrix(MATRIX_SIZE), generate_large_matrix(MATRIX_SIZE)
        q.put((A, B))
        time.sleep(CALL_RATE)

    q.close()
    q.join_thread()
    for p in processes:
        p.join()
    print("Multi-processing Test Completed")


if __name__ == "__main__":
    start_time = time.time()
    run_multithreading()
    print(f"Multi-threading Execution Time: {time.time() - start_time} seconds\n")

    start_time = time.time()
    run_multiprocessing()
    print(f"Multi-processing Execution Time: {time.time() - start_time} seconds\n")
