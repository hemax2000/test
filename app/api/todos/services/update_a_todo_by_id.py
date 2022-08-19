from sqlalchemy.orm import Session

from ..helpers import get_todo
from ..schema import TodoUpdateRequest


def update_a_todo_by_id_(
    todo_id: str,
    body: TodoUpdateRequest,
    db_session: Session,
    current_user: dict,
):

    todo = get_todo(todo_id=todo_id, db_session=db_session, user_id=current_user["sub"])

    todo.title = body.title

    return todo
