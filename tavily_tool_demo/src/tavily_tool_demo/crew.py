from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tavily_tool_demo.tools.tavily_search import TavilySearchTool

tavily_search = TavilySearchTool()


# Uncomment the following line to use an example of a custom tool
# from tavily_tool_demo.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class TavilyToolDemoCrew:
    """TavilyToolDemo crew"""

    @agent
    def assistant(self) -> Agent:
        return Agent(
            config=self.agents_config["assistant"],
            tools=[tavily_search],
            verbose=True,
#            llm="groq/llama3-8b-8192",
			llm="groq/llama3-groq-8b-8192-tool-use-preview"
        )

    @task
    def assistant_task(self) -> Task:
        return Task(
            config=self.tasks_config["assistant_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TavilyToolDemo crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

