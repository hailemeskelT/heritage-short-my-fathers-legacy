import argparse
from pipeline.validate import validate_storyboard
from pipeline.plan import create_plan
from pipeline.assemble import assemble_from_stills


def main():
    parser = argparse.ArgumentParser(description='Heritage Short storyboard-driven pipeline scaffold')
    parser.add_argument('command', choices=['validate','plan','assemble','run'])
    parser.add_argument('--storyboard', default='storyboard.json')
    args = parser.parse_args()

    data = validate_storyboard(args.storyboard)
    if args.command == 'validate':
        return
    if args.command == 'plan':
        create_plan(data)
        return
    if args.command == 'assemble':
        assemble_from_stills(data)
        return
    if args.command == 'run':
        create_plan(data)
        assemble_from_stills(data)


if __name__ == '__main__':
    main()
