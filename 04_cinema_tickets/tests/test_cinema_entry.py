"""Unit tests for can_watch(age) in cinema_entry.py.

Spec 3.2: age >= 16 may watch (True); age < 16 may not (False); returns a bool.
Spec 2: non-int (incl. bool) -> TypeError; negative int -> ValueError.
Test IDs (TC-E-xx) match the Test Case Specification document.
"""
import pytest

from cinema_entry import can_watch


# ---- Valid inputs: boundary at 16 ----
@pytest.mark.parametrize(
    "age, expected",
    [
        pytest.param(0, False, id="TC-E-01-lower-bound-0"),
        pytest.param(1, False, id="TC-E-02-just-above-lower-bound"),
        pytest.param(10, False, id="TC-E-03-child"),
        pytest.param(15, False, id="TC-E-04-just-below-threshold"),
        pytest.param(16, True, id="TC-E-05-exactly-at-threshold"),
        pytest.param(17, True, id="TC-E-06-just-above-threshold"),
        pytest.param(30, True, id="TC-E-07-adult"),
        pytest.param(120, True, id="TC-E-08-very-old"),
    ],
)
def test_can_watch_valid_ages(age, expected):
    assert can_watch(age) is expected



# ---- Invalid value (correct type, outside range) -> ValueError ----
@pytest.mark.parametrize(
    "age",
    [
        pytest.param(-1, id="TC-E-09-just-below-lower-bound"),
        pytest.param(-50, id="TC-E-10-large-negative"),
    ],
)
def test_can_watch_negative_raises_value_error(age):
    with pytest.raises(ValueError):
        can_watch(age)


# ---- Invalid type -> TypeError ----
@pytest.mark.parametrize(
    "bad_value",
    [
        pytest.param(16.0, id="TC-E-11-float-with-integer-value"),
        pytest.param(15.5, id="TC-E-12-float"),
        pytest.param("18", id="TC-E-13-string"),
        pytest.param(None, id="TC-E-14-none"),
        pytest.param(True, id="TC-E-15-bool-true"),
        pytest.param(False, id="TC-E-16-bool-false"),
        pytest.param([18], id="TC-E-17-list"),
    ],
)
def test_can_watch_invalid_type_raises_type_error(bad_value):
    with pytest.raises(TypeError):
        can_watch(bad_value)
