#-*- coding: utf-8 -*-

import markdown as md
import random
from pprint import pprint

def generate_test_data():
    data = []

    for epoch in range(20):
        train_acc = random.randrange(1,100)  # train accuracy for current epoch
        test_acc = random.randrange(1,100)  # test accuracy for current epoch
        loss = random.randrange(1,100)  
        data.append({
            "epoch": epoch,
            "train_acc": train_acc,
            "test_acc": test_acc,
            "loss" : loss
        })

    return data

def analyze_data(data):
    final_epoch = data[-1]

    copied_data = data.copy()

    def sort_method(e):
        return e["train_acc"]
    
    copied_data.sort(key = sort_method)
    best_epoch = copied_data[-1]
    
    return final_epoch,best_epoch


def generate_markdown_table(data):

    if not data:
        return "", ""

    headers = list(data[0].keys())
    header_row = "| " + " | ".join(headers) + " |\n"
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |\n"
    table_rows = ""
    for row in data:
        table_rows += ("| " + " | ".join([str(row[header])
                       for header in headers]) + " |\n")

    markdown_string = header_row + separator_row + table_rows
    html_output = md.markdown(markdown_string, extensions=['tables'])

    return markdown_string, html_output


def generate_file(md_tuple):

    with open('test.md', 'w') as f:
        f.write(md_tuple[0])

    with open('test.html', 'w') as f:
        f.write(md_tuple[1])

data = generate_test_data()
pprint(analyze_data(data))
generate_file(generate_markdown_table(data))
