import pytest

import calc_module


@pytest.mark.calc
def test_add_calculator():
    result = calc_module.add_function(2, 7)
    print("Result = ",result)


@pytest.mark.calc
def test_sub_calculator():
    result = calc_module.sub_function(2, 7)
    print("Result = ",result)


@pytest.mark.calc
def test_mul_calculator():
    result = calc_module.mul_function(2, 7)
    print("Result = ",result)


@pytest.mark.calc
def test_div_calculator():
    result = calc_module.div_function(2, 7)
    print("Result = ",result)

