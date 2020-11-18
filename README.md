# *The CIHC Dictionary*

DESCRIPTION
*A user-adjustable online dictionary for the Chinese Indonesian Heritage Center*

CREATOR
*Mariska Snijdewind*

TABLE OF CONTENTS
1. About CIHC
2. Development Goals
3. Technical Accomplishments
4. Dictionary Experience
5. Process
6. Wishlist

## 1. About CIHC

The Chinese Indonesian Heritage Center focuses on maintaining the heritage Chinese Indonesian culture in the Netherlands, with a strong focus on those who migrated to the Netherlands in the 20th century.

One of their objectives is to inform their target audience on how the Chinese community lived in the Dutch East Indies, now known as Indonesia. Many Chinese, Indonesian or hybrid words that are used, don’t have a true counterpart in Dutch or English. In order for them to easily clarify these words for their readers, I decided to make a dictionary of the exotic words used on the website.

## 2. Development Goals

The main goal was to complete a project that fuses everything I’ve been learning together and create a standalone product using the CRUD operations making use of MongoDB, HTML, CSS, Javascript and Python.

## 3. Technical Accomplishments
Front-end uses HTML5, CSS3, Materialize as an addition to the css including the given icons. The backend uses Python3 with Flask and JavaScript. Additional dependencies are written in the *requirements.txt*.

## 4. Dictionary Experience
The website starts off with an overview of all words currently in the database, with a handy search bar at the top of the screen. The menu in the word card allows you to perform the following actions:
* Edit the word
* Delete the word
* Read the article the word is used in

In addition to the funtionalities above the top menu can be used to access the add (word) function.

The add word page includes imput fields for the word, word language, translation, translation language, meaning and the url of the article.

## 5. Process

Intially the idea was to have different pages for editing, deleting and adding words. However during the development phase this seemed more convoluted than neccessary, in hindsight i did add it to the wishlist. All steps were written down on paper and thus less accessable than when doing it digitally [Link to wireframe photo](https://photos.app.goo.gl/kREX3ry4ZTXTuVox6)

There were some issues with the validation function, however this funtion was deleted and placed on the wishlist. In addition earlier versions took the green and grey color scheme of the current CIHC website, however after contemplation it was decided that a fabric background would suit the company distionary better.

With regards to further issues. With handing in the project I accidentaly deleted the Heroku app, which caused other issues. One of this was updating flask etc. This issue is not yet resolved. And the app is thus not runnable on Heroku.

The app is tested by trying all funtionailities and checking this with the database. 

The website is however tested using Lighthouse:

Performance | Accessibility | Best Practices | SEO 
-- | -- | -- | --
93 | 82 | 100 | 91

## 6. Wishlist
The dictionary has all the required features, but for future updates I’d like to research and implement the following as well.

* User dependent functionalities (as delete and edit)
* Adding images loaded from the wedsite / refered page
* Alphabetical order of words
* Add creation and update timestamp

/* */

