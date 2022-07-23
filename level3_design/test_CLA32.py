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
    dut.a = a
    dut.b = b
    dut.cin = cin
    
    if dut.s != s:
        x = "incorrect result for sum: {} != {}".format(dut.s, int(s))
        raise TestFailure(x)
    elif dut.cout != cout:
        x = "incorrect result for carry: {} != {}".format(dut.cout, int(cout))
        raise TestFailure(x)
    else:
        dut._log.info("passed!")


    # input driving 
    dut.sel.value = SEL
    dut.inp0.value = Inp0
    #dut.inp13.value = Inp13
     
        
  
    
    assert dut.out.value == Inp0, f"Muliplexer has selected wrong input: {dut.sel.value} != 0"

    cocotb.log.info('a|b||cout|sum')


