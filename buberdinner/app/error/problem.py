from httpproblem import Problem

from buberdinner.app.error.type_factory import get_type


class ApiProblem(Problem):
    def __init__(self, status: int, title=None, detail=None, instance=None, **kwargs):
        if "type" in kwargs:
            kwargs.pop("type")
        super().__init__(status, title, detail, get_type(status), instance, **kwargs)
