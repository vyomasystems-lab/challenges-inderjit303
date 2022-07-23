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
     
    await Timer(2, units='ns')
        
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
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp2, f"Muliplexer has selected wrong input: {dut.sel.value} != 2"

    cocotb.log.info('##### CTB: Test 2 #####')

@cocotb.test()
async def test3_basic_mux(dut):
    """Test 3 for mux"""

    Inp3 = 1
    SEL = 3
    
    # input driving 
    dut.sel.value = SEL
    dut.inp3.value = Inp3
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp3, f"Muliplexer has selected wrong input: {dut.sel.value} != 3"

    cocotb.log.info('##### CTB: Test 3 #####')

@cocotb.test()
async def test4_basic_mux(dut):
    """Test 4 for mux"""

    Inp4 = 1
    SEL = 4
    
    # input driving 
    dut.sel.value = SEL
    dut.inp4.value = Inp4
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp4, f"Muliplexer has selected wrong input: {dut.sel.value} != 4"

    cocotb.log.info('##### CTB: Test 4 #####')

@cocotb.test()
async def test5_basic_mux(dut):
    """Test 5 for mux"""

    Inp5 = 1
    SEL = 5
    
    # input driving 
    dut.sel.value = SEL
    dut.inp5.value = Inp5
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp5, f"Muliplexer has selected wrong input: {dut.sel.value} != 5"

    cocotb.log.info('##### CTB: Test 5 #####')

@cocotb.test()
async def test6_basic_mux(dut):
    """Test 6 for mux"""

    Inp6 = 1
    SEL = 6
    
    # input driving 
    dut.sel.value = SEL
    dut.inp6.value = Inp6
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp6, f"Muliplexer has selected wrong input: {dut.sel.value} != 6"

    cocotb.log.info('##### CTB: Test 6 #####')



