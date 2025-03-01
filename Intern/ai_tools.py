import asyncio
from playwright.async_api import async_playwright
import csv
import time
import re

async def scrape_bestofai(max_cards=1000):
    """Scrape bestofai.com website for AI tools information"""
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Navigate to the website
        await page.goto('https://bestofai.com/')
        print("Website loaded successfully")

        # Handle potential pop-ups
        try:
            await page.click('button:has-text("Accept")', timeout=3000)
            print("Closed cookie consent")
        except:
            try:
                close_button = await page.wait_for_selector('button[aria-label="Close"]', timeout=3000)
                await close_button.click()
                print("Closed pop-up")
            except:
                print("No pop-up detected")

        # Wait for initial cards to load
        await page.wait_for_selector('a[data-discover="true"]')
        
        # Initialize variables to track progress
        all_cards_data = []
        processed_hrefs = set()  # Track cards we've already processed by their href
        
        # Continue loading and processing cards until we reach the desired count
        while len(all_cards_data) < max_cards:
            # First get all cards
            cards = await page.query_selector_all('a[data-discover="true"]')
            current_count = len(cards)
            print(f"Found {current_count} cards, processed {len(all_cards_data)} so far")
            
            # Process any new cards we haven't seen before
            for card in cards:
                try:
                    # Check if we've reached our target
                    if len(all_cards_data) >= max_cards:
                        break
                        
                    # Get href to use as unique identifier
                    href = await card.get_attribute('href')
                    if not href or href in processed_hrefs:
                        continue
                    
                    # Mark as processed
                    processed_hrefs.add(href)
                    
                    # Only process if it looks like an actual tool card (has a title)
                    title_elem = await card.query_selector('h3')
                    if not title_elem:
                        # Skip navigation links and non-tool cards
                        continue
                    
                    # Get the outer HTML of the card
                    outer_html = await card.evaluate('el => el.outerHTML')
                    
                    # Extract title
                    title_text = await title_elem.text_content()
                    
                    # Extract rating if available
                    rating_elem = await card.query_selector('div.flex.items-baseline.gap-2 strong')
                    rating = await rating_elem.text_content() if rating_elem else "No Rating"
                    
                    # Extract description
                    description_elem = await card.query_selector('p.my-6')
                    description = await description_elem.text_content() if description_elem else "No Description"
                    
                    # Extract tags/categories
                    tags_elements = await card.query_selector_all('button[type="button"] span.whitespace-nowrap')
                    tags = [await tag.text_content() for tag in tags_elements]
                    tags_text = ", ".join(tags)
                    
                    # Extract likes count
                    likes_elem = await card.query_selector('span.text-md.text-dark span')
                    likes_text = await likes_elem.text_content() if likes_elem else "0 likes"
                    # Clean up likes count
                    likes_count = re.search(r'(\+?\d+)', likes_text).group(1) if re.search(r'(\+?\d+)', likes_text) else "0"
                    
                    # Build full URL
                    url = "https://bestofai.com" + href if href.startswith('/') else href
                    
                    # Extract image URL if available
                    img_elem = await card.query_selector('img')
                    image_url = await img_elem.get_attribute('src') if img_elem else "No Image"
                    
                    # Featured tag
                    featured_elem = await card.query_selector('div.absolute.-top-3')
                    featured = "Yes" if featured_elem else "No"
                    
                    # Create card data dictionary
                    card_data = {
                        'title': title_text,
                        'rating': rating,
                        'description': description.strip(),
                        'tags': tags_text,
                        'likes': likes_count,
                        'url': url,
                        'image_url': image_url,
                        'featured': featured,
                        'outer_html': outer_html
                    }
                    
                    all_cards_data.append(card_data)
                    
                    # Print progress every 50 cards
                    if len(all_cards_data) % 50 == 0:
                        print(f"Processed {len(all_cards_data)} cards...")
                    
                except Exception as e:
                    print(f"Error extracting data from a card: {e}")
            
            # Check if we already have enough cards
            if len(all_cards_data) >= max_cards:
                print(f"Reached target of {max_cards} cards. Stopping.")
                break
                
            # Scroll to the bottom to trigger lazy loading
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            await asyncio.sleep(1)
            
            # Try to find and click the "Load more" button if visible
            try:
                load_more_button = await page.query_selector('button:has-text("Load more tools")')
                if load_more_button:
                    await load_more_button.scroll_into_view_if_needed()
                    await load_more_button.click()
                    print("Clicked 'Load more tools' button")
                    await asyncio.sleep(2)  # Wait for new content to load
                else:
                    # If button is not found, try scrolling more to check if more cards load
                    old_processed = len(all_cards_data)
                    await asyncio.sleep(3)
                    if old_processed == len(all_cards_data):
                        # No new cards loaded after scrolling, we might be at the end
                        print("No 'Load more' button found and no new cards loaded. We may have reached the end.")
                        # Break if we have at least 100 cards to ensure we got something
                        if len(all_cards_data) > 100:
                            break
            except Exception as e:
                print(f"Error during pagination: {e}")
        
        print(f"Total cards collected: {len(all_cards_data)}")
        await browser.close()
        
        return all_cards_data

def save_to_csv(cards, filename="bestofai_tools.csv"):
    if not cards:
        print("No cards to save!")
        # Still create a file with headers even if empty
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['title', 'rating', 'description', 'tags', 'likes', 'url', 'image_url', 'featured', 'outer_html'])
            writer.writeheader()
        return
        
    # Define the fields for the CSV file
    fields = list(cards[0].keys())
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for card in cards:
            writer.writerow(card)
            
    print(f"Data saved to {filename} with {len(cards)} cards")

async def main():
    print("Starting scraper for bestofai.com...")
    # Set max_cards to limit how many cards to scrape (default: 1000)
    cards = await scrape_bestofai(max_cards=1000)
    print(f"Scraped {len(cards)} cards")
    save_to_csv(cards)
    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())