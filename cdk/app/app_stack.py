from aws_cdk import core

from app.static_web_hosting_stack import StaticWebHostingStack

class AppStack:

    def __init__(self):
        self.app = core.App()

    def build(self) -> core.App:

        StaticWebHostingStack(
            self.app,
            "static-web-hosting-stack",
            env={'region':'us-east-1'}
        )

        return self.app
