**Background:**

This is a python script that converts the study drug name (eg, SB206) to molecular name (eg, Berdazimer sodium) leverage Adisinsight online query and the Beautiful Soup library. The input list can be in csv format and the output will be returned in csv format as well. If the searched name is not on the Adisinsight database, it output will be returned as the original study drug name.

**How it works:**

1. The script will search up the input

![](RackMultipart20221003-1-efzmba_html_8f25704c3642c6fa.png)

1. Then scrape the molecule name from the search result page.

![](RackMultipart20221003-1-efzmba_html_5ae0db41c8194863.png)

1. The output list can be easily inserted back into excel rows without changes to the format.

![](RackMultipart20221003-1-efzmba_html_426e2988be2bd8d0.png)

**Installation instruction:**

1. Download adisinsight.py file
2. Download Visual Studio Code
3. Open adisinsight.py file using VS Code
4. Open the terminal
5. Install dependencies by typing the following line in the terminal. Press enter after each line.

![](RackMultipart20221003-1-efzmba_html_8f386ed7a18dd586.gif)

**How to open the scraper:**

1. Copy and paste the input column from Excel.
2. Use text editor like to change the input into the following format. I used Sublime Editor to do this.

**Input format:**

- The input needs to be inserted into the array as strings under the following format:

![](RackMultipart20221003-1-efzmba_html_234663375153f180.gif)

1. Input the formatted list in between scrape (["x",]) located in line 62 of the code

![](RackMultipart20221003-1-efzmba_html_7c38b008bd330820.png)

1. Click on the run button located on the top right corner. ![Shape1](RackMultipart20221003-1-efzmba_html_8d5bc4e88a5f90f.gif)
2. ![](RackMultipart20221003-1-efzmba_html_b9f2498958778608.png)
3. The output will be shown in the terminal

![](RackMultipart20221003-1-efzmba_html_66bce5748153d81.png)

1. Copy and paste the output back onto your Excel spreadsheet.

![](RackMultipart20221003-1-efzmba_html_53dbaef4b47ab4d6.png)
