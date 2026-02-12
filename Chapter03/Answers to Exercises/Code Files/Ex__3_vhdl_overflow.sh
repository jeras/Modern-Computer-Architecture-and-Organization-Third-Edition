#!/bin/sh

# analyse VHDL source code
ghdl -a --std=08 \
  ../../Chapter\ Files/ALU.vhdl \
  ALU_testbench.vhdl

# elaborate top level entity
ghdl -e --std=08 ALU_TESTBENCH

# run testbench
ghdl -r --std=08 ALU_TESTBENCH --wave=ALU_testbench.ghw

# synthesize
yosys -m ghdl -p 'ghdl ALU.vhdl -e ALU; proc; opt; show'

# open waveform with GTKWave
#gtkwave ALU_testbench.ghw --save=ALU_testbench.gtkw
