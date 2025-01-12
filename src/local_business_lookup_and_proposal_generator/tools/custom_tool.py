from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

class MockEmailTool(BaseTool):
    name: str = "Send Mock Email"
    description: str = (
        "This tool sends a mock email to a recipient."
    )
    def _run(self, recipient: str, subject: str, body: str) -> bool:
        # Implementation goes here
        print(f"Mock email sent to {recipient} with subject: {subject}")
        return True
   

   class CSVWriterTool(BaseTool):
     name: str = "CSV Writer"
        description: str = (
        "This tool writes structured data to a CSV file."
    )
    def _run(file_name: str, data: list) -> str:
        """
        Writes data to a CSV file.

        Args:
            file_name (str): The name of the CSV file to write to.
            data (list): A list of rows, where each row is a list of values.

        Returns:
            str: A confirmation message or an error message.
        """
        try:
            # Open the file in write mode
            with open(file_name, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data)  # Write rows to the file
            return f"Data successfully written to {file_name}."
        except Exception as e:
            # Handle any errors during the file writing process
            return f"Failed to write to {file_name}. Error: {str(e)}"