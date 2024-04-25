import sys
import os

script_dir = os.path.dirname(__file__)  # Gets the directory where the script is located
base_dir = os.path.join(script_dir, '..')  # Adjusts the path to include the base directory
sys.path.append(os.path.normpath(base_dir))  # Normalizes and appends the path to sys.path

import asyncio
from playwright.async_api import async_playwright
from wikipedia.tasks.search_tasks import SearchTasks
from wikipedia.tasks.navigation_tasks import NavigationTasks

async def run_wikipedia_test(playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=2000)
    context = await browser.new_context()
    page = await context.new_page()

    search_tasks = SearchTasks(page)
    navigation_tasks = NavigationTasks(page)

    await search_tasks.perform_initial_search("dogs")
    await search_tasks.fill_article_search("dog")  # Fill without submitting
    await navigation_tasks.navigate_to_article("Dogs in warfare Overview of")  # Click the link directly

    await context.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run_wikipedia_test(playwright)

asyncio.run(main())
