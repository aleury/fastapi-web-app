class Package:
    def __init__(
            self,
            name: str,
            summary: str,
            home_page: str,
            lic: str,
            author_name: str,
            description: str,
            maintainers: list = None,
    ):
        self.id = name
        self.name = name
        self.summary = summary
        self.home_page = home_page
        self.license = lic
        self.author_name = author_name
        self.description = description
        self.maintainers = maintainers or []
