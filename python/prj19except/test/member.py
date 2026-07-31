def check_pw_validation(pw) :
    if len(pw) < 4 :
        raise Exception("pw is too short")
    if len(pw) > 8 :
        raise Exception("pw is too long")

def join():
    print("sign up called")
    id = input("id : ")
    pw = input("password : ")
    check_pw_validation(pw)
    print("sign up finished")