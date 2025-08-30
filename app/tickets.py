# app/tickets.py
tickets = []

def add_ticket(title):
    tickets.append(title)
    print(f"Ticket '{title}' lagd till. Totalt: {len(tickets)}")

def list_tickets():
    for idx, t in enumerate(tickets, start=1):
        print(f"{idx}. {t}")

if __name__ == "__main__":
    while True:
        choice = input("Vill du lägga till en ticket? (ja/nej): ").strip().lower()
        if choice == "ja":
            title = input("Skriv ticket titel: ")
            add_ticket(title)
        else:
            break
    print("\nAlla tickets:")
    list_tickets()
