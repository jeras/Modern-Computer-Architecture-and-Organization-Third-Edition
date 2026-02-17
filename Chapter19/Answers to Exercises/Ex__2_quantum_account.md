__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 19, Exercise 2

Create a free IBM Quantum account at https://quantum.cloud.ibm.com/. Create an IBM Quantum API key from that page and install it into your local environment using the instructions at https://quantum.cloud.ibm.com/docs/en/guides/save-credentials. Create a free Qiskit Runtime Instance at https://quantum.cloud.ibm.com/instances.

# Answer
1.	Visit https://quantum.cloud.ibm.com/. If you don’t already have an account, click the **Create an IBMid account** link to get started.
2.	Once you are logged in, locate **API key** on the screen. Create an API key, then save a copy of the key string on your computer.
3.	Enter the following commands at a command prompt to install your API token. Replace `MY_TOKEN` with the key string you copied in step 2:
```
C:\>python
from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(token='MY_TOKEN')
```
4.	Visit https://quantum.cloud.ibm.com/instances and select **Create Instance**. Choose the **Open (free) plan** and name your instance _free-quantum_.
