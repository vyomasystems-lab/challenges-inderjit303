# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    Inp30 = 1
    SEL = 30
    
    # input driving 
    dut.sel.value = SEL
    dut.inp30.value = Inp30
    #dut.inp13.value = Inp13
     
    await Timer(2, units='ns')
        
    # cocotb.log.info('##### CTB: Develop your test here ########')
    
    assert dut.out.value == Inp30, f"Muliplexer has selected wrong input: {dut.sel.value} = 30"
