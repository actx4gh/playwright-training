from wikipedia.actions.article_actions import ArticleActions

class NavigationTasks:
    def __init__(self, page):
        self.article_actions = ArticleActions(page)

    async def navigate_to_article(self, article_name):
        await self.article_actions.select_link_by_name(article_name)
