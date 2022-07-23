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
