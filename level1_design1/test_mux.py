# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    #inputs initial value
    inp0 = 0
    inp1 = 1
    inp2 = 2
    inp3 = 3
    inp4 = 0
    inp5 = 1
    inp6 = 2
    inp7 = 3
    inp8 = 0
    inp9 = 1
    inp10 = 2
    inp11 = 3
    inp12 = 0
    inp13 = 1
    inp14 = 2
    inp15 = 3
    inp16 = 0
    inp17 = 1
    inp18 = 2
    inp19 = 3
    inp20 = 0
    inp21 = 1
    inp22 = 2
    inp23 = 3
    inp24 = 0
    inp25 = 1
    inp26 = 2
    inp27 = 3
    inp28 = 0
    inp29 = 1
    inp30 = 2
    
    #input driving
    dut.inp0.value = inp0
    dut.inp1.value = inp1
    dut.inp2.value = inp2
    dut.inp3.value = inp3
    dut.inp4.value = inp4
    dut.inp5.value = inp5
    dut.inp6.value = inp6
    dut.inp7.value = inp7
    dut.inp8.value = inp8
    dut.inp9.value = inp9
    dut.inp10.value = inp10
    dut.inp11.value = inp11
    dut.inp12.value = inp12
    dut.inp13.value = inp13
    dut.inp14.value = inp14
    dut.inp15.value = inp15
    dut.inp16.value = inp16
    dut.inp17.value = inp17
    dut.inp18.value = inp18
    dut.inp19.value = inp19
    dut.inp20.value = inp20
    dut.inp21.value = inp21
    dut.inp22.value = inp22
    dut.inp23.value = inp23
    dut.inp24.value = inp24
    dut.inp25.value = inp25
    dut.inp26.value = inp26
    dut.inp27.value = inp27
    dut.inp28.value = inp28
    dut.inp29.value = inp29
    dut.inp30.value = inp30
    
    sel = 0
    dut.sel.value = sel
     
    
    #select lines
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp0.value} Select={dut.sel.value}  model = {dut.inp0.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp0.value, "Test Failed for input"
    
    sel = 1
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp1.value} Select={dut.sel.value}  model = {dut.inp1.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp1.value, "Test Failed for input"

    sel = 2
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp2.value} Select={dut.sel.value}  model = {dut.inp2.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp2.value, "Test Failed for input"

    sel = 3
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp3.value} Select={dut.sel.value}  model = {dut.inp3.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp3.value, "Test Failed for input"

    sel = 4
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp4.value} Select={dut.sel.value}  model = {dut.inp4.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp4.value, "Test Failed for input"

    sel = 5
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp5.value} Select={dut.sel.value}  model = {dut.inp2.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp5.value, "Test Failed for input"

    sel = 6
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp6.value} Select={dut.sel.value}  model = {dut.inp6.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp6.value, "Test Failed for input"

    sel = 7
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp7.value} Select={dut.sel.value}  model = {dut.inp7.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp7.value, "Test Failed for input"

    sel = 8
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp8.value} Select={dut.sel.value}  model = {dut.inp8.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp8.value, "Test Failed for input"

    sel = 9
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp9.value} Select={dut.sel.value}  model = {dut.inp9.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp9.value, "Test Failed for input"

    sel = 10
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp10.value} Select={dut.sel.value}  model = {dut.inp10.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp10.value, "Test Failed for input"

    sel = 11
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp11.value} Select={dut.sel.value}  model = {dut.inp11.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp11.value, "Test Failed for input"

    sel = 12
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp12.value} Select={dut.sel.value}  model = {dut.inp12.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp12.value, "Test Failed for input"

    sel = 13
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp13.value} Select={dut.sel.value}  model = {dut.inp13.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp13.value, "Test Failed for input{dut.inp13.value}"

    sel = 14
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp14.value} Select={dut.sel.value}  model = {dut.inp14.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp14.value, "Test Failed for input {dut.inp14.value}"

    sel = 15
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp15.value} Select={dut.sel.value}  model = {dut.inp15.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp15.value, "Test Failed for input"

    sel = 16
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp16.value} Select={dut.sel.value}  model = {dut.inp16.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp16.value, "Test Failed for input"

    sel = 17
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp17.value} Select={dut.sel.value}  model = {dut.inp17.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp17.value, "Test Failed for input"

    sel = 18
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp18.value} Select={dut.sel.value}  model = {dut.inp18.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp18.value, "Test Failed for input"

    sel = 19
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp19.value} Select={dut.sel.value}  model = {dut.inp19.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp19.value, "Test Failed for input"

    sel = 20
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp20.value} Select={dut.sel.value}  model = {dut.inp20.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp20.value, "Test Failed for input"

    sel = 21
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp21.value} Select={dut.sel.value}  model = {dut.inp21.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp21.value, "Test Failed for input"

    sel = 22
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp22.value} Select={dut.sel.value}  model = {dut.inp22.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp22.value, "Test Failed for input"

    sel = 23
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp23.value} Select={dut.sel.value}  model = {dut.inp23.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp23.value, "Test Failed for input"

    sel = 24
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp24.value} Select={dut.sel.value}  model = {dut.inp24.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp24.value, "Test Failed for input"

    sel = 25
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp25.value} Select={dut.sel.value}  model = {dut.inp25.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp25.value, "Test Failed for input"

    sel = 26
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp26.value} Select={dut.sel.value}  model = {dut.inp26.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp26.value, "Test Failed for input"

    sel = 27
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp27.value} Select={dut.sel.value}  model = {dut.inp27.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp27.value, "Test Failed for input"

    sel = 28
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp28.value} Select={dut.sel.value}  model = {dut.inp28.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp28.value, "Test Failed for input"

    sel = 29
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp29.value} Select={dut.sel.value}  model = {dut.inp29.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp29.value, "Test Failed for input"

    sel = 30
    dut.sel.value = sel
    await Timer(2,units='ns')
    out = dut.out.value
    dut._log.info(f'Input = {dut.inp30.value} Select={dut.sel.value}  model = {dut.inp30.value}, DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp30.value, "Test Failed for input "

    cocotb.log.info('##### CTB: Develop your test here ########')

@cocotb.test()
async def test_mux_randomised(dut):
    """Test for mux2"""
    #inputs initial value
    inp0 = random.randint(0, 3)
    sel = random.randint(0, 30)
    #input driving
    dut.inp0.value = inp0
    dut.sel.value = sel
    #select lines
    await Timer(2,units='ns')
    #out = dut.out.value
    #dut._log.info(f'Select = {sel:02}, output = {int(out)}')
    #dut._log.info(f'Input = {dut.inp13.value} Select={dut.sel.value}  model = {dut.inp13.value}, DUT={int(dut.out.value)}')
    #assert dut.out.value == dut.inp13.value, "Randomised Test Failed"
    for i in range(0,31,1):
       sel1 = i
       dut.sel.value = sel1
       await Timer(2, units='ns')
       out = dut.out.value
       #dut._log.info(f'Select = {sel:02}, inputs = {"inp%s" %i=:2}')
       dut._log.info(f'Select = {sel:02}, inputs = {"inp%d"%i:2}, output = {int(out)}')
        #dut._log.info(f'Select = {sel:02}, inputs = {inp0}, output = {int(out)}')
       assert dut.out.value == dut.inp0.value,  "output was incorrect" 
        


    cocotb.log.info('##### CTB: Develop your test here ########')