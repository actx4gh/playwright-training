from core.core_actions import CoreActions

class ArticleActions(CoreActions):
    def __init__(self, page):
        super().__init__(page)

    async def fill_search(self, term):
        # Use a CSS selector to target the input based on its placeholder attribute
        await self.fill("input[placeholder='Search Wikipedia']", term)

    async def select_link_by_name(self, link_name):
        # Use role selector instead of text selector
        await self.click_by_role(link_name)
