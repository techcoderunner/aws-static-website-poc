from aws_cdk import(
    core,
    aws_iam as iam,
    aws_s3 as s3
)

class StaticWebHostingStack(core.Stack):

    def __init__(self,scope:core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope,id,**kwargs)

        
        