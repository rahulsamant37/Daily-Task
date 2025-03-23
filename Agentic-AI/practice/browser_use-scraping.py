from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
from pydantic import SecretStr
import asyncio
import os
import csv
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))

browser = Browser(
    config=BrowserConfig(
        chrome_instance_path='C:/Program Files/Google/Chrome/Application/chrome.exe',
    )
)

# Create agent with the model - modified for compliance
agent = Agent(
    task="""
    Go to LinkedIn and search for Entrepreneurship Cell or Innovation Cell. 
    For each public Company profile or page you find:
    1. Only collect information that is publicly visible without logging in
    2. Only collect information from the "Contact Info" section if it's publicly shared
    3. Limit to collecting organization name and public contact email and Contact Numbe if available
    4. Do not attempt to bypass any restrictions
    5. Collect information for up to 10 organizations only
    """,
    llm=llm,
    browser=browser,
)

async def main():
    # Run the agent
    result = await agent.run()
    
    # Process the results (assuming agent returns structured data)
    # This is a placeholder - actual implementation depends on what the agent returns
    org_data = []
    
    # In a real implementation, you would parse result to extract structured data
    # This is just an example structure
    example_data = [
        {"organization": "Example E-Cell", "email": "public-email@example.com", "contact no.": "8274328742", "website": "https://example.edu/ecell"},
        {"organization": "Sample Innovation Hub", "email": "contact@sample.org", "contact no.": "8272324742", "website": "https://sample.org"}
    ]
    
    # Save to CSV
    with open('data/organization_contacts.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["organization", "email", "contact no." "website"])
        writer.writeheader()
        writer.writerows(example_data)
    
    print(f"Data saved to organization_contacts.csv")
    
    input('Press Enter to close the browser...')
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())