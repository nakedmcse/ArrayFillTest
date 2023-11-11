import random
import time

#Helper to generate random text
def generate_random_text(length):
    characters = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choice(characters) for _ in range(length))

#Function to generate options string
def generate_options_string():
    options = ["option=one"]
    for _ in range(1, 10):
        random_text = generate_random_text(5)
        options.append(f"{random_text}=100")
    random.shuffle(options)
    return '&'.join(options)

#Trivial fill of 100k options strings
def fill_inputs_trivial():
    inputs = []
    for i in range(100000):
        inputs.append(generate_options_string())
    print(f"Last Trivial Entry:{inputs[99999]}")

#Fill 100K options strings using the constructor
def fill_inputs_constructor():
    inputs = [generate_options_string()] * 100000
    print(f"Last Constructor Entry:{inputs[99999]}")

#Fill 100k options strings using for range fill
def fill_inputs_forrange():
    inputs = [generate_options_string() for _ in range(100000)]
    print(f"Last For Range Entry:{inputs[99999]}")

if __name__ == '__main__':
    print("Testing Trivial Fill method")
    start_trivial_time = time.time()
    fill_inputs_trivial()
    end_trivial_time = time.time()
    print(f"Execution time {(end_trivial_time - start_trivial_time) * 1000} ms")
    print()

    print("Testing Constructor Fill method")
    start_constructor_time = time.time()
    fill_inputs_constructor()
    end_constructor_time = time.time()
    print(f"Execution time {(end_constructor_time - start_constructor_time) * 1000} ms")
    print()

    print("Testing For Range Fill method")
    start_forrange_time = time.time()
    fill_inputs_forrange()
    end_forrange_time = time.time()
    print(f"Execution time {(end_forrange_time - start_forrange_time) * 1000} ms")
    print()