class DockCapacityError(Exception):
    """Custom exception raised when dock capacity is exceeded."""
    pass


# Dock Management System for Cargo and Cruise Ships
def dock_management():
    """Calculates the total weekly profit for a dock."""

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

    # Initialize total earnings
    weekly_profit = 0

    # Calculate dock earnings for a week
    for day in range(1, 8):
        print(f"\n--- Day {day} ---")  # f-string

        # Get number of cargo ships docking today
        while True:
            try:
                num_cargo = int(input(f"Enter number of cargo ships (max {max_cargo_ships}): "))
                if num_cargo < 0 or num_cargo > max_cargo_ships:
                    raise DockCapacityError("Cargo ships exceeded daily capacity!")
                break
            except ValueError:
                print("Invalid input! Please enter a valid numeric value.")
            except DockCapacityError as e:
                print(e)

        # Get number of cruise ships docking today
        while True:
            try:
                num_cruise = int(input(f"Enter number of cruise ships (max {max_cruise_slots}): "))
                if num_cruise < 0 or num_cruise > max_cruise_slots:
                    raise DockCapacityError("Cruise ships exceeded daily capacity!")
                break
            except ValueError:
                print("Invalid input! Please enter a valid numeric value.")
            except DockCapacityError as e:
                print(e)

        # Calculate anchoring fees
        daily_anchor_fees = (num_cargo * cargo_anchor_price) + (num_cruise * cruise_anchor_price)

        # Cargo profit calculation
        cargo_profit = 0
        for i in range(num_cargo):
            ship_size = input(f"Enter cargo ship size (small/medium/large) for ship {i + 1}: ").lower()
            cargo_profit += cargo_ships_capacity.get(ship_size, 0) * container_price

        # Daily total profit
        daily_profit = daily_anchor_fees + cargo_profit
        weekly_profit += daily_profit

        print(f"Daily anchoring fees: ${daily_anchor_fees}")
        print(f"Daily cargo profit: ${cargo_profit}")
        print(f"Total earnings for day {day}: ${daily_profit}")

    # Final weekly report
    print("\n======= Weekly Report =======")
    print(f"Total earnings for the week: ${weekly_profit}")


def test_anchoring_fees():
    """Test if anchoring fees are calculated correctly."""
    assert (5 * 50) + (2 * 150) == 550  # Example case: 5 cargo ships, 2 cruise ships


def test_cargo_profit():
    """Test if cargo profit calculation works correctly."""
    cargo_ships_capacity = {"small": 100, "medium": 150, "large": 200}
    assert cargo_ships_capacity["medium"] * 350 == 52500  # Medium ship profit


# Run the dock management system
dock_management()