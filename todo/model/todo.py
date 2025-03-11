# TODO: Add code here
class Todo:
    def __init__(self, code_id: int , title: str , description : str ):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed: bool = False
        self.tags = []
    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
    def __str__(self) -> str :
        return f"{self.code_id} ,{self.title}"

class TodoBook:
    def __init__(self):
        self.todos: dict[int:Todo] = {}

    def add_todo(self , title , description) -> int:










