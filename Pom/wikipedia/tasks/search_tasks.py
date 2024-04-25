from wikipedia.actions.homepage_actions import HomepageActions
from wikipedia.actions.article_actions import ArticleActions

class SearchTasks:
    def __init__(self, page):
        self.homepage_actions = HomepageActions(page)
        self.article_actions = ArticleActions(page)

    async def perform_initial_search(self, term):
        await self.homepage_actions.open_homepage()
        await self.homepage_actions.submit_search(term)

    async def fill_article_search(self, term):
        await self.article_actions.fill_search(term)
