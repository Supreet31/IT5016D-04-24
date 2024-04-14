
# Class Ticket to get the ticket data 
class Ticket:
    ticket_counter = 0

    def __init__(self, staff_id, staff_name, email, description, status="open"):
        Ticket.ticket_counter += 1
        self.ticket_number = Ticket.ticket_counter + 2000
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.email = email
        self.description = description
        self.it_response = "Not Yet Provided" 
        self.status = status

    def __str__(self):
        return (
            f"Ticket Number: {self.ticket_number}\n"
            f"Ticket Creator: {self.staff_name}\n"
            f"Staff ID: {self.staff_id}\n"
            f"Email Address: {self.email}\n"
            f"Description: {self.description}\n"
            f"Response: {self.it_response}\n"
            f"Ticket Status: {self.status}")

# Class HelpDesk will manage the collection of tickets  and will provide ticket related functionalities.
class HelpDesk:
    def __init__(self):
        self.tickets = [] # List for tickets

    def submit_ticket(self):
        print("\n*** Submit a New Ticket ***")
        staff_id = input("Your Staff ID: ")
        staff_name = input("Your Name: ")
        email = input("Email: ")
        description = input("Describe your issue:\nIf you would like to change your password, Type 'password change':  ")
# Password function
        if "password change" in description.lower():
            new_password = self.generate_password(staff_id, staff_name)
            print(f"Generated Password: {new_password}")
            status = "Closed"
        else:
            new_password = None
            status = "open"

        new_ticket = Ticket(staff_id, staff_name, email, description, status)
        self.tickets.append(new_ticket)
        print(f"Ticket '{description}' added successfully with Ticket Number: {new_ticket.ticket_number}")
        print(f"Status: {status}")

#generate a password using a rule-- The first two characters of the staffID, followed by the first three characters of the ticket creator name.
    def generate_password(self, staff_id, staff_name):
        password = staff_id[:2] + staff_name[:3]
        return password

#Close the ticket
    def close_ticket(self):
        print("\n*** Close an Existing Ticket ***")
        ticket_number = int(input("Enter the ticket number to close: "))  

        for ticket in self.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.status = "Closed"
                print(f"Ticket {ticket_number} has been closed.")
                return

        print(f"Ticket {ticket_number} not found.")
# Reopen a ticket
    def reopen_ticket(self):
        print("\n=== Re-open a Closed Ticket ===")
        ticket_number = int(input("Enter the ticket number to re-open: "))  

        for ticket in self.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.status = "open"
                print(f"Ticket {ticket_number} has been re-opened.")
                return

        print(f"Ticket {ticket_number} not found.")
#Display tickets
    def display_tickets(self):
        print("\n=== Printing Tickets ===")
        if not self.tickets:
            print("No tickets to print.")
        else:
            for ticket in self.tickets:
                print(ticket)
                print("--------------------------------------------------------")
#Tickets Stats
    def ticket_statistics(self):
        print("\n=== Displaying Ticket Statistics ===")
        total_tickets = len(self.tickets)
        resolved_tickets = sum(1 for ticket in self.tickets if ticket.status == "Closed")
        open_tickets = total_tickets - resolved_tickets

        print(f"Tickets Created: {total_tickets}")
        print(f"Tickets Resolved: {resolved_tickets}")
        print(f"Tickets To Solve: {open_tickets}")

#main function will serve as an entry point to the program interacting with helpdesk to manage tickets 
def main():
    help_desk = HelpDesk()

    while True:
        print("\n**************************")
        print("Welcome to IT HelpDesk")
        print("**************************")
        print("Please select from the following options:")
        print("--------------------------------------------------------")
        print("0: Submit a New Ticket")
        print("1: Close an Existing Ticket")
        print("2: Re-open a Closed Ticket")
        print("3: Display All Tickets")
        print("4: Ticket Statistics")
        print("5: Exit")
        print("--------------------------------------------------------")

        choice = input("Select an option (0-5): ")

        if choice == "0":
            help_desk.submit_ticket()
        elif choice == "1":
            help_desk.close_ticket()
        elif choice == "2":
            help_desk.reopen_ticket()
        elif choice == "3":
            help_desk.display_tickets()
        elif choice == "4":
            help_desk.ticket_statistics()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")


if __name__ == "__main__":
    main()
