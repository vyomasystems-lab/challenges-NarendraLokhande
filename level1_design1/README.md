Mux Design Verification

Verification Environment

Test Scenario (Important)
Test Inputs: a=7 b=5
Expected Output: sum=12
Observed Output in the DUT dut.sum=2

Test Scenario (Important)

Output mismatches for the above inputs proving that there is a design bug
 always @(a or b) 
  begin
    sum = a - b;             ====> BUG
  end

  For the adder design, the logic should be a + b instead of a - b as in the design code.

  Design Fix