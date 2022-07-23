# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test0_basic_mux(dut):
    """Test 0 for mux"""

    Inp0 = 1
    SEL = 0
    
    # input driving 
    dut.sel.value = SEL
    dut.inp0.value = Inp0
    #dut.inp13.value = Inp13
     
    await Timer(2, units='ns')
        
    # cocotb.log.info('##### CTB: Develop your test here ########')
    
    assert dut.out.value == Inp0, f"Muliplexer has selected wrong input: {dut.sel.value} != 0"

    cocotb.log.info('##### CTB: Test 0 #####')


@cocotb.test()
async def test1_basic_mux(dut):
    """Test 1 for mux"""

    Inp1 = 1
    SEL = 1
    
    # input driving 
    dut.sel.value = SEL
    dut.inp1.value = Inp1
     
    await Timer(4, units='ns')
        
    # cocotb.log.info('##### CTB: Develop your test here ########')
    
    assert dut.out.value == Inp1, f"Muliplexer has selected wrong input: {dut.sel.value} != 1"

    cocotb.log.info('##### CTB: Test 1 #####')


@cocotb.test()
async def test2_basic_mux(dut):
    """Test 2 for mux"""

    Inp2 = 1
    SEL = 2
    
    # input driving 
    dut.sel.value = SEL
    dut.inp2.value = Inp2
     
    await Timer(6, units='ns')
        
    assert dut.out.value == Inp2, f"Muliplexer has selected wrong input: {dut.sel.value} != 2"

    cocotb.log.info('##### CTB: Test 2 #####')