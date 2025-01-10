from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import WebsiteSearchTool
from .tools.custom_tool import MockEmailTool
from crewai_tools import SerpApiGoogleSearchTool

@CrewBase
class LocalBusinessLookupAndProposalGeneratorCrew():
    """LocalBusinessLookupAndProposalGenerator crew"""

    @agent
    def business_lookup_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['business_lookup_specialist'],
            tools=[SerpApiGoogleSearchTool()],
        )

    @agent
    def email_proposal_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['email_proposal_writer'],
            tools=[MockEmailTool()],
        )


    @task
    def lookup_local_businesses_task(self) -> Task:
        return Task(
            config=self.tasks_config['lookup_local_businesses_task'],
            tools=[SerpApiGoogleSearchTool()],
        )

    @task
    def create_email_proposal_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_email_proposal_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the LocalBusinessLookupAndProposalGenerator crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
