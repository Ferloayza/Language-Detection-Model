# Language-Detection-Model

## About the project

This project tries to break the language barriers in the world by building a language detection model. Utilizing a public Kaggle dataset, consisting of text samples in various languages and the Multinomial Naive Bayes algorithm. I decided to train a model to identify text languages.

## Data Used

The data used in this project was obtained from a public Kaggle dataset. There are various texts in 17 different languages.

This data was also cleaned, punctuation marks were eliminated, because the model might conclude these marks are distinctive features of a certain languages. 

The preprocessing consisted in labeling the languages, and vectorizing the texts.

## Multinomial Naive Bayes 

This project utilizes MNB for language detection due to its strengths in handling large text datasets. MNB excels at analyzing the likelihood of individual words appearing in a specific language. This is useful when the word order might be less important than the presence of specific words.

## RESULTS 

This model detects the language in a text and I also added "googletrans" library so it also outputs the translation

Phrase: "Hola, esta es una prueba"
Output: The predicted language is: ['Spanish'] and it says (Hello, this is a test)

Phrase: "Hallo, das ist ein test"
Output: The predicted language is: ['German'] and it says (Hello, this is a test)

Phrase: "Привет, это тест"
Output: The predicted language is: ['Russian'] and it says (Hello, this is a test)

Phrase: "Γεια σας αυτό είναι ένα τεστ"
Output: The predicted language is: ['Greek'] and it says (Hello this is a test)

## TO-DO

The base for the language detection is settled and works fine, the goal is to create a model capable of detecting a sentence in any language in a picture and translate what it says to your native language. This is useful when traveling, because you just can't Ctrl+C the text. 
