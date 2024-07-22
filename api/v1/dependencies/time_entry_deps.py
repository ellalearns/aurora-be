#!/usr/bin/python3
from models.time_entry_model import TimeEntry
from dependencies.get_db import get_db
from sqlalchemy.orm.attributes import flag_modified


def add_time_entry(start, stop, task_id):
    """
    add a new time entry
    """
    db = next(get_db())

    time_entry = f"{start} - {stop}"

    entry = db.query(TimeEntry).filter(TimeEntry.task_id==task_id).one_or_none()
    if entry is None:
        print("is none")
        print("")
        print("")
        entry = TimeEntry(
            task_id=task_id,
            tracked_time=[]
        )
        db.add(entry)
        db.commit()
        db.refresh(entry)

    print("before adding time entry =>", entry.tracked_time)
    print("")
    print("")

    time_list = entry.tracked_time
    time_list.append(time_entry)

    entry.tracked_time = time_list

    flag_modified(entry, "tracked_time")
    db.commit()
    db.refresh(entry)

