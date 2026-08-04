class ToDo:
    def __init__(self, name, content, priority=2):
        self.name = name # 할 일 이름
        self.content = content # 내용
        self.priority = priority # 우선 순위
        self.done = False # 완료 여부

    def __str__(self):
        # 완료 체크 표시
        if self.done:
            status = "[V]"
        else :
            status = "[ ]"
        return f"{status} | {self.name}\n{self.content}\n"