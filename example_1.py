from queue import Queue


def task(name, work_queue: Queue):
    if work_queue.empty():
        print(f'Task {name} nothing to do')
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0
            print(f'Task {name} running')
            for x in range(count):
                total += 1
            print(f'Task {name} total: {total}')


def main():
    work_queue = Queue()

    for work in [8, 5, 3, 1]:
        work_queue.put(work)

    tasks = [(task, 'One', work_queue), (task, 'Two', work_queue)]

    for t, n, q in tasks:
        t(n, q)


if __name__ == '__main__':
    main()
