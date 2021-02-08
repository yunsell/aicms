from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
#현재 _list 함수에 등록된 라우트는 @bp.route('/list/')이므로 url_for('question._list')는
#bp의 접두어인 /question/과 /list/가 더해진 /question/list/ URL을 반환한다.