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

    def to_dict(self):
        return {
            "name": self.name,
            "content": self.content,
            "priority": self.priority,
            "done": self.done
        }

    @staticmethod
    def from_dict(dict_data):
        todo = ToDo(dict_data["name"], dict_data["content"], dict_data["priority"])
        todo.done = dict_data["done"]
        return todo