import os
import json
import argparse


def add_answer(problem_id, answer):
    if not problem_id.startswith('B'):
        problem_id = '%03d' % int(problem_id)
    else:
        problem_id = f'B{int(problem_id[1:]):02d}'
    
    # prompt user to confirm
    print(f'Are you sure to add answer {repr(answer)} for problem {problem_id}? (y/n)')
    confirm = input()
    if confirm != 'y':
        print('Aborting...')
        return
    
    prob = json.load(open('ProblemInfo.json'))
    
    if problem_id not in prob:
        prob[problem_id] = {'answer': answer}
    else:
        if 'answer' in prob[problem_id]:
            print(f'Problem {problem_id} already has answer {repr(prob[problem_id]["answer"])}, replace it? (y/n)')
            confirm = input()
            if confirm != 'y':
                print('Aborting...')
                return
        prob[problem_id]['answer'] = answer
    
    prob = dict(sorted(prob.items(), key=lambda x: x[0]))
    json.dump(prob, open('ProblemInfo.json', 'w'), indent=4, ensure_ascii=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('problem_id', type=str)
    parser.add_argument('answer', type=int)
    args = parser.parse_args()
    add_answer(args.problem_id, args.answer)
    pass
