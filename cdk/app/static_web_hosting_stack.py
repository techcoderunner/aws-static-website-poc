from aws_cdk import(
    core,
    aws_iam as iam,
    aws_s3 as s3,
    aws_s3_deployment as s3_deploy
)

from static_site_hosting import StaticSiteHosting

class StaticWebHostingStack(core.Stack):

    def __init__(self,scope:core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope,id,**kwargs)

        StaticSiteHosting(self,"techcoderunner_static_web")

        

        
        