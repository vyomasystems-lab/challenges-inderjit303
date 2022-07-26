# challenges-inderjit303
challenges-inderjit303 created by GitHub Classroom

# Level 1 Design 1 (Mux Design Verification)

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Gitpod id is included in the screenshot shown below*

![l1d1_image1](https://user-images.githubusercontent.com/99788755/182015934-d71a6af6-e681-4be8-ba86-7d8c379be922.png)


## Verification Environment (Level 1 Design 1)

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 5-bit select input *sel*, 1-bit inputs *inp0* to *inp30* and it gives 1-bit output *out*.

A cocotb Testbench is created for each individual inputs *inpo* to *inp30*. 
In each cocotb test, the inputs are first assigned values and then are driven as follows:

```
 Inp0 = 1
 SEL = 0
```

```
 # input driving 
 dut.sel.value = SEL
 dut.inp0.value = Inp0
```

31 such cocotb tests are created for testing all states of input and monitoring output.

![l1d1_image2](https://user-images.githubusercontent.com/99788755/182016224-2026ce7f-2b9e-481f-89b3-f7a1867a0fb3.png)

The assert statement is used for comparing the multiplexer's output to the expected value and the cocotb log command display's the user typed message as shown below: 

![l1d1_image3](https://user-images.githubusercontent.com/99788755/182016740-c253fc77-eacc-4a3e-9b22-b8d92ad93266.png)


The following error's are observed:

**Error 1**
```
test12_basic_mux failed
Traceback (most recent call last):
File "/workspace/challenges-inderjit303/level1_design1/test_mux.py", line 236, in test12_basic_mux
assert dut.out.value == Inp12, f"Muliplexer output is incorrect: {dut.sel.value} != 12"
AssertionError: Muliplexer output is incorrect: 01100 != 12
```

**Error 2**
```
test30_basic_mux failed
Traceback (most recent call last):
File "/workspace/challenges-inderjit303/level1_design1/test_mux.py", line 560, in test30_basic_mux
assert dut.out.value == Inp30, f"Muliplexer output is incorrect: {dut.sel.value} != 30"
AssertionError: Muliplexer output is incorrect: 11110 != 30
```

## Test Scenario **(Level 1 Design 1)**
Cocotb tests are created for testing all states of input and monitoring outputs purposes. This makes sure that all the inputs are compared with expected output and DUT output. 

The following cases reveals incorrect outputs for 2 such inputs cases: 

Case 1: 
- Test inputs: Inp12 = 1 and SEL = 12
- Expected Output: out = 12
- Observed Output in the DUT dut.out.value != Inp12 != 12

Case 2: 
- Test inputs: Inp12 = 1 and SEL = 30
- Expected Output: out = 30
- Observed Output in the DUT dut.out.value != Inp30 != 30

Output mismatches for the above inputs proving that there is a **design bug in Level 1 Design 1**

![l1d1_image4](https://user-images.githubusercontent.com/99788755/182018143-9dd1cbe3-3dd1-4b98-9517-734b1242c366.png)


## Design Bug (Level 1 Design 1)
Based on the above test input and analysing the design, two bugs in the code were detected as discussed below: 

```
5'b01101: out = inp12;     ====> BUG 1
5'b01101: out = inp13;
5'b01110: out = inp14;            
```

For the mux design, the logic should be '5'b01100: out = inp12' instead of '5'b01101: out = inp12' as in the design code.

```
5'b11100: out = inp28;
5'b11101: out = inp29;
default: out = 0;          ====> BUG 2
```

For the mux design, the logic should be '5'b11110: out = inp30' instead of 'default: out = 0' as in the design code.


## Design Fix (Level 1 Design 1)
Updating the verilog design code and re-running the test makes the test pass.

![l1d1_image6](https://user-images.githubusercontent.com/99788755/182022235-bd16f2d3-8efd-462f-9e0b-120b8c50d833.png)

The updated design is updated in the folder 'fixed_level1_design1'

## Verification Strategy (Level 1 Design 1)
As explained in test scenarios above, bug free verilog code is updated in folder named **fixed_level1_design1**.
The following bugs were detected and corrected.

Case 1: 
- Test inputs: Inp12 = 1 and SEL = 12
- Expected Output: out = 12
- Observed Output in the DUT dut.out.value = Inp12 = 12

Case 2: 
- Test inputs: Inp12 = 1 and SEL = 30
- Expected Output: out = 30
- Observed Output in the DUT dut.out.value = Inp30 = 30

Output matches for the above inputs proving that **Level 1 Design 1 is bug free**

![l1d1_image5](https://user-images.githubusercontent.com/99788755/182021868-8bf24130-1865-4fdd-a2f5-2fca44ae3207.png)

## Is the verification complete for Level 1 Design 1 ?   
The bugs present in original verilog code were detected using cocotb testbench verification on level1_design1 MUX code. 
The bugs were located in code and updated bug-free. The same Cocotb test which detected the bugs, now with modified changes in the code, passes without committing any errors.
Hence, the verification of Mux Level 1 Design 1 is complete. 

# 
#
#

# Level 1 Design 2 (Sequence Detector Verification)

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Gitpod id is included in the screenshot shown below*

![l1d2_image1](https://user-images.githubusercontent.com/99788755/182026222-2b934776-da3e-4fab-a0e0-0ae27012771a.png)


## Verification Environment (Level 1 Design 2)

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives input sequence of bits to the Design Under Test (seq_detect_1011 module here) which takes in 1-bit input *clk*, *reset*, *inp_bit* and it gives 1-bit output *seq_seen*.

A cocotb Testbench is created to detect the input sequence pattern 1011. Sequence detector accepts input *inp_bit* a string a bits either 0 or 1. The output *seq_seen* goes high when the target sequence *1011* has been detected with overlap sequence. 

In cocotb testbench, the inputs are first assigned values and then are driven as follows:

![l1d2_image3](https://user-images.githubusercontent.com/99788755/182026472-14d29353-abd1-407a-bf04-392bdb521470.png)

Next, a 10us period clock is created on port clk and clock is started with reset. Cocotb tests are created for the input sequence *1101111*

![l1d2_image2](https://user-images.githubusercontent.com/99788755/182026315-cc3e90d8-3b41-4d84-a3c9-d01812fd9aaa.png)


The assert statement is used for comparing the current state value to the expected sequence 1011 and the cocotb log command display's the user typed message as shown below:

![l1d2_image4](https://user-images.githubusercontent.com/99788755/182026399-0140428f-a820-4503-8587-a7aa8324d9f4.png)


The following error's are observed:

**Error message**
```
test_seq_bug failed
Traceback (most recent call last):
File "/workspace/challenges-inderjit303/level1_design2/test_seq_detect_1011.py", line 78, in test_seq_bug
assert dut.current_state.value == dut.SEQ_1011.value, f"Sequence must be detected but is not detected {dut.current_state.value}!= {dut.SEQ_1011.value}"
AssertionError: Sequence must be detected but is not detected 000!= 4
```

## Test Scenario **(Level 1 Design 2)**
Cocotb tests are created for testing all states of input and monitoring outputs purposes. This makes sure that the input sequence are compared with expected output and DUT output.

![l1d2_image6](https://user-images.githubusercontent.com/99788755/182026718-6ac98353-878a-428b-8665-33856b524d75.png)


The following cases reveals incorrect outputs for following input sequence cases: 

- Test input sequence: *1101111*
- Expected Output: seq_seen = 1 or dut.SEQ_1011.value = 4
- Observed Output in the DUT i.e Sequence must be detected but is not detected if dut.current_state.value != dut.SEQ_1011.value 

Output mismatches for the above inputs proving that there is a **design bug in Level 1 Design 2**

![l1d2_image5](https://user-images.githubusercontent.com/99788755/182026652-191b1c45-40bd-4cbc-8d2e-4272d4ee6758.png)


## Design Bug (Level 1 Design 2)
Based on the above test input and analysing the design, the following bugs in the code are detected as discussed below: 

```
SEQ_1:
   begin
      if(inp_bit == 1)
        next_state = IDLE;   ====> BUG 1
      else
        next_state = SEQ_10;   ====> BUG 2
    end
```

For the sequence detector design, IDLE and SEQ_10 should be interchanged in the design code. 


## Design Fix (Level 1 Design 2)
Updating the verilog design code and re-running the test makes the test pass.

![l1d2_image7](https://user-images.githubusercontent.com/99788755/182026727-cd48515e-366c-4ccc-b2cb-34490df96dd9.png)


The updated design is updated in the folder 'fixed_level1_design2'

## Verification Strategy (Level 1 Design 2)
As explained in test scenarios above, bug free verilog code is updated in folder named **fixed_level1_design2**.
The following bugs were detected and corrected.

```
SEQ_1:
   begin
     if(inp_bit == 1)
       next_state = SEQ_10;
       // this statement causes bug in the code
     else
       next_state = IDLE;
       // this statement causes bug in the code
    end
```

Sequence 1011 is detected proving that **Level 1 Design 2 is bug free**

![l1d2_image8](https://user-images.githubusercontent.com/99788755/182026698-6d8e7a17-a4c0-4ee2-9fd7-3765f61d81de.png)


## Is the verification complete ?   (Level 1 Design 2)
Yes, the bugs were detected using cocotb testbench on level1_design2 Sequence detector code. 
The bugs were located and rectified. The same Cocotb test which detected the bugs, now with modified changes in the code, passes without committing any errors.
Hence, the verification of Sequence Detector Level 1 Design 2 is complete.  


# 
#
#

# Level 2 Design (Bitmanipulation co-processor)

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.


## Test Scenario **(Level 1 Design 1)**
Cocotb tests are created for testing most of the instructions states.


Following is the testbench which catches the bug in Level 2 Design: 

```

# Test 3   
@cocotb.test()
def run_test_3(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


    ######### CTB : Test 3 to expose the bug #############
    # input transaction

    mav_putvalue_src1 = 0b00000000000000001010101010100000
    mav_putvalue_src2 = 0b00000000000000000000000000000011
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0b01000000000000000111000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    print(f'SRC1 value in binary: {dut.mav_putvalue_src1.value}')
    print(f'SRC1 value in hex: {hex(dut.mav_putvalue_src1.value)}')
    print(f'SRC2 value in binary: {dut.mav_putvalue_src2.value}')
    print(f'SRC2 value in hex: {hex(dut.mav_putvalue_src2.value)}')
    print(f'SRC3 value in binary: {dut.mav_putvalue_src3.value}')
    print(f'SRC3 value in hex: {hex(dut.mav_putvalue_src3.value)}')
    print(f'Instruction value in binary: {dut.mav_putvalue_instr.value}')
    print(f'Instruction value in hex: {hex(dut.mav_putvalue_instr.value)}')
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

```
![failtest](https://user-images.githubusercontent.com/99788755/182216610-e53cf013-3dd5-4cce-b825-290fd61b007a.png)

The above images shows that DUT and expected output are not matching, thus fails the test 

**The error message displayed in the terminal: **

```
0.00ns INFO     running run_test_1 (1/21)
     0.01ns INFO     DUT OUTPUT=0x0
     0.01ns INFO     EXPECTED OUTPUT=0x0
SRC1 value in binary: 00000000000000000000000000000101
SRC1 value in hex: 0x5
SRC2 value in binary: 00000000000000000000000000000000
SRC2 value in hex: 0x0
SRC3 value in binary: 00000000000000000000000000000000
SRC3 value in hex: 0x0
Instruction value in binary: 00010000000100000001000010110011
Instruction value in hex: 0x101010b3
     0.01ns INFO     run_test_1 passed
     0.01ns INFO     running run_test_3 (2/21)
--ANDN 1
     0.02ns INFO     DUT OUTPUT=0x1
     0.02ns INFO     EXPECTED OUTPUT=0x15541
SRC1 value in binary: 00000000000000001010101010100000
SRC1 value in hex: 0xaaa0
SRC2 value in binary: 00000000000000000000000000000011
SRC2 value in hex: 0x3
SRC3 value in binary: 00000000000000000000000000000000
SRC3 value in hex: 0x0
Instruction value in binary: 01000000000000000111000000110011
Instruction value in hex: 0x40007033
     0.02ns INFO     run_test_3 failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-inderjit303/level2_design/test_mkbitmanip.py", line 123, in run_test_3
                         assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x1 does not match MODEL = 0x15541
     0.02ns INFO     running run_test_4 (3/21)
--ANDN 1
     0.04ns INFO     DUT OUTPUT=0x1
     0.04ns INFO     EXPECTED OUTPUT=0x1
SRC1 value in binary: 00000000000000000000000000000000
SRC1 value in hex: 0x0
SRC2 value in binary: 00000000000000000000000000000011
SRC2 value in hex: 0x3
SRC3 value in binary: 00000000000000000000000000000000
SRC3 value in hex: 0x0
Instruction value in binary: 01000000000000000111000000110011
Instruction value in hex: 0x40007033
     0.04ns INFO     run_test_4 passed


```


#
#
#

# Level 3 Design (32 bit CLA adder)

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.


## Test Scenario **(Level 3 Design)**
Cocotb tests are created for testing for the input states 

## Testbench code for Adder 

```
# Cocotb Testbench for 32 bit CLA adder
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_CLA32_Basic(dut):
    """Test for 32 bit CLA adder which calculates a ='bd999; b='d98999"""

    # input driving 
    A = 429
    B = 429
    dut.a.value = A
    dut.b.value = B

    cocotb.log.info('A|B||cout|sum')

    await Timer(2, units='ns')
    
    assert dut.sum.value == A + B, "Adder result is incorrect: {A} + {B} != {SUM}".format(
    A=int(dut.a.value) , B=int(dut.b.value), SUM=int(dut.sum.value))


@cocotb.test()
async def test_CLA32_randomise(dut):
    """Test for adding two random numbers multiple times"""

    for i in range(5):

        A = random.randint(0, 4294967295)
        B = random.randint(0, 4294967295)
        
        A = 0b1100100011001010
        B = 0b1100100011001010
        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
        assert dut.sum.value == A + B , "Randomised test failed with: {A} + {B} != {SUM}".format(
        A=dut.a.value, B=dut.b.value, SUM=dut.sum.value)
        
  
```

# Results 

## cocotb tests created for 32 bit CLA failed due to error which could not be rectified within time limit. So, it was a unsuccessful attempt for Level 3 design 

## Attahcing the error message the terminal: 

```
0.00ns INFO     Found test test_CLA32.test_CLA32_Basic
     0.00ns INFO     Found test test_CLA32.test_CLA32_randomise
     0.00ns INFO     running test_CLA32_Basic (1/2)
     0.00ns INFO     A|B||cout|sum
     2.00ns INFO     test_CLA32_Basic failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-inderjit303/level3_design/test_CLA32.py", line 20, in test_CLA32_Basic
                         assert dut.sum.value == A + B, "Adder result is incorrect: {A} + {B} != {SUM}".format(
                       File "/workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb/binary.py", line 501, in __eq__
                         return self.value == other
                       File "/workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb/binary.py", line 345, in value
                         return self.integer
                       File "/workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb/binary.py", line 336, in integer
                         return self._convert_from(self._str)
                       File "/workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb/binary.py", line 231, in _convert_from_unsigned
                         return int(x.translate(_resolve_table), 2)
                       File "/workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb/binary.py", line 77, in __missing__
                         return self.resolve_x(key)
                       File "/workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb/binary.py", line 59, in resolve_error
                         raise ValueError("Unresolvable bit in binary string: '{}'".format(chr(key)))
                     ValueError: Unresolvable bit in binary string: 'x'
     2.00ns INFO     running test_CLA32_randomise (2/2)
     4.00ns INFO     test_CLA32_randomise failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-inderjit303/level3_design/test_CLA32.py", line 40, in test_CLA32_randomise
                         dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
                       File "/workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb/binary.py", line 509, in __int__
                         return self.integer
                       File "/workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb/binary.py", line 336, in integer
                         return self._convert_from(self._str)
                       File "/workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb/binary.py", line 231, in _convert_from_unsigned
                         return int(x.translate(_resolve_table), 2)
                       File "/workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb/binary.py", line 77, in __missing__
                         return self.resolve_x(key)
                       File "/workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb/binary.py", line 59, in resolve_error
                         raise ValueError("Unresolvable bit in binary string: '{}'".format(chr(key)))
                     ValueError: Unresolvable bit in binary string: 'x'
     4.00ns INFO     *****************************************************************************************
                     ** TEST                             STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     *****************************************************************************************
                     ** test_CLA32.test_CLA32_Basic       FAIL           2.00           0.01        267.77  **
                     ** test_CLA32.test_CLA32_randomise   FAIL           2.00           0.00       1113.10  **
                     *****************************************************************************************
                     ** TESTS=2 PASS=0 FAIL=2 SKIP=0                     4.00           0.02        234.98  **
                     ****************************************************************************************

```


