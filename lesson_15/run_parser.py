from mails_parser import MailSegregator
import argparse

CATEGORIES = ("Security", "Refunds", "Troubleshooting", "Account", "Advertising_and_Collaboration",
              "Limits", "Payments", "Features", "Others")
file_name = "user_support_letters.csv"
result_file = "result.csv"


def run_main(start_file: str, res_file: str, to_console: bool = False):
    """This function runs mian process. Takes two files(to read and to write result of sorting)."""
    new_segregator = MailSegregator("finished_segregator", *CATEGORIES)
    new_segregator.read_mails_file(start_file)
    new_segregator.sort_mails()
    new_segregator.write_result_to_file(res_file)
    if to_console:
        new_segregator.return_result()


def parse():
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('-mails_file', '--start_file', type=str)
    parser.add_argument('-result_file', '--res_file', type=str)
    parser.add_argument('-write_to_console', '--write_to_console', type=str)
    args = parser.parse_args()
    return args.start_file, args.res_file, args.write_to_console


if __name__ == "__main__":
    firs_file, last_file, write_to_console = parse()
    write_to_console = True if write_to_console == "+" else False
    run_main(start_file=firs_file, res_file=last_file, to_console=write_to_console)
