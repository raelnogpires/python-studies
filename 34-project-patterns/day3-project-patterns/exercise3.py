# exercise 3
# you've been invited to work in a security update
# in the intern system of a company.
# this system attends the financial, support and sales dpts.
# respecting the general law of data protection,
# the company needs to assure that intern informations
# will be exposed only to those who needs it.

# support acount ->  access support system.
# sales and financial acounts -> access financial and sales systems.
# manager acount -> access support, financial and sales systems.

from abc import abstractmethod, ABC


class SystemAccess(ABC):
    def __init__(self, permission=False):
        ...

    def set_authorization(self, permission):
        ...


class FinanceSystemAcess(SystemAccess):
    def __init__(self, permission=False) -> None:
        self.name = "Finances"
        self.set_authorization = permission

    def set_authorization(self, permission: bool) -> None:
        self.permission = permission


class SalesSystemAcess(SystemAccess):
    def __init__(self, permission=False) -> None:
        self.name = "Sales"
        self.set_authorization = permission

    def set_authorization(self, permission: bool) -> None:
        self.permission = permission


class SupportSystemAccess(SystemAccess):
    def __init__(self, permission=False) -> None:
        self.name = "Support"
        self.set_authorization = permission

    def set_authorization(self, permission: bool) -> None:
        self.permission = permission


class Account(ABC):
    def __init__(self, username: str) -> None:
        self.username = username
        self.permissions = []
        self.create_account()

    @abstractmethod
    def create_account(self) -> None:
        ...

    def show_permissions(self):
        permissions = [permission.name for permission in self.permissions]
        return permissions

    def add_permission(self, permission: SystemAccess) -> None:
        self.permissions.append(permission)


class FinanceAccount(Account):
    def create_account(self) -> None:
        self.add_permission(FinanceSystemAcess(True))


class SupportFinaceAccount(Account):
    def create_account(self) -> None:
        self.add_permission(FinanceSystemAcess(True))
        self.add_permission(SupportSystemAccess(True))


class ManagerAccount(Account):
    def create_account(self) -> None:
        self.add_permission(FinanceSystemAcess(True))
        self.add_permission(SupportSystemAccess(True))
        self.add_permission(SalesSystemAcess(True))


if __name__ == "__main__":
    print("coworker name: ")
    name = input()
    print("choose code of account to be created: ")
    account_t = input(
        "\n1 - Finances \n2 - Finances Support \n3 - Manager\n"
    )

    if account_t == "1":
        account = FinanceAccount(name)
    elif account_t == "2":
        account = SupportFinaceAccount(name)
    elif account_t == "3":
        account = ManagerAccount(name)

    print(f"account created in the name of {account.username}")
    print(f'''access clear to the following systems: {
            account.show_permissions()
        }''')
