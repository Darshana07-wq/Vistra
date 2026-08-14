import multiprocessing

def worker():
    print("Hello from a new process!")

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn", force=True)
    
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()

    print("Process finished.")
