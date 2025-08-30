from app.tickets_file import add_ticket, remove_ticket, update_ticket

def test_add_ticket():
    tickets = []
    add_ticket("Test 1", tickets)
    assert tickets == ["Test 1"]

def test_remove_ticket():
    tickets = ["A", "B", "C"]
    remove_ticket(2, tickets)  # tar bort "B"
    assert tickets == ["A", "C"]

def test_update_ticket():
    tickets = ["Old"]
    update_ticket(1, "New", tickets)
    assert tickets == ["New"]
