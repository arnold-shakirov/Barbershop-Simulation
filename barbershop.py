import threading
import time
import random

class Barbershop:
    def __init__(self, n_chairs):
        self.chairs = threading.Semaphore(n_chairs)
        self.customer_queue = threading.Semaphore(0)
        self.barber_ready = threading.Lock()
        self.barber_awake = threading.Event()  # Indicates if the barber is awake
        self.print_lock = threading.Lock()

    def barber(self):
        while True:
            # Barber waits for a customer or goes to sleep if no customer is ready
            if not self.customer_queue.acquire(timeout=5):  # Timeout to simulate waiting for customer
                with self.print_lock:
                    print("No customers. Barber is going to sleep.")
                self.barber_awake.clear()
                self.barber_awake.wait()  # Barber sleeps here waiting to be awakened
                with self.print_lock:
                    print("Barber wakes up.")

            with self.barber_ready:
                self.cut_hair()

    def cut_hair(self):
        with self.print_lock:
            print("Barber is cutting hair.")
        time.sleep(random.uniform(0.5, 1.5))

    def customer(self, customer_id):
        with self.print_lock:
            print(f"Customer {customer_id} entering the shop.")

        if self.chairs.acquire(blocking=False):
            with self.print_lock:
                print(f"Customer {customer_id} is waiting in a chair.")

            self.customer_queue.release()  # Customer signals they are ready
            if not self.barber_awake.is_set():
                with self.print_lock:
                    print(f"Customer {customer_id} is waking up the barber.")
                self.barber_awake.set()

            with self.barber_ready:
                self.customer_queue.acquire()
                with self.print_lock:
                    print(f"Customer {customer_id} getting a haircut.")
                time.sleep(random.uniform(0.1, 0.3))

            with self.print_lock:
                print(f"Customer {customer_id} leaving with a fresh haircut.")
            self.chairs.release()
        else:
            with self.print_lock:
                print(f"Customer {customer_id} found no free chairs and is leaving.")

def main():
    n_chairs = 3
    n_customers = 10
    shop = Barbershop(n_chairs)

    barber_thread = threading.Thread(target=shop.barber)
    barber_thread.start()

    customer_threads = [threading.Thread(target=shop.customer, args=(i,)) for i in range(n_customers)]
    for thread in customer_threads:
        thread.start()
        time.sleep(0.1)

    for thread in customer_threads:
        thread.join()

    barber_thread.join()

if __name__ == "__main__":
    main()
