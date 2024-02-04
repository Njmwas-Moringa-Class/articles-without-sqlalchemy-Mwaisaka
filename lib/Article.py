class Article:
    all_articles =[]
    def __init__(self, author,magazine,title):
        self._author = author
        self._magazine = magazine
        self._title=title
        Article.all_articles.append(self)
    
    def title(self):
        return self._title
    
    @classmethod
    def all(cls):
        return cls.all_articles
    
    def author(self):
        return self._author
    
    def magazine(self):
        return self._magazine