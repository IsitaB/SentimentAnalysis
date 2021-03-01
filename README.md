# Sentiment Analysis: charlotte

## SVM 1

I started trying to using Natural Language Toolkit (NLTK) to normalize text and feed it into an svm, but I decided to move on to using BERT.

## SVM 2

Uses DistilBERT to classify sentences, which is then fed into an SVM to determine the sentiment.

BERT was limited by the number of tokens it can process at a time, so I had to use a dataset with short text samples. It should then be possible to classify arbitrary length text by splitting it up.

The dataset I used was had positive and negative labels, not specifically hateful and not hateful.
