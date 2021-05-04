# Remesh-Visualization-Challenge

Hi there,

Thanks for giving me a chance to solve this visualization challenge. I will be giving detailed setup instructions and description of what my application does. I used Dash Plotly to develop the visualizations, pandas for data manipulation, numpy for some math. 

**Setup:**

1. I had written the code in PyCharm IDE. So I have a .py file attached to this repository. 
2. I also have a requirements.txt file in the same folder as the .py file to easily install all the requirements.
3. I have created a local copy of the JSON data for convenience and I am attaching that too.
4. Open the .py in any Python IDE, install the requirements and run the code.
5. Before running the code, Please make sure you have a copy of the JSON data locally as I had issues opening the file from the given link in the description of this challenge. 
6. Also, Please make sure to update the path to that file at line number 20 in the code. 
7. After running the file in the IDE, you will be given an end point with port 8000. Click on it to open the Dash application and an interactive visualization. 

**After running the .py file**
1. Once the Dash application opens on your browser, enter a starting and ending range by which the graph will the updated. To get a high level view, endter start as 0 and end as 300. I used 300 as maximum because the length of the longest tweet is 288. This number can vary but I have considered this variable based on the data I have.
2. The xaxis of the graph shows the length of the tweets and y axis shows the corresponding number of likes and hashtags respectively in the subplots. 

**Insights drawn from the visualizations:**
1. A very important question I was asked in the prompt was how do I define user engagement? 
My answer after playing with the data and giving it a thought is the number of likes a tweet gets defines user engagement as it shows if a user is interested in a given tweet or not.
2. If you drill deeper into the bar charts by changes the ranges, it can be inferred that there is a direct relationship between the number of likes and the number of hashtags used. 
3. Another insight that can be drawn is people prefer tweets which are neither too short nor too long. By looking at the chart, the tweets with length less than 20 and more than 110 lose charm and people are unlikely to react to these tweets. 
4. Another observation is users dont prefer long tweets even when a large number of hashtags are used. The ideal tweet length to get maximum user engagement is 40 to 80. 
5. Finally, I want to stress upon the most important insight drawn, tweet length defines likes and user engagement. 

**Some final words***
I tried my best to come up with an effective solution that looks good and performs well. 
I am confident that I have satisfied the given application and technical requirements and supported my thoughts with proof led and proven insights. I am also sure that I would get constructive feedback from you if you decide to move ahead with me or otherwise. 


Have a great day and rest of the week.

Thanks,
Ramya.
