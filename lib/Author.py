from Article import Article

class Author:
    def __init__(self, name):
        self._name = name
        self._written_articles = []
   
    def name(self):
        return self._name
    
    def articles(self):
        return self._written_articles
    
    def magazines(self):
        unique_magazines_for_author = set(article.magazine() for article in self._written_articles)
        return list(unique_magazines_for_author)

    def add_new_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._written_articles.append(new_article)
        return new_article
    
    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        magazine.add_contributor(self)
        return new_article

    def topic_areas(self):
        return list(set(magazine.category() for magazine in self.magazines()))