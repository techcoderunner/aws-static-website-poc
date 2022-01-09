from aws_cdk import (
    core,
    aws_iam as iam,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy
)

from static_site_hosting import StaticSiteHosting


class StaticWebHostingStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        static_web_hosting = StaticSiteHosting(
            self, "techcoderunner_static_web", bucket_name="techcoderunner-static-website")

        s3deploy.BucketDeployment(self, "DeployWebsite",
                                  sources=[
                                      s3deploy.Source.asset("webContent")],
                                  destination_bucket=static_web_hosting.bucket
                                  )
