
#!/usr/bin/python3



def matrix_mul(m_a, m_b):
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    result = []
    len_a = len(m_a[0])
    len_b = len(m_b[0])

    for a in range(len(m_a)):
        new_arr = []
        row = m_a[a]
        col = m_b[a]
        if len(row) != len_a:
            raise TypeError("each row of m_a must be of the same size")
        if len(col) != len_b:
            raise TypeError("each row of m_b must be of the same size")
        for i in range(len(col)):
            points = 0
            for j in range(len(row)):
                if type(row[j]) not in (int, float):
                    raise TypeError("m_a should contain only integers or floats")
                if type(m_b[j][i]) not in (int, float):
                    raise TypeError("m_b should contain only integers or floats")
                points += row[j] * m_b[j][i]
            new_arr.append(points)
        result.append(new_arr)
    return result
