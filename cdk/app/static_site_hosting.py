"""Main Stack File."""
from aws_cdk import (
    core,
    aws_cloudfront as aws_cloudfront,
    aws_s3 as aws_s3,
    aws_wafv2 as waf2
)


class StaticSiteHosting(core.Construct):
    """defines stack infra."""

    def __init__(self, scope: core.Construct, myid: str) -> None:
        super().__init__(scope, myid)

        oai = aws_cloudfront.OriginAccessIdentity(
            self, 'OAI', comment="demo origin")

        # create s3 bucket, which hold static content
        self.bucket = aws_s3.Bucket(
            self, id="static_website_poc_id", bucket_name="techcoderunner-static-website", website_index_document='index.html',
            block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=core.RemovalPolicy.DESTROY
        )

        self.bucket.grant_read(oai)

        aws_cloudfront.CloudFrontWebDistribution(self,
            id='cloud_front_distribution_id',
            origin_configs=[aws_cloudfront.SourceConfiguration(
                s3_origin_source=aws_cloudfront.S3OriginConfig(
                    s3_bucket_source=self.bucket,
                    origin_access_identity=oai
                ),
                behaviors=[aws_cloudfront.Behavior(is_default_behavior=True)]
            )]
        )


