from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')
#블루프린트(blueprint)는 ‘ 청사진’을 뜻하는데, 플라스크에서는 URL과 호출되는 함수의 관계를 확인할 수 있는 Blueprint 클래스를 의미한다.
@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
#현재 _list 함수에 등록된 라우트는 @bp.route('/list/')이므로 url_for('question._list')는
#bp의 접두어인 /question/과 /list/가 더해진 /question/list/ URL을 반환한다.