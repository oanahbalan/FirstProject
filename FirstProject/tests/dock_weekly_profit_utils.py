# Dock Management System for Cargo and Cruise Ships

def dock_management():
    """ Calculates the total weekly profit for a dock."""
    # Print the Docstring here.print
    dock_management.__doc__

    # Constants
    max_cargo_ships = 10  # Max cargo ships per day
    max_cruise_slots = 5  # Max cruise slots per day
    cargo_anchor_price = 50  # Price per day for cargo ship
    cruise_anchor_price = 150  # Price per day for cruise ship
    container_price = 350  # Selling price per container

    # Cargo ship capacity
    cargo_ships_capacity = {
        "small": 100,
        "medium": 150,
        "large": 200
    }

    # Ship categories
    ship_types = ("cargo", "cruise")

    # Initialize total earnings
    weekly_profit = 0

    # Calculate dock earnings for a week
    for day in range(1, 8):
        print(f"\n--- Day {day} ---") # f-string

        # Get number of cargo ships docking today
        while True:
            num_cargo = int(input(f"Enter number of cargo ships (max {max_cargo_ships}): "))
            if 0 <= num_cargo <= max_cargo_ships:
                break
            print("Invalid input! Please enter a valid number.")

        # Get number of cruise ships docking today
        while True:
            num_cruise = int(input(f"Enter number of cruise ships (max {max_cruise_slots}): "))
            if 0 <= num_cruise <= max_cruise_slots:
                break
            print("Invalid input! Please enter a valid number.")

        # Calculate anchoring fees
        daily_anchor_fees = (num_cargo * cargo_anchor_price) + (num_cruise * cruise_anchor_price)

        # Cargo profit calculation
        cargo_profit = 0
        for i in range(num_cargo):
            ship_size = input(f"Enter cargo ship size (small/medium/large) for ship {i + 1}: ").lower()
            cargo_profit += cargo_ships_capacity[
                                ship_size] * container_price if ship_size in cargo_ships_capacity else print(
                "Invalid ship size! No earnings added.") # Ternary operator

        # Daily total profit
        daily_profit = daily_anchor_fees + cargo_profit
        weekly_profit += daily_profit

        print(f"Daily anchoring fees: ${daily_anchor_fees}")
        print(f"Daily cargo profit: ${cargo_profit}")
        print(f"Total earnings for day {day}: ${daily_profit}")

    # Final weekly report
    print("\n======= Weekly Report =======")
    print(f"Total earnings for the week: ${weekly_profit}")


# Run the dock management system
dock_management()
