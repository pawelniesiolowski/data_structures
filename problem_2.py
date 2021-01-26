import os


def find_files(suffix, path):
    '''
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    '''
    if os.path.isfile(path):
        return [path] if path.endswith(suffix) else []

    files = []
    if os.path.isdir(path):
        for f in os.listdir(path):
            files.extend(find_files(suffix, os.path.join(path, f)))
    return files


if __name__ == '__main__':

    # Tests

    result = find_files('.c', './testdir/subdir1')
    assert result == ['./testdir/subdir1/a.c']
    print(*result)
    # ./testdir/subdir1/a.c

    result = find_files('.c', './testdir')
    assert all(path in result for path in ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c'])
    print(*result, sep=', ')
    # ./testdir/subdir1/a.c, ./testdir/subdir3/subsubdir1/b.c, ./testdir/subdir5/a.c, ./testdir/t1.c (in arbitrary order)

    result = find_files('.not_existing', 'not_existing_path')
    assert result == []
    print(*result)
    # it found nothing for not existing values

    result = find_files('', './testdir/subdir1')
    # assert result == []
    assert all(path in result for path in ['./testdir/subdir1/a.h', './testdir/subdir1/a.c'])
    print(*result, sep=', ')
    # ./testdir/subdir1/a.h, ./testdir/subdir1/a.c (it found all files in path for empty string as suffix)
