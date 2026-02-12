__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 2, Exercise 3

Search the internet for free VHDL development software suites that include a simulator. Get one of these suites, set it up, and build any simple demo projects that come with the suite to ensure it is working properly.

# Answer
Some freely available VHDL development suites are listed here:
1.	Xilinx Vivado Design Suite is available at https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado.html.
2.	Intel® Quartus® Prime Software Lite Edition is available at https://www.intel.com/content/www/us/en/collections/products/fpga/software/downloads.html.
3.	The open source GHDL simulator for VHDL is available at https://github.com/ghdl/ghdl.
4.	Electronic Design Automation (EDA) Playground is available at https://www.edaplayground.com.

**Vivado Design Suite** will be used for the examples in this chapter and in following chapters, including creating circuit designs for a low-cost FPGA development board. The following steps describe the installation and setup process for Vivado Design Suite on Windows.

We will be using an older version of Vivado because it is compatible with projects we will work with later. Using a more recent Vivado version would entail a somewhat complex project upgrade process that is not relevant for our purposes.

1.	Download _Vivado Design Suite - HLx Editions - 2020.1  Full Product_ Installation from https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive.html. During this process, you will need to create a Xilinx account if you do not already have one. Save your account username and password for later use. Verify the downloaded file name is **Xilinx_Unified_2020.1_0602_1208.tar.gz**.
2.	Extract the downloaded file. Move into the top-level directory and run **xsetup.exe**.
3.	You will be asked to accept the license agreements. Check the boxes and click **Next**.
4.	Select the **Vitis** tool suite and click **Next**.
5.	Ensure the **7 Series** option is checked in the **Devices** list. Accept the remaining default options and click **Next**.
6.	Accept the default installation directory and other options. You may need to create the _C:\Xilinx_ directory if it does not exist. Click **Next**.
7.	On the **Installation Summary** page, click **Install**. The installation will take some time. 
 
Perform these steps to build an example project:

1. Locate the **vivado.bat** file and run it to start Vivado. The default location is _C:\Xilinx\2020.1\Vivado\bin_. You may want to create a shortcut to this file on your desktop if the installer did not do so.
2.	In the Vivado main window, click **Open Example Project**.
3.	Click through to the **Select Project Template** dialog and select **CPU (HDL)**.
4.	Click through and accept the defaults on the following dialogs, then click **Finish** to create the project.
5.	On the **Project Manager** page, you’ll find the **Sources** panel. Expand the tree listing and double-click some of the files to open them in the editor. Most of the files in this design are in the Verilog hardware design language.
6.	Click **Run Synthesis** in the **Project Manager** panel, then click **OK** in the **Launch Run**s dialog. The **Design Runs** panel at the bottom will update the status as synthesis proceeds. This may take several minutes.
7.	After synthesis finishes, a dialog will appear offering to run the implementation. Click **Cancel**.
8.	Click **Run Simulation** in the Vivado main dialog **Project Manager** section, and then select **Run Behavioral Simulation**. Again, this may take several minutes.

> ⚠️ _If you experience problems running the simulation, it may be necessary to exclude your project directory from antivirus scanning._

9.	After the simulation completes, you will see a timing diagram in the **Simulation** window showing simulated CPU signals in response to the input data provided by the simulation source files. Rescale the window and examine the timing traces of the signals, starting from the beginning of the data.
10.	This completes the exercise. You may close Vivado.
