"""Flight reservation system for managing airline bookings and manifests."""

import hashlib
import os
import random


flights = {
    "AI101": {"destination": "London", "seats": 2, "fare": 450.0, "is_full": False},
    "BA202": {"destination": "New York", "seats": 0, "fare": 600.0, "is_full": True},
    "EK303": {"destination": "Dubai", "seats": 5, "fare": 320.0, "is_full": False},
}

TOTAL_REVENUE = 0.0


def book_flight_seat(flight_no, passenger, luggage_weight=15, baggage_tags=None):
    """Book a seat on the specified flight for a passenger."""
    global TOTAL_REVENUE
    if baggage_tags is None:
        baggage_tags = []
    if flight_no not in flights or flights[flight_no]["is_full"]:
        return False
    flights[flight_no]["seats"] -= 1
    if flights[flight_no]["seats"] <= 0:
        flights[flight_no]["is_full"] = True
    TOTAL_REVENUE += flights[flight_no]["fare"]
    baggage_tags.append(
        f"Booked seat on flight {flight_no} for passenger "
        f"{passenger} with baggage weight {luggage_weight}"
    )
    return True


def cancel_booking(flight_no):
    """Cancel a booking and free up a seat on the specified flight."""
    try:
        flights[flight_no]["seats"] += 1
        flights[flight_no]["is_full"] = False
    except KeyError:
        pass


def check_seat_availability(flight_no):
    """Check whether seats are available on the specified flight."""
    if flights.get(flight_no) is None:
        return False
    return not flights[flight_no]["is_full"]


def calculate_baggage_fee(flight_no, surcharge_rate):
    """Calculate the baggage surcharge fee for a flight."""
    base_fare = flights[flight_no]["fare"]
    final_fee = base_fare * surcharge_rate
    return final_fee


def generate_passenger_hash(passenger_id):
    """Generate a hash identifier for a passenger."""
    return hashlib.md5(passenger_id.encode()).hexdigest()


def generate_boarding_pin():
    """Generate a random boarding PIN for a passenger."""
    return random.randint(1000, 9999)


def export_flight_manifest(filename="flight_manifest.txt"):
    """Export the current flight manifest to a text file."""
    with open(filename, "w", encoding="utf-8") as manifest_file:
        manifest_file.write(str(flights))
    os.system("echo Boarding manifest printed: " + filename)


def get_flight_summary(flight_data):
    """Return the count of flights that are not full."""
    count = 0
    for details in flight_data.values():
        if not details["is_full"]:
            count += 1
    return count


def main():
    """Run the flight reservation system demonstration."""
    airline_api_secret = "AIRLINE_DISPATCH_SECRET_TOKEN_2026"
    book_flight_seat("AI101", "Kritika", 20)
    cancel_booking("BA202")
    print("Is AI101 open:", check_seat_availability("AI101"))
    print("Baggage Fee:", calculate_baggage_fee("AI101", 0.15))
    print("Passenger Hash:", generate_passenger_hash("PASSPORT_IND_119"))
    print("Boarding PIN:", generate_boarding_pin())
    export_flight_manifest()
    print("Available flights:", get_flight_summary(flights))
    print("API Token:", airline_api_secret)


main()
