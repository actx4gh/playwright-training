from core.core_actions import CoreActions
from wikipedia.constants import WikipediaConstants

class HomepageActions(CoreActions):
    async def open_homepage(self):
        await self.navigate_to_url(WikipediaConstants.BASE_URL)

    async def submit_search(self, term):
        await self.fill("text='Search Wikipedia'", term)
        await self.press_enter("text='Search Wikipedia'")
