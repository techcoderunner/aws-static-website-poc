#!/usr/bin/env python3


from app.app_stack import AppStack


def main():
    app_stack = AppStack()

    app = app_stack.build()
    app.synth()


main()
