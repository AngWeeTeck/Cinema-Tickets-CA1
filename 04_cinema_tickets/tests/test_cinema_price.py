"""Unit tests for ticket_price(ticket_count) in cinema_price.py.

Spec 3.1: each ticket costs 1200 cents; zero tickets costs zero; no discounts.
Spec 2: non-int (incl. bool) -> TypeError; negative int -> ValueError.
Test IDs (TC-P-xx) match the Test Case Specification document.
"""
import pytest

from cinema_price import ticket_price


# ---- Valid inputs (equivalence partition + boundary values) ----
@pytest.mark.parametrize(
    "ticket_count, expected",
    [
        pytest.param(0, 0, id="TC-P-01-zero-tickets-costs-zero"),
        pytest.param(1, 1200, id="TC-P-02-one-ticket"),
        pytest.param(2, 2400, id="TC-P-03-two-tickets"),
        pytest.param(10, 12000, id="TC-P-04-typical-quantity"),
        pytest.param(1000, 1200000, id="TC-P-05-large-quantity"),
    ],
)
def test_ticket_price_valid_counts(ticket_count, expected):
    assert ticket_price(ticket_count) == expected





# ---- Invalid value (correct type, outside range) -> ValueError ----
@pytest.mark.parametrize(
    "ticket_count",
    [
        pytest.param(-1, id="TC-P-06-just-below-lower-bound"),
        pytest.param(-100, id="TC-P-07-large-negative"),
    ],
)
def test_ticket_price_negative_raises_value_error(ticket_count):
    with pytest.raises(ValueError):
        ticket_price(ticket_count)


# ---- Invalid type -> TypeError ----
@pytest.mark.parametrize(
    "bad_value",
    [
        pytest.param(2.5, id="TC-P-08-float"),
        pytest.param(2.0, id="TC-P-09-float-with-integer-value"),
        pytest.param("3", id="TC-P-10-string"),
        pytest.param(None, id="TC-P-11-none"),
        pytest.param(True, id="TC-P-12-bool-true"),
        pytest.param(False, id="TC-P-13-bool-false"),
        pytest.param([1], id="TC-P-14-list"),
    ],
)
def test_ticket_price_invalid_type_raises_type_error(bad_value):
    with pytest.raises(TypeError):
        ticket_price(bad_value)
