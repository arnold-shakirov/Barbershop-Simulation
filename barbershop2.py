import threading
import time
import random

class Barbershop:
    def __init__(self, n_chairs):
        self.chairs = threading.Semaphore(n_chairs)  # Controls available chairs
        self.customer_queue = threading.Semaphore(0)  # Manages customer readiness to get haircuts
        self.barber_ready = threading.Lock()  # Ensures barber serves one customer at a time
        self.barber_awake = threading.Event()  # Indicates if the barber is awake
        self.barber_awake.clear()  # Initially, the barber is ASLEEP
        self.print_lock = threading.Lock()  # Mutex for printing

    def barber(self):
        while True:
            # Check if there are any customers before proceeding to wait to be more efficient
            if not self.customer_queue.acquire(timeout=5):  # Wait for a customer to be ready, with timeout
                self.barber_awake.clear()  # No customers, so the barber goes to sleep
                print(f"Barber goes to sleep.")
                self.barber_awake.wait()  # Wait to be woken up by a customer
            with self.barber_ready:  # Lock the barber service
                time.sleep(random.uniform(0.5, 1.5))  # Simulate haircut duration

    def customer(self, customer_id):
        with self.print_lock:
            print(f"Customer {customer_id} entering the shop.")

        if self.chairs.acquire(blocking=False):
            with self.print_lock:
                print(f"Customer {customer_id} is waiting in a chair.")

            self.customer_queue.release()  # Signal that the customer is ready

            if not self.barber_awake.is_set():
                with self.print_lock:
                    print(f"Customer {customer_id} wakes up the barber.")
                self.barber_awake.set()  # Wake up the barber if he is asleep



            with self.barber_ready:  # Wait for exclusive barber access
                with self.print_lock:
                    print(f"Customer {customer_id} getting a haircut.")
                time.sleep(random.uniform(0.5, 1.0))  # Simulate haircut duration
                with self.print_lock:
                    print(f"Barber has finished the haircut for customer {customer_id}.")
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
