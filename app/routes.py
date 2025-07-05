from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file
from flask_login import login_required, current_user
from app.models import Synopsis
from app import db
from app.llm import generate_synopsis
import io

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/generate', methods=['POST'])
@login_required
def generate():
    title = request.form['title']
    genre = request.form['genre']
    style = request.form['style']
    tone = request.form['tone']
    length = request.form['length']
    language = request.form['language']
    batch = request.form.get('batch') == 'yes'

    results = []
    for _ in range(3 if batch else 1):
        synopsis_text = generate_synopsis(title, genre, style, tone, length, language)
        synopsis = Synopsis(
            title=title,
            genre=genre,
            style=style,
            tone=tone,
            length=length,
            language=language,
            content=synopsis_text,
            user_id=current_user.id
        )
        db.session.add(synopsis)
        results.append(synopsis_text)

    db.session.commit()
    return render_template('index.html', generated=results if batch else results[0])

@main.route('/history')
@login_required
def history():
    synopses = Synopsis.query.filter_by(user_id=current_user.id).order_by(Synopsis.created_at.desc()).all()
    return render_template('history.html', synopses=synopses)

@main.route('/download', methods=['POST'])
@login_required
def download():
    synopsis_id = request.form['synopsis_id']
    synopsis = Synopsis.query.get_or_404(synopsis_id)
    if synopsis.user_id != current_user.id:
        flash("Unauthorized download attempt.", "danger")
        return redirect(url_for('main.history'))

    file_content = f"Title: {synopsis.title}\n\n{synopsis.content}"
    return send_file(
        io.BytesIO(file_content.encode('utf-8')),
        mimetype='text/plain',
        as_attachment=True,
        download_name=f"{synopsis.title}_synopsis.txt"
    )
