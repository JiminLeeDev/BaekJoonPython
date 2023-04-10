def Num1931():
    inputs = [input().split(" ") for idx in range(int(input()))]

    meetings = sorted(
        [[int(input[0]), int(input[1])] for input in inputs],
        key=lambda x: (x[1], x[0]),
    )

    meeting_idx = 0
    maximum_meeting_cnt = 0

    while meeting_idx < len(meetings):
        maximum_meeting_cnt += 1
        fixed_meeting = meetings[meeting_idx]

        meeting_idx += 1

        while (
            meeting_idx < len(meetings)
            and meetings[meeting_idx][0] < fixed_meeting[1]
            and meetings[meeting_idx][0] != meetings[meeting_idx][1]
        ):
            meeting_idx += 1

    print(maximum_meeting_cnt)


Num1931()
