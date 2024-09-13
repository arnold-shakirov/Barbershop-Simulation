import threading
import time
import random
# 3 chairs, 10 customers
class Barbershop:
    def __init__(self, n_chairs):
        self.chairs = threading.Semaphore(n_chairs)  # available chairs
        self.customer_queue = threading.Semaphore(0)  # customer readiness to get haircuts
        self.barber_ready = threading.Lock()  # Ensures barber serves one customer at a time, using lock
        self.barber_awake = threading.Event()  # Indicates if the barber is awake, initially asleep
        self.barber_awake.clear()  # Initially, the barber is ASLEEP
        self.print_lock = threading.Lock()  # Mutex


    def customer(self, customer_id):
        retrying = False
        while True:
            with self.print_lock:
                if retrying:
                    print(f"Customer {customer_id} coming back to the shop.")
                else:
                    print(f"Customer {customer_id} entering the shop.")

            if self.chairs.acquire(blocking=False):

                if not self.barber_awake.is_set():
                    with self.print_lock:
                        print(f"Customer {customer_id} wakes up the barber.")
                    self.barber_awake.set()

                with self.print_lock:
                    print(f"Customer {customer_id} is waiting in a chair.")

                self.customer_queue.release()  #customer is ready



                with self.barber_ready:  # exclusive barber access
                    with self.print_lock:
                        print(f"Customer {customer_id} getting a haircut.")
                    time.sleep(random.uniform(0.5, 1.0))  # getting a haircut
                    with self.print_lock:
                        print(f"Barber has finished the haircut for customer {customer_id}.")
                        print(f"Customer {customer_id} leaving, got a haircut.")
                self.chairs.release()
                break  # Leave the loop once served
            else:
                with self.print_lock:
                    print(f"Customer {customer_id} found no free chairs and is leaving.")
                time.sleep(random.uniform(1, 3))  # wait outside for some time
                retrying = True  # try to come back later

    def barber(self):
        while True:
            if not self.customer_queue.acquire(timeout=5):  # waiting for customers for some time otherwise going to sleep
                with self.print_lock:
                    print("Barber goes to sleep.")
                self.barber_awake.clear()  # goes to sleep, no customers
                self.barber_awake.wait()  # asleep while no customers waiting
            with self.barber_ready:  # Lock the barber
                time.sleep(random.uniform(0.5, 1.5))  # haircut

def main():
    n_customers = 10
    n_chairs = 3

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