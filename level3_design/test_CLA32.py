# Cocotb Testbench for 32 bit CLA adder
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random


@cocotb.test()
async def test_basic_CLA32(dut):
    """Test for 32 bit CLA adder which calculates a ='bd999; b='d98999"""

    # input driving 
    a = 0x000003E7
    b = 0x000182b7
    cin = 0
    dut.a.value = a
    dut.b.value = b
    dut.cin.value = cin
    
    cocotb.log.info('a|b||cout|sum')


    await Timer(2, units='ns')

    assert dut.sum.value == a+b, f"Sum result is incorrect: {dut.sum.value} != 99998"
    dut._log.info("Test passed!")

    
    #assert dut.out.value == Inp0, f"Muliplexer has selected wrong input: {dut.sel.value} != 0"

    


