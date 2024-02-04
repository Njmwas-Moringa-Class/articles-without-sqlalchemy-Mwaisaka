from lib.Article import Article

class Magazine:
    all_magazines = []
    def __init__(self,name,category):
        self._name = name
        self._category = category
        self._contributors = [] # list of contributors
        Magazine.all_magazines.append(self)
        
    def name(self): 
        return self._name
    
    def category(self):
        return self._category
    
    def contributors(self):
        return self._contributors
    
    def add_contributors(self, author):
        self._contributors.append(author)
    
    @classmethod
    def all(cls):
        return cls.all_magazines
    
    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.all_magazines:
            if magazine.name() == name:
                return magazine
        return None

    @classmethod
    def article_titles(cls, magazine):
        return [article.title() for article in Article.all() if article.magazine() == magazine]

    @classmethod
    def contributing_authors(cls, magazine):
        authors_count = {}
        for article in Article.all():
            if article.magazine() == magazine:
                author = article.author()
                if author in authors_count:
                    authors_count[author] += 1
                else:
                    authors_count[author] = 1

        return [author for author, count in authors_count.items() if count > 2]