from light_switch import LightSwitch


def test_new_switch_is_off_with_zero_switches():
    light = LightSwitch()
    assert not light.is_on()
    assert light.switches() == 0


def test_toggle_changes_state_and_counts():
    light = LightSwitch()
    light.toggle()
    assert light.is_on()
    light.toggle()
    assert not light.is_on()
    assert light.switches() == 2


def test_switches_are_independent():
    first, second = LightSwitch(), LightSwitch()
    first.toggle()
    assert second.switches() == 0
    assert not second.is_on()
