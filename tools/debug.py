#!/usr/bin/env python3

import sys
sys.path.append('lib') 

import ipdb;

from lib.Article import Article
from lib.Author import Author
from lib.Magazine import Magazine


if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###

    # Create Authors
    author1 = Author("Frank Mwaisaka")
    author2 = Author("Ben Leonards")

    # Insert a breakpoint here to interact with the terminal
    ipdb.set_trace()
    
    # Create Magazines
    magazine1 = Magazine("The Origin of Species", "History")
    magazine2 = Magazine("The internet of things", "Technology")

    # Insert a breakpoint here to interact with the terminal
    ipdb.set_trace()

    #Author adds a new article to a magazine
    article1 = author1.add_article(magazine1, "Survival for the fittest")
    article2 = author1.add_article(magazine2, "Artificial intelligence")

#Test code

#Accessing articles and magazines for an Author
print("Author:", author1.name())
print("\nArticles by Author:")
for article in author1.articles():
    print("Article Title:", article.title(), "Magazine:", article.magazine().name())

print("\nMagazines contributed by Author:")
for magazine in author1.magazines():
    print("Magazine:", magazine.name(), "Category:", magazine.category())

#Accessing unique topic areas for an Author
print("\nTopic Areas for Author:")
print(author1.topic_areas())

#Find a magazine by name
found_magazine = Magazine.find_by_name("Magazine1")
if found_magazine:
    print("\nFound Magazine:", found_magazine.name(), "Category:", found_magazine.category())
else:
    print("\nMagazine not found.")
    
#Accessing article titles for a magazine
print("\nArticle Titles for Magazine1:")
print(Magazine.article_titles(magazine1))

#Accessing contributing authors for a magazine
contributing_authors = Magazine.contributing_authors(magazine1)
print("\nContributing Authors for Magazine1 (written more than 2 articles):")
for author in contributing_authors:
    print("Contributing Author:", author.name())   
    
# DO NOT REMOVE THIS
    ipdb.set_trace()
