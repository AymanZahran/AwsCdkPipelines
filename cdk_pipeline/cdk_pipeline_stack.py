from aws_cdk import (
    # Duration,
    Stack,
    aws_codecommit as codecommit,
)
from constructs import Construct

#from pipeline_stage import WorkshopPipelineStage


class CdkPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Creates a CodeCommit repository called 'WorkshopRepo'
        repo = codecommit.Repository(
            self, 'WorkshopRepo',
            repository_name= "WorkshopRepo"
        )

        # Pipeline code goes here
