__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 2, Exercise 5

Add test driver code to your 4-bit adder to drive it through a range of input combinations to confirm the circuit is operating correctly.

# Answer
Follow these steps to test the 4-bit adder project created in [Exercise 4](Ex__4_vhdl_project.md):

1.	Double-click the **Vivado 2020.1** icon to start Vivado.
2.	Click **Open Project** in the Vivado main dialog and open the project you created in [Exercise 4](Ex__4_vhdl_project.md).
3.	Click **Add Sources** in the **Project Manager** panel, select **Add or create simulation sources**, add [Ex__5_adder4_testbench.vhdl](Code%20Files/Ex__5_adder4_testbench.vhdl), and then click **Finish**.
4.	Expand the tree in the **Simulation Sources** window in the **Project Manager** dialog and locate the file you added. Double-click the file and expand the source code window to view the code. Observe the six test cases present in the code.
5.	Click **Run Simulation** in the Vivado main dialog **Project Manager** section, then select **Run behavioral simulation**.
6.	Wait for the simulation to complete, then expand the window with the timing diagram (which is likely labeled **Untitled 1**).
7.	Use the magnifying glass icons and the window’s horizontal scroll bar to view the six test cases during the first 60 ns of execution. Determine whether the sum and carry for each addition operation are correct. You can drag the yellow marker to update the numerical information in the **Value** column.
8.	This completes the exercise. You may close Vivado.
