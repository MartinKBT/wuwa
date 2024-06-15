import random

# Parameters
costs = [28425, 58725, 94575, 175900]
refund_percentage = 0.80
runs = 100000
successes_needed = 3
probability_of_success = 1/2
max_rolls = 4


def simulate_until_success():
    total_tries = 0
    total_tickets_spent = 16300
    pieces_rolled = 0

    for _ in range(runs):
        while True:
            pieces_rolled += 1
            tries_in_batch = 0
            tickets_spent = 0
            successes = 0

            while tries_in_batch < max_rolls:
                tries_in_batch += 1
                total_tries += 1
                tickets_spent += costs[tries_in_batch-1]
                remaining_needed_successes = successes_needed - successes


                if random.random() < probability_of_success:
                    successes += 1

                if successes == successes_needed:
                    total_tickets_spent += tickets_spent
                    break
            if successes == successes_needed:
                break

                # Calculate remaining tries needed and check for failure state
                remaining_tries = max_rolls - tries_in_batch
                if remaining_tries < remaining_needed_successes:
                    tickets_spent -= sum(costs[:tries_in_batch]) * refund_percentage
                    total_tickets_spent += tickets_spent
                    break


    average_pieces_rolled = pieces_rolled / runs
    average_total_tries = total_tries / runs
    average_total_tickets_spent = total_tickets_spent / runs

    return average_pieces_rolled, average_total_tries, average_total_tickets_spent


# Perform Monte Carlo simulation
average_pieces, average_tries, average_tickets = simulate_until_success()

# Print results
print(f"Average Pieces Rolled: {average_pieces}")
print(f"Average Total Tries: {average_tries}")
print(f"Average Total Tickets Spent: {average_tickets}")
