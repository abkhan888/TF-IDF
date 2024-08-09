TF-IDF (Term Frequency-Inverse Document Frequency)
TF-IDF is a statistical measure used to evaluate the importance of a word in a document relative to a collection of documents (corpus). It is widely used in text mining and information retrieval to identify words that carry significant meaning. TF-IDF combines two metrics:

Term Frequency (TF):

Definition: Measures how frequently a term appears in a document.
Formula:
TF
(
𝑡
,
𝑑
)
=
Number of times term 
𝑡
 appears in document 
𝑑
Total number of terms in document 
𝑑
TF(t,d)= 
Total number of terms in document d
Number of times term t appears in document d
​
 
Purpose: Highlights the importance of a term within a specific document.
Inverse Document Frequency (IDF):

Definition: Measures how important a term is across the entire corpus.
Formula:
IDF
(
𝑡
,
𝐷
)
=
log
⁡
(
Total number of documents
Number of documents containing term 
𝑡
)
IDF(t,D)=log( 
Number of documents containing term t
Total number of documents
​
 )
 
Purpose: Downscales terms that appear in many documents, reducing their influence on the analysis.
TF-IDF Score:

Formula:
TF-IDF
(
𝑡
,
𝑑
,
𝐷
)
=
TF
(
𝑡
,
𝑑
)
×
IDF
(
𝑡
,
𝐷
)

TF-IDF(t,d,D)=TF(t,d)×IDF(t,D)

Purpose: Provides a composite score that highlights important terms that are frequent in a document but not common across the corpus.
