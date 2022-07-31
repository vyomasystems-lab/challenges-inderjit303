# challenges-inderjit303
challenges-inderjit303 created by GitHub Classroom

# Level 1 Design 1 (Mux Design Verification)

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Gitpod id is included in the screenshot shown below*

![l1d1_image1](https://user-images.githubusercontent.com/99788755/182015934-d71a6af6-e681-4be8-ba86-7d8c379be922.png)


## Verification Environment (Level 1 Design 1)

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 5-bit select input *sel*, 2-bits inputs *inp0* to *inp30* and it gives 1-bit output *out*.

A cocotb Testbench is created for each individual inputs *inpo* to inp30*. 
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


The following error is seen:
```
assert dut.sum.value == A+B, "Adder result is incorrect: {A} + {B} != {SUM}, expected value={EXP}".format(
                     AssertionError: Adder result is incorrect: 7 + 5 != 2, expected value=12
```
## Test Scenario **(Important)**
- Test Inputs: a=7 b=5
- Expected Output: sum=12
- Observed Output in the DUT dut.sum=2

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 always @(a or b) 
  begin
    sum = a - b;             ====> BUG
  end
```
For the adder design, the logic should be ``a + b`` instead of ``a - b`` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://i.imgur.com/5XbL1ZH.png)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?
