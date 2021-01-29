import click
import os
import fitz  # this is pymupdf


@click.command()
@click.option('--pdf', prompt="pdf filepath")
@click.option('--dest', prompt="filename to save")

def parse_pdf(pdf, dest):
    """ Simple program to split a pdf into Abstract & Main text"""
    print("not implemented")
    with fitz.open(pdf) as doc:
        text = ""
        for page in doc:
            print(page.getText())

if __name__ == "__main__":
    parse_pdf()
