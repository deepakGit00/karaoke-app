from flask import Blueprint, render_template, request, redirect
from app.models import db, Performance
from app.services import singer_conflict, duplicate_song, validate_duet

main = Blueprint('main', __name__)
