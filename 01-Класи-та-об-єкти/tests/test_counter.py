from counter import Counter


def test_starts_from_zero():
    assert Counter().value() == 0


def test_increment_and_decrement():
    counter = Counter()
    counter.increment()
    counter.increment()
    counter.decrement()
    assert counter.value() == 1


def test_decrement_does_not_go_below_zero():
    counter = Counter()
    counter.decrement()
    assert counter.value() == 0


def test_reset_and_independence():
    first, second = Counter(), Counter()
    first.increment()
    second.increment()
    first.reset()
    assert (first.value(), second.value()) == (0, 1)
