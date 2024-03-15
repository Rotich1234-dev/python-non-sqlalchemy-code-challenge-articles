
class Article:
    all = []  # Class variable to store all instances of articles

    def __init__(self, author, magazine, title):
        # Validate input parameters
        if not isinstance(author, Author) or not isinstance(magazine, Magazine) or not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Invalid author, magazine, or title")

        self.author = author
        self.magazine = magazine
        self._title = title  # Private attribute for the article title
        Article.all.append(self)  # Add the article to the list of all articles

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        # Setter for the title property with validation
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Invalid title")
        self._title = title



class Magazine:
    all = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be of type str and between 2 and 16 characters")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be of type str and more than 0 characters")

    def articles(self):
        # Retrieve all articles associated with this magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Retrieve all unique contributors (authors) for this magazine
        return list({article.author for article in self.articles()})

    def article_titles(self):
        # Retrieve titles of all articles associated with this magazine
        if self.articles():
            return [article.title for article in self.articles()]
        else:
            return None

    def contributing_authors(self):
        # Retrieve authors who contributed to more than 2 articles for this magazine
        author_article_count = {}
        for article in self.articles():
            if isinstance(article.author, Author):
                if article.author in author_article_count:
                    author_article_count[article.author] += 1
                else:
                    author_article_count[article.author] = 1
        contributing_article_authors = [author for author, count in author_article_count.items() if count > 2]        
        
        if contributing_article_authors:
            return contributing_article_authors
        else:
            return None
    
    @classmethod
    def top_publisher(cls):
        # Find the magazine with the most articles (top publisher)
        magazines_with_articles = [magazine for magazine in cls.all if magazine.articles()]
        
        if magazines_with_articles:
            return max(magazines_with_articles, key=lambda magazine: len(magazine.articles()))
        else:
            return None

class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        # Sets the author's name with validation
        if isinstance(name, str) and name != "" and not hasattr(self, 'name'):
            self._name = name
        else:
            raise ValueError("Name must be of type str and must not be empty")

    def articles(self):
        # this function retrieves all articles written by this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Retrieve all magazines the author has contributed to
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        # Add a new article authored by this author
        return Article(self, magazine, title)

    def add_magazine(self, magazine):
        # Adds a magazine to the author's list of contributions
        return [self, magazine]

    def topic_areas(self):
        # Retrieves unique topic areas covered by articles written by this author
        if self.articles():
            return list(set(article.magazine.category for article in self.articles()))
        else:
            return None 
