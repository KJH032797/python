# 4글자 ~ 12글자
# 4개 연속된 값 X
# "@" or "!" 반드시 포함
from operator import contains


def is_valid_password(pw) :
    if len(pw) < 4 :
        return False
    elif len(pw) > 12 :
        return False
    elif pw[0] == pw[1] == pw[2] == pw[3] :
        return False
    elif not (contains(pw, "!") or contains(pw, "@")) :
        return False
    else :
        return True

def is_valid_password(pw) :
    if len(pw) < 4 :
        return False
    elif len(pw) > 12 :
        return False
    elif pw[0] == pw[1] == pw[2] == pw[3] :
        return False
    elif not (contains(pw, "!") or contains(pw, "@")) :
        return False

    return True