# Barbershop Problem Simulation

## Overview
This project implements various solutions to the classic **Barbershop Problem** using Python. The Barbershop Problem is a synchronization problem in computer science where a barber sleeps until a customer arrives, and customers must wait if all chairs are occupied. The project simulates these scenarios, handling different variations of the problem in multiple Python files.

## Files
- **`barbershop.py`**: The main implementation of the Barbershop Problem simulation.
- **`barbershop1.py`**: A variation of the barbershop simulation with different concurrency handling.
- **`barbershop2.py`**: Another variation of the problem with different synchronization mechanisms.
- **`barbershop3.py`**: A more complex version of the simulation, possibly involving multiple barbers or advanced waiting logic.
- **`barbershoppresudo.py`**: A pseudocode-style implementation or high-level description of the Barbershop Problem solution.

## Problem Description
In the classic Barbershop Problem:
1. The barber sleeps if no customers are present.
2. A customer must wait if the barber is cutting hair, but only if there are available chairs in the waiting room.
3. If no chairs are available, the customer leaves.

The goal is to use synchronization (typically with semaphores or other concurrency primitives) to ensure that the barber and customers interact correctly without deadlocks or race conditions.

## How to Run the Simulation

### Prerequisites
- **Python 3.x** or higher is required to run the scripts.

### Running the Simulation

1. Clone the repository:
    ```bash
    git clone https://github.com/arnold-shakirov/Barbershop-Simulation.git
    ```

2. Navigate to the project directory:

3. Run any of the Python files to execute the simulation:

    Alternatively, you can run the variations of the simulation:
    ```bash
    python barbershop1.py
    python barbershop2.py
    python barbershop3.py
    ```

### Output
The simulation outputs the interactions between customers and the barber. Depending on the version, you will see messages indicating:
- When a customer arrives.
- When the barber is cutting hair.
- When customers are waiting or leaving due to full chairs.

## Requirements
- **Python 3.x** or higher.

## Contact
For any questions or suggestions, feel free to reach out to me at [ashakirov@stetson.edu].
