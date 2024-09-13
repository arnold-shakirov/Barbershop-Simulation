import threading
import time
import random


class Barbershop:
    def __init__(self, n_chairs):
        self.chairs = threading.Semaphore(n_chairs)  # Controls available chairs
        self.customer_queue = threading.Semaphore(0)  # Manages customer readiness to get haircuts
        self.barber_ready = threading.Lock()  # Ensures barber serves one customer at a time
        self.barber_awake = threading.Event()  # Indicates if the barber is awake
        self.barber_awake.set()  # Initially, the barber is awake
        self.print_lock = threading.Lock()  # Mutex for printing

    def barber(self):
        while True:
            self.customer_queue.acquire()  # Wait for a customer to be ready
            with self.barber_ready:  # Lock the barber service
                # The barber waits here for the customer to signal they are ready inside their locked section
                pass

    def customer(self, customer_id):
        with self.print_lock:
            print(f"Customer {customer_id} entering the shop.")

        if self.chairs.acquire(blocking=False):
            with self.print_lock:
                print(f"Customer {customer_id} is waiting in a chair.")

            time.sleep(random.uniform(0.1, 0.2))  # Simulate delay before getting ready
            self.customer_queue.release()  # Signal that the customer is ready
            # Check if the barber is asleep and wake him up if necessary
            if not self.barber_awake.is_set():
                with self.print_lock:
                    print(f"Customer {customer_id} is waking up the barber.")
                self.barber_awake.set()

            with self.barber_ready:  # Wait for exclusive barber access
                with self.print_lock:
                    print(f"Customer {customer_id} getting a haircut.")
                    print(f"Barber is cutting hair for customer {customer_id}.")
                time.sleep(random.uniform(0.5, 1.5))  # Simulate haircut duration
                with self.print_lock:
                    print("Barber has finished the haircut.")
                    print(f"Customer {customer_id} leaving with a fresh haircut.")
            self.chairs.release()  # Release the chair
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
