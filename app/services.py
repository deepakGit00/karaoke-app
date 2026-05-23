from app.models import Performance, db

def singer_conflict(event_id, round_id, singer_id):
    return Performance.query.filter_by(
        event_id=event_id,
        round_id=round_id
    ).filter(
        (Performance.singer1 == singer_id) |
        (Performance.singer2 == singer_id)
    ).first()


def duplicate_song(event_id, song_title):
    return Performance.query.filter_by(
        event_id=event_id,
        song_title=song_title
    ).first()


def validate_duet(s1, s2):
    return s1 != s2
