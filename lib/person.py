#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name='no name', job='Sales'):
        if type(name) != str:
            print("Name must be string between 1 and 25 characters.")
        elif 1 < len(name) < 25:
            self.name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self.job = job

        