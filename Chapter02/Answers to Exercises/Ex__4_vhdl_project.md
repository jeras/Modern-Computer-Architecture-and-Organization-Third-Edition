__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 2, Exercise 4

Using your VHDL tool set, implement the 4-bit adder using the code listings presented in the chapter.

# Answer
Follow these steps to implement the 4-bit adder:

1.	Install the board files for the CMOD A7-35T device:

    * Install Git if you don't have it. Windows users: Install from https://git-scm.com/downloads/win  
    * In a command window, execute the command: `git clone https://github.com/Digilent/vivado-boards.git`  
    * Change to the _vivado_boards_ directory, then select version 1.1 of the Cmod board file with the command: `git checkout bc3730c`  
    * Copy all the files from _.vivado-boards\new\board_files_ to _C:\Xilinx\Vivado\2020.1\data\boards\board_files_. In Windows, change to the _board_files_ directory and execute the command `xcopy/s * \Xilinx\Vivado\2020.1\data\boards\board_files`.

2.  Start the Vivado application.
3.	Click **Create Project** in the Vivado main dialog.
4.	Click through and accept the default project name and location.
5.	Select **RTL Project**, the default project type.
6.	In the **Add Sources** dialog, select VHDL as both the Target Language and Simulator Language. Click **Add Files** and add [Ex__4_fulladder.vhdl](Code%20Files/Ex__4_fulladder.vhdl) and [Ex__4_adder4.vhdl](Code%20Files/Ex__4_adder4.vhdl) from _Chapter 2_ files, and click **OK**, then click **Next**.
7.	On the **Add Constraints** dialog, click **Next**.
8.	On the **Default Part** page, select the **Boards** tab. Type `Cmod` in the search field and choose **Cmod A7-35t**. If no results appear when searching, the board package was not installed. Repeat step 1 to ensure it is correctly installed.
9.	Click **Finish** to create the project.
10.	Expand the tree in the **Sources** window in the **Project Manager** dialog and locate the two files you added. Double-click each of them and expand the source code window to view the code.
11.	Click **Run Synthesis** in the **Project Manager** panel. Leave the options in the **Launch Runs** dialog at their defaults and click **OK**. The **Design Runs** panel will update the status as synthesis proceeds.
12.	Wait for synthesis to complete, then select **View Reports** in the **Synthesis Completed** dialog. Double-click each of the reports produced during the synthesis process. Only reports with a green dot on the icon will be available.
13.	This completes the exercise. You may close Vivado.
