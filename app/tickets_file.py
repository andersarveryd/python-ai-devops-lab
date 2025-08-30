TICKET_FILE = "tickets.txt"

def load_tickets():
    """Läser tickets från fil och returnerar som lista"""
    try:
        with open(TICKET_FILE, "r") as f:
            tickets = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tickets = []
    return tickets

def save_tickets(tickets):
    """Skriver tickets till fil"""
    with open(TICKET_FILE, "w") as f:
        for t in tickets:
            f.write(t + "\n")

def add_ticket(title, tickets):
    tickets.append(title)
    save_tickets(tickets)
    print(f"Ticket '{title}' lagd till. Totalt: {len(tickets)}")

def remove_ticket(position, tickets):
    """Tar bort ticket på given position (1-baserad)"""
    if 1 <= position <= len(tickets):
        removed = tickets.pop(position - 1)
        save_tickets(tickets)
        print(f"Ticket '{removed}' på position {position} borttagen!")
    else:
        print(f"Inget borttaget. Ogiltig position: {position}")

def update_ticket(position, new_title, tickets):
    """Uppdaterar ticket på given position"""
    if 1 <= position <= len(tickets):
        old_title = tickets[position - 1]
        tickets[position - 1] = new_title
        save_tickets(tickets)
        print(f"Ticket på position {position} uppdaterad: '{old_title}' → '{new_title}'")
    else:
        print(f"Inget uppdaterat. Ogiltig position: {position}")

def list_tickets(tickets):
    if tickets:
        for idx, t in enumerate(tickets, start=1):
            print(f"{idx}. {t}")
    else:
        print("Inga tickets än.")

if __name__ == "__main__":
    tickets = load_tickets()
    
    while True:
        print("\nNuvarande tickets:")
        list_tickets(tickets)
        
        choice = input(
            "\nSkriv 'l' för lägg till, 'r' för ta bort, 'u' för uppdatera, eller 'sluta' för att avsluta: "
        ).strip().lower()

        if choice == "sluta":
            break
        elif choice == "l":
            title = input("Skriv ticket titel: ").strip()
            if title:
                add_ticket(title, tickets)
        elif choice == "r":
            pos = input("Skriv nummer på ticket som ska tas bort: ").strip()
            if pos.isdigit():
                remove_ticket(int(pos), tickets)
            else:
                print("Ogiltig position")
        elif choice == "u":
            pos = input("Skriv nummer på ticket som ska uppdateras: ").strip()
            if pos.isdigit():
                new_title = input("Skriv nytt namn för ticket: ").strip()
                if new_title:
                    update_ticket(int(pos), new_title, tickets)
            else:
                print("Ogiltig position")
        else:
            print("Ogiltigt val, försök igen.")

    print("\nSlutlig lista av tickets:")
    list_tickets(tickets)
