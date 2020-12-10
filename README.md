# Canada's Response to Economic Impacts of COVID-19

Amanda Cheney  
Metis Final Project   
December 8, 2020    

**Motivation**  

After the COVID-19 pandemic first hit in March 2020, the Canadian government unveiled numerous temporary social security and financial aid programs. The most high profile of which is the Canadian Emergency Response Benefit (CERB), which provides $2,000 a month for up to seven months for qualifying residents facing unemployment due to the pandemic. Although the program was formally ended in October it has since been replaced by the Canadian Recovery Benefit (CRB), a nearly identical program extending benefits for six additional months. 

24% of the entire Canadian population applied for CERB. With nearly one in four people receiving this benefit, this program has clearly been popular, yet, at the same time, it has its shortcomings, and there has been vocal concern from some members of the public and conservative lawmakers that this program might be subject to fraud. Since public opinion, or at least our perception of public opinion, is increasingly shaped by social media, I wanted to take a look at what kind of conversations about these programs are happening on Twitter. 

**Objective**  

Unsupervised learning and natural language processing to identify two sets of clusters of Twitter conversations about the Canadian Emergency Response Benefit (CERB) and Canadian Recovery Benefit(CRB) programs to address unemployment and economic impacts of the COVID-19 pandemic. 

1. One that captures the contours of everyday user conversations. 

2.  Another that highlights clusters of conversation that are really, really dense, have users make collaborative efforts to shape public opinion and perception.  

**Data Sources** 

250,000 tweets from between March 1 and December 1, 2020 using Tweepy and snscrape – using my own domain knowledge to design my queries to exclude extraneous content.   

**Methods**  

Preprocessing using SpaCy.   

Transfer learning from [Godin (2019)](https://fredericgodin.com/research/twitter-word-embeddings/) Twitter embeddings library and FastText to create document embeddings.  

HDBSCAN to identify 5 dense, high level clusters and KMeans to identify 7 clusters of everyday conversations.

VADER sentiment analysis.  

**Key Findings**    

HDBSCAN originally produced 31 clusters, however, many of them were redundant – for instance a number of tabloid news conglomerates have botnets of dozens of local newspapers tweeting out identical content at the same time – which I condensed where possible to get down to 5 clusters, in ascending order:

1. Pandemic Outrage
2. Troll named FathersInCanada
3. News agency botnets and custom retweets of news content
4. Petition drives for expanding CERB programs to include people with disabilities and transitioning to Universal Basic Income
5. CERB applicants, recipients and defenders 

However, because of nature of HDBSCAN algorithm, 93% of tweets treated as noise. Yet given my aggressive filtering in my query, I felt confident that my data wasn’t *that* noisy. So I took this chuck of unclassified tweets and ran KMeans to identify 7 clusters of “every day” conversations. In order from largest to smallest:

1. Business interests vs public welfare  
2. CERB fraud and failures
3. Unequal economic impacts of COVID
4. CERB as wage subsidy
5. Financial problems
6. Program announcements
7. CERB extension   

**Takeaways**   

1. CERB has a lot of public support
2. Critiques reflect how indispensable the program is, focus on improving and expanding the program to cover more people.
3. Twitter conversations reflect Canada’s political culture.   

**Technologies Used**

- FastText 
- SpaCy
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Yellowbrick 
- Twitter API 
- snscrape 

**Skills Demonstrated**

- Natural Language Processing
- Transfer Learning
- Word Embeddings
- Document Embeddings 
- Unsupervised Learning
- Clustering
- Visualization 