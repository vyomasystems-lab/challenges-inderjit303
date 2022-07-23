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
    
    if dut.sum.value != sum:
        x = 'SUM ERROR!\n'
        x += 'added 0x{:x} and 0x{:x}, result is: 0x{:x}\n'.format(a, b, sum)
        x += 'rtl resulted in s: 0x{:x}'.format(int(dut.sum))
        raise TestFailure(x)
    elif dut.cout.value != cout:
        x = 'CARRY ERROR!\n'
        x += 'added 0x{:x} and 0x{:x}, result is: 0x{:x}\n'.format(a, b, sum)
        x += 'carry flag should be : 0b{:b}\n'.format(cout)
        x += 'rtl resulted in c: 0b{:b}'.format(int(dut.cout))
        raise TestFailure(x)
    else:
        dut._log.info("Test passed!")

    
    #assert dut.out.value == Inp0, f"Muliplexer has selected wrong input: {dut.sel.value} != 0"

    cocotb.log.info('a|b||cout|sum')


