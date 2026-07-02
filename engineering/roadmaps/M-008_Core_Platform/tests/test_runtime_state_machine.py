from runtime_state_machine import RuntimeState

def test_runtime_states_exist():
    assert RuntimeState.RUNNING.value=='running'
