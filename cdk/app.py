#!/usr/bin/env python3

from aws_cdk import core
from app.app_stack import AppStack


def main():
    app_stack = AppStack()

    app = app_stack.build()
    app.synth()


main()
