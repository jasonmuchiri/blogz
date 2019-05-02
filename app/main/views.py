from flask import render_template, request, redirect, url_for, abort, flash, session
from . import main
from ..models import User, Post, Comments
from ..date_pipe import date_calc
from flask_login import login_required, current_user
from .. import db
from .forms import PostForm, CommentForm
from datetime import datetime
from functools import wraps
from ..email import updates_mail_message

def requires_admin(access_level):
  def decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
      if not session.get('username'):
        return redirect(url_for('auth.login'))
      user = User.find_by_username(session['username'])
      if not user.allowed(access_level):
        return redirect(url_for('main.index', message='You do not have the required permissions to access that'))
      return f(*args, **kwargs)
    return decorated_function
  return decorator

@main.route('/')
@login_required
def index():
  posts=Post.query.all()
  title='Welcome to Blogz'
  return render_template('index.html', title=title, posts=posts)

@main.route('/profile/user/<uname>/<id>')
def profile_user(id, uname):
  user = User.query.filter_by(username = uname).first()
  memberFor=date_calc(user.joined)
  return render_template('profile/profile.html', memberFor=memberFor)

@main.route('/profile/admin/<uname>/<id>')
def profile_admin(id, uname):
  nō_users=User.query.all()
  nō_posts=Post.query.all()
  return render_template('profile/admin.html', users=nō_users, posts=nō_posts)

@main.route('/writing-posts', methods=['GET', 'POST'])
@login_required
def write_post():
  users=User.query.all()
  form = PostForm()
  if form.validate_on_submit():
    post = Post(title=form.title.data, body=form.body.data)

    Post.save_post(post)
    return redirect(url_for('main.index'))

    update_mail_message('Update from Blogz', 'email/update_email', users.email)

  title='New Blog Post'
  return render_template('new_post.html', post=form, title=title)

@main.route('/view_comments/<id>')
def view_comments(id):
  user = User.query.filter_by(id=id).first()
  post = Post.query.filter_by(id=id).first()
  comments = Post.get_comments(post)

  return render_template('comments.html', comments=comments, post=post, user=user)

@main.route('/write-comment/<id>', methods=['GET', 'POST'])
def write_comments(id):
  form=CommentForm()
  post = Post.query.filter_by(id=id).first()
  user = User.query.filter_by(id=id).first()
  if form.validate_on_submit():
    comment = Comments(comment=form.comment.data, user=user, post_comments=post)
    comment.save_comment()

    return redirect(url_for('main.index'))

  return render_template('comment.html', comment=form, user=user, post=post)

@main.route('/delete-comments/<id>', methods=['GET', 'POST'])
def delete_comments(id):
  post = Post.query.filter_by(id=id).first()
  comment = Post.query.filter_by(post=id).first()
  user = User.query.filter_by(id=id).first()
  
  if user.access>0:
    return delete_comments(comment)
  
  return render_template('comment.html', comment=comments, post=post, user=user)
