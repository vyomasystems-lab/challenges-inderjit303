# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test 1 for 1011 sequence detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Sequence detector Testbench! ######')

    # intitalize input
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut._log.info(f'Input bit: {dut.inp_bit.value}')
    dut._log.info(f'Output sequence: {dut.seq_seen.value}')

    assert dut.seq_seen.value == 1, f'Sequence must be detected but is not detected. Given sequence = 110111. Model Output: {dut.seq_seen.value} Expected Output: 1'
    dut._log.info(f'Input bit: {dut.inp_bit.value}')
    dut._log.info(f'Output sequence: {dut.seq_seen.value}')


@cocotb.test()
async def test_seq_bug2(dut):
    """Test 2 for 1011 sequence detection"""
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)

    dut._log.info(f'Input bit: {dut.inp_bit.value}')
    dut._log.info(f'Output sequence: {dut.seq_seen.value}')
    assert dut.seq_seen.value == 1, f'Sequence must be detected but is not detected. Given sequence = 1010111. Model Output: {dut.seq_seen.value} Expected Ouput: 1'
    
    

    
