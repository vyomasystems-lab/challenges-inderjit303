# Cocotb Testbench for 32 bit CLA adder
import cocotb
from cocotb.triggers import Timer
import random


@cocotb.test()
async def test_CLA32_Basic(dut):
    """Test for 32 bit CLA adder which calculates a ='bd999; b='d98999"""

    # input driving 
    A = 4294967295
    B = 4294967295
    # Cin = 0
    dut.a.value = A
    dut.b.value = B


    cocotb.log.info('A|B||cout|sum')

    await Timer(2, units='ns')
    
    assert dut.sum.value == A+B, "Adder result is incorrect: {A} + {B} != {SUM}, expected value={EXP}".format(
            A=int(dut.a.value), B=int(dut.b.value), SUM=int(dut.sum.value), EXP=A+B)

@cocotb.test()
async def test_CLA32_randomise(dut):
    """Test for adding two random numbers multiple times"""

    for i in range(10):

        A = random.randint(0, 4294967295)
        B = random.randint(0, 4294967295)
        
        A = 4294967295
        B = 255
        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:10} B={B:10} model={A+B:10} DUT={int(dut.sum.value):10}')
        assert dut.sum.value == A + B  , "Randomised test failed with: {A} + {B} = {SUM}".format(
            A=dut.a.value, B=dut.b.value, SUM=dut.sum.value)
        
    


