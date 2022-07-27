# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def adder_basic_test(dut):
    """Test for 3 + 12"""

    A = 3
    B = 12

    # input driving
    dut.a.value = A
    dut.b.value = B
   
    await Timer(2, units='ns')

    assert dut.sum.value == A+B, f"Adder result is incorrect: {dut.sum.value} != 15"

