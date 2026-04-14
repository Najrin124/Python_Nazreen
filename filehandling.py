def get_last_n_lines(file_path, n=100):
    with open(file_path, "rb") as f:
        f.seek(0, 2)  # move to end of file
        file_size = f.tell()
        
        buffer = bytearray()
        pointer = file_size - 1
        lines = []

        while pointer >= 0 and len(lines) < n:
            f.seek(pointer)
            byte = f.read(1)
            
            if byte == b'\n':
                lines.append(buffer.decode()[::-1])
                buffer = bytearray()
            else:
                buffer.extend(byte)
            
            pointer -= 1

        if buffer:
            lines.append(buffer.decode()[::-1])

    return lines[::-1]


# Usage
last_lines = get_last_n_lines("log.txt", 100)

for line in last_lines:
    print(line)