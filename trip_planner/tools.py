
import json
import os
import requests
from crewai import Agent, Task
from langchain.tools import tool
from dotenv import load_dotenv


# Initialize variables from `.env`
load_dotenv()
browserless_host = os.getenv("BROWSERLESS_URL")


## Define and create tools, as necessary

class SearchTool():
  @tool("Search the internet")
  def search_internet(query):
    """Useful to search the internet about a a given topic and return relevant results"""
    top_result_to_return = 4
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    # Send the request to search
    response = requests.request("POST", url, headers=headers, data=payload)
    # check if there is an organic key, don't include sponsor results
    if 'organic' not in response.json():
      return "Sorry, I couldn't find anything about that, there could be an error with you serper api key."
    else:
      results = response.json()['organic']
      string = []
      for result in results[:top_result_to_return]:
        try:
          string.append('\n'.join([
              f"Title: {result['title']}", f"Link: {result['link']}",
              f"Snippet: {result['snippet']}", "\n-----------------"
          ]))
        except KeyError:
          next
      return '\n'.join(string)



## Browser Tool using a network-local (but off-host) Browserless instance

from unstructured.partition.html import partition_html

class BrowserTool():
  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""
    # url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    url = "http://localhost:3000/content"
    payload = json.dumps({"url": website})
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []
    for chunk in content:
      chunking_agent = Agent(
          role='Principal Researcher',
          goal=
          """
          Review and fully understand website content in order to create concise and useful summaries 
          based on the content you are working with
          """,
          backstory=
          """
          You're a Principal Researcher at a large enterprise corporation and you have been tasked to perform research for your bosses.
          When you do an amazing job and provide clear and actionable detail from the research content, 
          you are given a bonus in your paycheck.
          """,
          allow_delegation=False)
      chunking_task = Task(
          agent=agent,
          description=
          f'Analyze and summarize the content bellow, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
      )
      summary = task.execute()
      summaries.append(summary)
    return "\n\n".join(summaries)


class CalculatorTool():
    @tool("Make a calculation")
    def calculate(operation):
        """Useful to perform any mathematical calculations, 
        like sum, minus, multiplication, division, etc.
        The input to this tool should be a mathematical 
        expression, a couple examples are `200*7` or `5000/2*10`
        """        
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"