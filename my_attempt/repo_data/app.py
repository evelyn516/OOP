from api import fetch_repo_list
from show_repo_data import Show

class CLI():
    ''' User interface '''
    def _init_(self):
        self._user_input = ""
        

    def start(self):
        self._username = input("What is your github username?:  ")
        fetch_repo_list(self._username)
        self.menu()

# User is shown a numbered list their repos by name
    def menu(self):
        for idx, repo in enumerate(Show.all, start=1):
            print(f'{idx}. {repo._name}')
        self.more_on_this_repo()

# User can input a number to see more details on the corresponding repository
    def more_on_this_repo(self):
        try:
            self._user_input = int(input("\nSelect a number to see more details on the corresponding repository:  "))
            if self._user_input == 'exit':
                return self.goodbye()
            if not self.valid_input(self._user_input):
                raise ValueError
            self.show_repo()
            self.more_on_this_repo()
        except ValueError:
            print(f'Please enter a number between 0 and {len(Show.all)}')
            self.menu()

    def show_repo(self):
        repo = Show.find_by_input(self._user_input)
        print(f'\nRepo: {repo._name}')
        print(f'\tDescription: {repo._description}')
        print(f'\tCreated: {repo._created}')
        print(f'\tForks: {repo._forks}')
        print(f'\tLanguage: {repo._language}')
        print(f'\tURL: {repo._url}')


    @staticmethod
    def valid_input(i):
        return int(i) > 0 and int(i) <= len(Show.all)

    @staticmethod
    def goodbye():
        print('\nGoodbye.')

if __name__ == '__main__':
    app = CLI()
