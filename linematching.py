import re
import sys
import argparse


class OutputStrategy:
    """This is abstract method
    this method does not return anything here """
    def output(self, file_name, line_num, start_pos, matched_text, line):
        raise NotImplementedError("Output method not implemented.")


class UnderscoreOutput(OutputStrategy):
    def output(self, file_name, line_num, start_pos, matched_text, line):
        print(f"{file_name}:{line_num}:{line.strip()}")
        underline = " " * start_pos + "^" * len(matched_text)
        print(underline)


class ColorOutput(OutputStrategy):
    def output(self, file_name, line_num, start_pos, matched_text, line):
        highlighted_line = (line[:start_pos] + "\033[91m" + matched_text + "\033[0m" +
                            line[start_pos + len(matched_text):])
        print(f"{file_name}:{line_num}:{highlighted_line.strip()}")


class MachineOutput(OutputStrategy):
    def output(self, file_name, line_num, start_pos, matched_text, line):
        print(f"{file_name}:{line_num}:{start_pos}:{matched_text}")


class StandardOutput(OutputStrategy):
    def output(self, file_name, line_num, start_pos, matched_text, line):
        print(f"{file_name}:{line_num}:{line.strip()}")


class Grep:
    def __init__(self, regex, files, output_strategy):
        self.regex = regex
        self.files = files
        self.output_strategy = output_strategy

    def process_line(self, file_name, line, line_num):
        for match in re.finditer(self.regex, line):
            start_pos = match.start()
            matched_text = match.group()
            self.output_strategy.output(file_name, line_num, start_pos, matched_text, line)

    def grep_files(self):
        if self.files:
            for file_name in self.files:
                try:
                    with open(file_name, 'r') as file:
                        for line_num, line in enumerate(file, 1):
                            self.process_line(file_name, line, line_num)
                except FileNotFoundError:
                    print(f"File {file_name} not found.", file=sys.stderr)
                except Exception as e:
                    print(f"An error occurred: {e}", file=sys.stderr)
        else:
            for line_num, line in enumerate(sys.stdin, 1):
                self.process_line("STDIN", line, line_num)


def main():
    parser = argparse.ArgumentParser(description="Search for lines matching regular expression in files or STDIN.")
    parser.add_argument('-r', '--regex', required=True, help="Regular expression to search for.")
    parser.add_argument('-f', '--files', nargs='*', help="Files to search in.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-u', '--underscore', action='store_true', help="Print '^' under the matching text.")
    group.add_argument('-c', '--color', action='store_true', help="Highlight matching text.")
    group.add_argument('-m', '--machine', action='store_true', help="Generate machine readable output.")

    args = parser.parse_args()

    if args.underscore:
        output_strategy = UnderscoreOutput()   # this defines an object
    elif args.color:
        output_strategy = ColorOutput()
    elif args.machine:
        output_strategy = MachineOutput()
    else:
        output_strategy = StandardOutput()

    grep = Grep(args.regex, args.files, output_strategy)
    grep.grep_files()


if __name__ == "__main__":
    main()
