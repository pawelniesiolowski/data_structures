class Group(object):

    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
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
