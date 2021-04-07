from flask import Flask, request, render_template, Response, Blueprint
from flask_login import login_required, current_user