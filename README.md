**Background:**

This is a python script that converts the study drug name (eg, SB206) to molecular name (eg, Berdazimer sodium) leverage Adisinsight online query and the Beautiful Soup library. The input list can be in csv format and the output will be returned in csv format as well. If the searched name is not on the Adisinsight database, it output will be returned as the original study drug name.

**How it works:**

1. The script will search up the input

![Pic1](https://user-images.githubusercontent.com/112147745/193520137-820f30e8-8180-4dbb-b5e1-77b14ce7051b.png)

2. Then scrape the molecule name from the search result page.

![Picture2](https://user-images.githubusercontent.com/112147745/193520398-df9de114-674d-4770-a8f9-616608d7456b.png)

3. The output list can be easily inserted back into excel rows without changes to the format.

![Picture3](https://user-images.githubusercontent.com/112147745/193520410-e480d1bb-5724-4161-843c-4101d63fdf96.png)

**Installation instruction:**

1. Download adisinsight.py file
2. Download Visual Studio Code
3. Open adisinsight.py file using VS Code
4. Open the terminal
5. Install dependencies by typing the following line in the terminal. Press enter after each line.

```python
pip install requests
pip install BeautifulSoup
pip install json
pip install csv
```
**How to open the scraper:**

1. Copy and paste the input column from Excel.
2. Use text editor like to change the input into the following format. I used Sublime Editor to do this.

**Input format:**

- The input needs to be inserted into the array as strings under the following format:
```python
scrape ([“x1”,
“x2”,
“x3”,
“…”,
“x”,])
```

1. Input the formatted list in between scrape (["x",]) located in line 62 of the code

![Picture6](https://user-images.githubusercontent.com/112147745/193520425-1adcffa0-ed46-4b7b-880f-0fa4e0960a33.png)

2. Click on the run button located on the top right corner.

![Picture5](https://user-images.githubusercontent.com/112147745/193520423-673cefa0-c1e7-4feb-b752-6ee162938b98.png)

3. The output will be shown in the terminal

![Picture8](https://user-images.githubusercontent.com/112147745/193520436-cf9474a4-c7e4-429d-83b4-5767c99563c8.png)

1. Copy and paste the output back onto your Excel spreadsheet.

![Picture3](https://user-images.githubusercontent.com/112147745/193520410-e480d1bb-5724-4161-843c-4101d63fdf96.png)
