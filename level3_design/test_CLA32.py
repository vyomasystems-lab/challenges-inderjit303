# Cocotb Testbench for 32 bit CLA adder
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
from cocotb.result import ReturnValue
import random


@cocotb.test()
async def test_basic_CLA32(dut):
    """Test for 32 bit CLA adder which calculates a ='bd999; b='d98999"""

    # input driving 
    A = 999
    B = 98999
    Cin = 0
    dut.a.value = A
    dut.b.value = B
    dut.cin.value = Cin
    
    cocotb.log.info('A|B||cout|sum')


    await Timer(2, units='ns')

    # run model and get the results
    sum, cout = test_basic_CLA32(dut.sum.value)

    if dut.sum.value != sum:
         x = "incorrect result for sum: {} != {}".format(dut.sum.value, int(sum))
         raise TestFailure(x)
    elif dut.cout.value != cout:
        x = "incorrect result for carry: {} != {}".format(dut.cout.value, int(cout))
        raise TestFailure(x)
    else:
        dut._log.info("Test is passed!")
    


