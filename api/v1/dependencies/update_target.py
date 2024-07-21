#!/usr/bin/python3
from models.target_model import Target
from models.user_model import User
from dependencies.get_db import get_db
from sqlalchemy import and_


def update_target(date, user_id):
    """
    update target total tasks
    or total done
    depends on arguments passed into function
    """
    db = next(get_db())

    target = db.query(Target).filter(and_(Target.user_id==user_id, Target.date.contains(date))).one_or_none()
    
    if target is None:
        target = Target(
            user_id=user_id,
            daily_target=db.query(User).filter(User.id==user_id).one().daily_target,
            tasks_total=1
        )
    else:
        target.tasks_total += 1
    
    db.add(target)
    db.commit()
    db.refresh(target)
