import random

# Parameters
cost_per_try = 10
refund_percentage = 0.30
runs = 100000
max_rolls = 5

def simulate_until_success():
    total_tries = 0
    total_tickets_spent = 0
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
                tickets_spent += cost_per_try

                # Calculate dynamic probability of success
                remaining_needed_successes = 2 - successes
                probability_of_success = remaining_needed_successes / (13 - tries_in_batch)

                if random.random() < probability_of_success:
                    successes += 1

                if successes == 2:
                    total_tickets_spent += tickets_spent
                    break

                # Calculate remaining tries needed and check for failure state
                remaining_tries = max_rolls - tries_in_batch
                if remaining_tries < remaining_needed_successes:
                    tickets_spent -= tries_in_batch * cost_per_try * refund_percentage
                    total_tickets_spent += tickets_spent
                    break

            if successes == 2:
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
