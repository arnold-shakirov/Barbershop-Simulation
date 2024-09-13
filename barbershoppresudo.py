class Barbershop:
    Initialize(n_chairs):
    chairs = Semaphore(n_chairs)
    customer_queue = Semaphore(0)
    barber_ready = Lock()
    barber_awake = Event()
    barber_awake.clear()


Customer(customer_id): #code for customers
retrying = False
loop:
if not retrying:
    print
    "Customer customer_id entering the shop."
else:
    print
    "Customer customer_id coming back to the shop."

if chairs can be acquired (non-blocking):
    if barber is not awake:
        print
        "Customer customer_id wakes up the barber."
        Set barber_awake
        event(wake
        up
        the
        barber)

        print
        "Customer customer_id is waiting in a chair."
        Signal
        customer_queue(customer is ready)

        Lock
        barber_ready(wait for exclusive access
        to
        barber):
        print
        "Customer customer_id getting a haircut."
        Sleep
        for haircut duration
            print
            "Barber has finished the haircut for customer customer_id."
        print
        "Customer customer_id leaving, got a haircut."
    Release
    chair
    exit
    loop
else:
    print
    "Customer customer_id found no free chairs and is leaving."
    Sleep
    for a random time before retrying
    retrying = True

Barber():
loop:
if no customer arrives within timeout:
    print
    "Barber goes to sleep."
    Clear
    barber_awake(barber
    sleeps)
    Wait
    for barber_awake event(remain asleep until a customer arrives)

Lock
barber_ready:
Sleep
for haircut duration(simulate haircutting)

Main:
n_chairs = 3
n_customers = 10
shop = new
Barbershop(n_chairs)

Start
barber
thread(shop.barber)

Start
customer
threads
for each customer(shop.customer) with slight delay
Wait
for all threads to complete
