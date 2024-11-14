"""test file"""
import yaml


with open("test.yml", "r", encoding="utf-8") as f:
    program = yaml.safe_load(f)

for string in program:
    print(string)
