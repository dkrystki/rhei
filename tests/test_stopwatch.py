from rhei import Stopwatch


def test_basic_timing(time_mock):
    time_mock.return_value = 100.0
    stopwatch = Stopwatch()
    assert stopwatch.get() == 0.0
    assert not stopwatch.counting
    time_mock.return_value = 110.0
    stopwatch.start()
    assert stopwatch.counting

    time_mock.return_value = 120.0
    assert float(stopwatch) == 10.0


def test_pausing(time_mock):
    time_mock.return_value = 100.0
    stopwatch = Stopwatch()
    stopwatch.start()
    assert stopwatch.counting

    time_mock.return_value = 110.0
    assert stopwatch.value == 10.0

    stopwatch.pause()
    time_mock.return_value = 120.0
    assert stopwatch.value == 10.0
    assert not stopwatch.counting

    stopwatch.start()
    time_mock.return_value = 130.0
    assert stopwatch.get() == 20.0
    assert stopwatch.counting

    stopwatch.pause()
    time_mock.return_value = 140.0
    assert stopwatch.get() == 20.0
    assert not stopwatch.counting

    stopwatch.start()
    time_mock.return_value = 150.0
    assert stopwatch.get() == 30.0
    assert stopwatch.counting


def test_pausing_twice(time_mock):
    time_mock.return_value = 0.0
    stopwatch = Stopwatch()
    stopwatch.start()
    assert stopwatch.counting

    time_mock.return_value = 10.0
    assert stopwatch.get() == 10.0
    assert stopwatch.counting

    time_mock.return_value = 20.0
    stopwatch.pause()
    assert not stopwatch.counting

    time_mock.return_value = 30.0
    stopwatch.pause()
    assert stopwatch.get() == 20.0
    assert not stopwatch.counting


def test_resetting(time_mock):
    time_mock.return_value = 0.0
    stopwatch = Stopwatch()
    stopwatch.start()
    assert stopwatch.counting

    time_mock.return_value = 10.0
    assert stopwatch.get() == 10.0
    assert stopwatch.counting

    time_mock.return_value = 20.0
    stopwatch.reset()
    assert stopwatch.get() == 0.0
    assert stopwatch.counting

    time_mock.return_value = 30.0
    assert stopwatch.get() == 10.0
    assert stopwatch.counting

    time_mock.return_value = 40.0
    stopwatch.pause()
    time_mock.return_value = 50.0
    assert stopwatch.get() == 20.0
    assert not stopwatch.counting


def test_pause_and_reset(time_mock):
    time_mock.return_value = 1000.0
    stopwatch = Stopwatch()
    stopwatch.start()
    assert stopwatch.counting

    time_mock.return_value = 1010.0
    assert stopwatch.get() == 10.0
    assert stopwatch.counting

    time_mock.return_value = 1020.0
    stopwatch.pause()
    assert stopwatch.get() == 20.0
    assert not stopwatch.counting

    time_mock.return_value = 1030.0
    stopwatch.reset()
    time_mock.return_value = 1040.0
    assert stopwatch.get() == 0.0
    assert not stopwatch.counting


def test_stopping(time_mock):
    time_mock.return_value = 1000.0
    stopwatch = Stopwatch()
    stopwatch.start()
    assert stopwatch.counting

    time_mock.return_value = 1010.0
    assert stopwatch.get() == 10.0
    assert stopwatch.counting

    time_mock.return_value = 1020.0
    stopwatch.stop()
    assert stopwatch.get() == 0.0
    assert not stopwatch.counting

    time_mock.return_value = 1030.0
    assert stopwatch.get() == 0.0
    time_mock.return_value = 1040.0
    assert stopwatch.get() == 0.0
    assert not stopwatch.counting

    time_mock.return_value = 1020.0
    stopwatch.reset(10.0)
    assert stopwatch.get() == 10.0
    assert not stopwatch.counting

    time_mock.return_value = 1030.0
    assert stopwatch.get() == 10.0
    assert not stopwatch.counting


def test_initial_value(time_mock):
    time_mock.return_value = 1000.0
    stopwatch = Stopwatch(10.0)
    assert not stopwatch.counting
    assert stopwatch.get() == 10.0

    stopwatch.start()
    time_mock.return_value = 1010.0
    assert stopwatch.get() == 20.0


def test_reverse_counting(time_mock):
    time_mock.return_value = 1000.0
    stopwatch = Stopwatch(10.0)
    assert not stopwatch.counting
    assert stopwatch.get() == 10.0

    stopwatch.start()
    time_mock.return_value = 1010.0
    assert stopwatch.get() == 20.0

    stopwatch.start(reversed=True)
    time_mock.return_value = 1020.0
    assert stopwatch.get() == 10.0

    stopwatch.start(reversed=False)
    stopwatch.start()
    time_mock.return_value = 1030.0
    assert stopwatch.get() == 20.0

    time_mock.return_value = 1050.0
    stopwatch.stop()
    stopwatch.reset(100.0)
    stopwatch.start(reversed=True)
    time_mock.return_value = 1080.0
    assert stopwatch.get() == 70.0


def test_repr(time_mock):
    time_mock.return_value = 1000.0
    stopwatch = Stopwatch(0.0)
    stopwatch.start()
    time_mock.return_value = 1010.0

    assert repr(stopwatch) == "10.0"
