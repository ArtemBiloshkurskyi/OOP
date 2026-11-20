from ticket import Ticket


def test_ids_are_increasing():
    first, second = Ticket(), Ticket()
    assert second.id == first.id + 1


def test_created_counts_new_tickets():
    before = Ticket.created()
    Ticket()
    Ticket()
    assert Ticket.created() == before + 2


def test_last_id_equals_created_count():
    ticket = Ticket()
    assert ticket.id == Ticket.created()


def test_ids_are_unique():
    ids = {Ticket().id for _ in range(5)}
    assert len(ids) == 5
