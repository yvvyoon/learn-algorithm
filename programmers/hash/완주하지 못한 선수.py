def solution(participant, completion):
    answer = ''
    participant_hash = {}
    participant_count = len(participant)
    completion_count = len(completion)

    if participant_count < 1 or participant_count > 100000:
        return

    if completion_count - participant_count != -1:
        return

    for person in participant:
        if person in participant_hash.keys():
            participant_hash[person] += 1
        else:
            participant_hash[person] = 1

    for person in completion:
        if person in participant_hash.keys():
            participant_hash[person] -= 1

    for person, count in participant_hash.items():
        if count != 0:
            return person
