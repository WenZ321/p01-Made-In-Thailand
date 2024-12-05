'''
Wen Zhang, Daniel Park, Danny Huang, Sasha(Alex) Murokh
Made-in-Thailand
SoftDev
P01 - ArRESTed Development - Stock Visualizer Platform - XÆA-69
Time Spent:
Target Ship Date: 2024-12-13
'''

# Import necessary libraries
import sqlite3
import csv
import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
# import database

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def landing():
    return render_template("landing.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route("/main", methods=['GET', 'POST'])
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.debug = True
    app.run()