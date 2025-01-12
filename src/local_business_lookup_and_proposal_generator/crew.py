from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool, WebsiteSearchTool, SerpApiGoogleSearchTool, SerpApiGoogleShoppingTool, CSVSearchTool


@CrewBase
class LocalBusinessLookupAndProposalGeneratorCrew():
    """LocalBusinessLookupAndProposalGenerator crew"""

    @agent
    def product_lookup(self) -> Agent:
        return Agent(
            config=self.agents_config['product_lookup'],
            tools=[WebsiteSearchTool()],
        )

    @agent
    def business_lookup(self) -> Agent:
        return Agent(
            config=self.agents_config['business_lookup'],
            tools=[SerpApiGoogleSearchTool()],
        )

    @agent
    def create_email(self) -> Agent:
        return Agent(
            config=self.agents_config['create_email'],
        )

    @agent
    def csv_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['csv_writer'],
            tools=[CSVSearchTool()],
        )

    @task
    def lookup_products_task(self) -> Task:
        return Task(
            config=self.tasks_config['lookup_products_task'],
            tools=[SerpApiGoogleSearchTool()],            
        )

    @task
    def lookup_local_businesses_task(self) -> Task:
        return Task(
            config=self.tasks_config['lookup_local_businesses_task'],
            
        )
    @task
    def create_email_proposal_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_email_proposal_task'],
            
        )

    @task
    def write_to_csv_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_to_csv_task'],
            tools=[FileWriterTool()],
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
