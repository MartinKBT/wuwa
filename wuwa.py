import random

# Parameters

costs = [4400, 12100, 23100, 39500, 63500]
cost_per_try = 10
refund_cubes = 0.30
refund_xp = 0.75
runs = 100000
successes_needed = 1
max_rolls = 5


def simulate_until_success():
    global remaining_needed_successes, money, money_spent, xp_spent
    total_tries = 0
    total_tickets_spent = 0
    total_xp_spent = 0
    total_money_spent = 0
    pieces_rolled = 0

    for _ in range(runs):
        while True:
            pieces_rolled += 1
            tries_in_batch = 0
            tickets_spent = 0
            successes = 0
            xp_spent = 0
            money_spent = 0

            while tries_in_batch < max_rolls:

                remaining_needed_successes = successes_needed - successes
                probability_of_success = remaining_needed_successes / (13 - tries_in_batch)
                xp_spent += costs[tries_in_batch]
                money_spent += costs[tries_in_batch] * 0.4
                tries_in_batch += 1
                total_tries += 1
                tickets_spent += cost_per_try

                if random.random() < probability_of_success:
                    successes += 1

                if successes == successes_needed:
                    total_tickets_spent += tickets_spent
                    break

            if successes == successes_needed:
                total_xp_spent += sum(costs[tries_in_batch:5]) + xp_spent
                total_money_spent += sum(costs[tries_in_batch:5])*0.4 + money_spent
                break

            xp_spent -= sum(costs[:tries_in_batch]) * refund_xp
            tickets_spent -= tries_in_batch * cost_per_try * refund_cubes
            total_tickets_spent += tickets_spent
            total_xp_spent += xp_spent
            total_money_spent += money_spent

    average_pieces_rolled = pieces_rolled / runs
    average_total_tries = total_tries / runs
    average_total_tickets_spent = total_tickets_spent / runs
    average_xp_spent = total_xp_spent / runs
    average_money = total_money_spent / runs

    return average_pieces_rolled, average_total_tries, average_total_tickets_spent, average_money, average_xp_spent, runs


# Perform Monte Carlo simulation
average_pieces, average_tries, average_tickets, average_money, average_xp, run = simulate_until_success()

# Print results
print(f"Average Pieces Rolled: {average_pieces}")
print(f"Average Total Tries: {average_tries}")
print(f"Average Cubes Spent: {average_tickets}")
print(f"Average Echo XP Spent: {average_xp}")
print(f"Average Money Spent: {average_money}")
print(f"Runs : {run}")
