__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 2, Exercise 6

Expand the test driver code and verify the 4-bit adder produces correct results for all possible combinations of inputs.

# Answer
Follow these steps to test the 4-bit adder project created in [Exercise 4](Ex__4_vhdl_project.md):

1.	Double-click the **Vivado 2020.1** icon to start Vivado.
2.	Click **Open Project** in the Vivado main dialog and open the project you created in [Exercise 4](Ex__4_vhdl_project.md) and modified in [Exercise 5](Ex__5_vhdl_test.md).
3.	Expand the tree in the **Simulation Sources** window in the **Project Manager** dialog and locate the module you added in [Exercise 5](Ex__5_vhdl_test.md) ([Ex__5_adder4_testbench.vhdl](Code%20Files/Ex__5_adder4_testbench.vhdl)). Right-click the module name, select **Remove File from Project**, and click **OK** to confirm the removal.
4.	Click **Add Sources** in the **Project Manage**r panel, select **Add or create simulation sources**, add [Ex__6_adder4_fulltestbench.vhdl](Code%20Files/Ex__6_adder4_fulltestbench.vhdl), and then click **Finish**.
5.	Expand the tree in the **Simulation Sources** window in the **Project Manager** dialog and locate the file you added. Double-click the file and expand the source code window to view the code. Observe the nested loop with 256 test cases.
6.	Click **Run Simulation** in the Vivado main dialog **Project Manager** section, and then select **Run behavioral simulation**.
7.	Wait for the simulation to complete, then expand the window with the timing diagram (probably labeled **Untitled 1**).
8.	Use the magnifying glass icons and the horizontal scroll bar to view the test cases. There is a problem: The run stops after 1,000 ns, which isn’t enough time for all the tests to execute.
9.	Right-click **Simulation** in the **Project Manager** panel and select **Simulation Settings...**.
10.	Select the **Simulation** tab and change the value for `xsim.simulate.runtime` to 3000 ns. Click **OK**.
11.	Click the **X** on the **Simulation** window to close the simulation.
12.	Re-run the simulation.
13.	After expanding and scaling the timing diagram, you will see all 256 test cases. Observe if the error signal is nonzero anywhere along the trace. A value of 1 would indicate the adder’s output did not match the expected output.
14.	This completes the exercise. You may close Vivado.
