class Group(object):

    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        if not isinstance(user, str) or user == '':
            raise ValueError('User must have a name')

        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    '''
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    '''
    for checked_user in group.get_users():
        if checked_user == user:
            return True

    for checked_group in group.get_groups():
        if is_user_in_group(user, checked_group) is True:
            return True

    return False


if __name__ == '__main__':

    # Basic tests data

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # Extended tests data

    parent2 = Group('parent2')
    child2 = Group('child2')
    second_child2 = Group('second_child2')
    sub_child2 = Group('subchild2')
    second_sub_child2 = Group('second_sub_child2')

    sub_child_user2 = 'sub_child_user2'
    sub_child2.add_user(sub_child_user2)

    second_sub_child_user2 = 'second_sub_child_user2'
    second_sub_child2.add_user(second_sub_child_user2)

    third_sub_child_user2 = 'third_sub_child_user2'
    second_sub_child2.add_user(third_sub_child_user2)

    child2.add_group(sub_child2)
    parent2.add_group(child2)
    second_child2.add_group(second_sub_child2)
    parent2.add_group(second_child2)

    quick_child2 = 'quick_child2'
    child2.add_user(quick_child2)

    # Tests

    result1 = is_user_in_group('sub_child_user', parent)
    assert result1 is True
    print(result1)
    # True

    result2 = is_user_in_group('sub_child_user2', parent2)
    assert result2 is True
    print(result2)
    # True

    result3 = is_user_in_group('second_sub_child_user2', parent2)
    assert result3 is True
    print(result3)
    # True

    result4 = is_user_in_group('quick_child2', parent2)
    assert result4 is True
    print(result4)
    # True

    result5 = is_user_in_group('not_existing_child', parent2)
    assert result5 is False
    print(result5)
    # False

    # Test empty user in group should throw exception

    some_group = Group('some_group');
    empty_user = ''

    exception_thrown = False
    try:
        some_group.add_user(empty_user)
    except ValueError:
        exception_thrown = True

    assert exception_thrown
    print(exception_thrown)

    # Test groups without users

    first_group = Group('first_group')
    second_group = Group('second_group')
    third_group = Group('third_group')

    first_group.add_group(second_group)
    second_group.add_group(third_group)

    result6 = is_user_in_group('some_user', first_group)
    assert result6 is False
    print(result6)
    # False
