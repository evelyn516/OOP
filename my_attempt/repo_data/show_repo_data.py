# API data is turned into instances of Repository class
class Show():

    all = []

    def __init__(self, data):
        self._name = data['name']
        self._description = data['description']
        self._created = data['created_at']
        self._forks = data["forks_count"]
        self._language = data["language"]
        self._url = data["url"]
        self._save()

    def _save(self):
        self.all.append(self)

    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1]


   

    
    

