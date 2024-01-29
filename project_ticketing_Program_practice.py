import datetime

def display_welcome_message():
    print("Welcome to Adventure Theme Park Ticketing System!")
    print("===============================================")

# Ticket prices
ADULT_PRICE = 20
CHILD_PRICE = 12
SENIOR_CITIZEN_PRICE = 11
PARKING_PRICE = 0



def display_ticket_prices():
    print("\nEntrance Ticket Prices:")
    print(f"Adult: £{ADULT_PRICE}")
    print(f"Child: £{CHILD_PRICE}")
    print(f"Senior Citizen: £{SENIOR_CITIZEN_PRICE}")

def get_number_of_tickets(ticket_type):
    while True:
        try:
            num_tickets = int(input(f"How many {ticket_type} tickets are required? "))
            if num_tickets < 0:
                raise ValueError("Number of tickets cannot be negative.")
            return num_tickets
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid positive integer.")

def get_lead_booker_surname():
    return input("Enter the lead booker's surname: ")

def ask_for_parking_pass():
    response = input("Do you require a parking pass for the car park? (yes/no) ").lower()
    return response == 'yes'

def calculate_total_cost(adult_tickets, child_tickets, senior_citizen_tickets, parking_pass):
    total_cost = (ADULT_PRICE * adult_tickets) + (CHILD_PRICE * child_tickets) + (SENIOR_CITIZEN_PRICE * senior_citizen_tickets)
    if parking_pass:
        total_cost += PARKING_PRICE
    return total_cost

def print_ticket(lead_booker_surname, adult_tickets, child_tickets, senior_citizen_tickets):
    print("\nTicket Details:")
    print(f"Lead Booker's Surname: {lead_booker_surname}")
    print(f"Adult Tickets: {adult_tickets}")
    print(f"Child Tickets: {child_tickets}")
    print(f"Senior Citizen Tickets: {senior_citizen_tickets}")
    print(f"Date: {datetime.date.today()}")

def print_parking_pass():
    print("\nCar Parking Pass:")
    print("Free (car pass must be displayed)")

def thank_customer():
    print("\nThank you for your purchase! Enjoy your visit to Adventure Theme Park.")

def main():
    display_welcome_message()
    display_ticket_prices()

    # Get the number of tickets for each category
    adult_tickets = get_number_of_tickets("adult")
    child_tickets = get_number_of_tickets("child")
    senior_citizen_tickets = get_number_of_tickets("senior citizen")

    # Get lead booker's surname
    lead_booker_surname = get_lead_booker_surname()

    # Ask for parking pass
    parking_pass = ask_for_parking_pass()

    # Calculate total cost
    total_cost = calculate_total_cost(adult_tickets, child_tickets, senior_citizen_tickets, parking_pass)

    # Display total cost
    print("\nTotal Cost:", total_cost)

    # Print ticket details
    print_ticket(lead_booker_surname, adult_tickets, child_tickets, senior_citizen_tickets)

    # Print parking pass if requested
    if parking_pass:
        print_parking_pass()

    # Thank the customer
    thank_customer()

if __name__ == "__main__":
    main()



   
