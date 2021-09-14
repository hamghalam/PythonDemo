def count_path(m:int, n:int):
    """[summary]

    Args:
        m (int): [description]
        n (int): [description]

    Returns:
        [type]: [description]
    """
    if (m==1 or n==1):
        return 1
    return count_path(m-1, n) + count_path(m, n-1)

print(count_path(5,5))