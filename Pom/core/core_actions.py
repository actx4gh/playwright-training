class CoreActions:
    def __init__(self, page):
        self.page = page

    async def navigate_to_url(self, url):
        await self.page.goto(url)

    async def click(self, selector):
        await self.page.click(selector)

    async def fill(self, selector, text):
        await self.page.fill(selector, text)

    async def press_enter(self, selector):
        await self.page.press(selector, "Enter")

    async def click_by_role(self, name):
        await self.page.get_by_role("link", name=name).click()
