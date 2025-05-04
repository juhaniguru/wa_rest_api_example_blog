class BlogAppNotFoundError(Exception):
    def __init__(self, message="Not found"):
        super(BlogAppNotFoundError, self).__init__(message)
        self.message = message